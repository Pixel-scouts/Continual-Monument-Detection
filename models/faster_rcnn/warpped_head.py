
from torch import nn
import torch.nn.functional as F

from typing import  Tuple, List


class ResidualBlock(nn.Module):
    def __init__(self, in_channels, out_channels):
        super(ResidualBlock, self).__init__()
        self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size=3, stride=1, padding=1, bias=False)
        self.bn1 = nn.BatchNorm2d(out_channels)

        self.conv2 = nn.Conv2d(out_channels, out_channels, kernel_size=3, stride=1, padding=1, bias=False)
        self.bn2 = nn.BatchNorm2d(out_channels)

        self.warp = nn.Conv2d(out_channels, out_channels, kernel_size=3, stride=1, padding=1, bias=False)
        self.warpbn = nn.BatchNorm2d(out_channels)
        self.relu = nn.ReLU(inplace=True)
        

    def forward(self, x):
        residual = x

        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)

        out = self.conv2(out)
        out = self.bn2(out)
        out = self.relu(out)

        warp_out = self.warp(out)
        warp_out = self.warpbn(warp_out)
        # warp_out = self.warprelu(warp_out)

        # Element-wise addition with input as a residual connection
        out = residual + warp_out
        out = self.relu(out)
        return out

class WarpedHead(nn.Sequential):
    def __init__(
        self,
        input_size: Tuple[int, int, int],
        residual_blocks: List[int],
        fc_layers: List[int],
    ):
        in_channels, in_height, in_width = input_size

        blocks = []
        previous_channels = in_channels
        for out_channels in residual_blocks:
            # Replace Conv2dNormActivation with ResidualBlock
            blocks.append(ResidualBlock(previous_channels, out_channels))
            previous_channels = out_channels

        blocks.append(nn.Flatten())

        # Calculate the input size for the first fully connected layer
        fc_input_size = previous_channels * in_height * in_width

        for current_channels in fc_layers:
            blocks.append(nn.Linear(fc_input_size, current_channels))
            blocks.append(nn.ReLU(inplace=True))
            fc_input_size = current_channels

        super().__init__(*blocks)

        # Initialize weights
        for layer in self.modules():
            if isinstance(layer, nn.Conv2d) or isinstance(layer, nn.Linear):
                nn.init.kaiming_normal_(layer.weight, mode="fan_out", nonlinearity="relu")
                if layer.bias is not None:
                    nn.init.zeros_(layer.bias)
