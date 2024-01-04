import torchvision
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
import torch
import torchvision.models as models
from torchvision.models.detection import FasterRCNN
from torchvision.models.detection.rpn import AnchorGenerator





# Define a custom Faster R-CNN model with additional return values
class CustomFasterRCNN(FasterRCNN):
    def forward(self, images, targets=None):
        if self.training and targets is None:
            raise ValueError("In training mode, targets should be passed to the forward method.")

        # Backbone feature extraction
        features = self.backbone(images.tensors)

        # Region Proposal Network
        proposals, proposal_losses = self.rpn(images, features, targets)

        # Intermediate features from the backbone
        backbone_features = features['0']  # Modify based on the actual backbone structure

        # Other components of the model
        x = self.roi_heads(features, proposals, images.image_sizes, targets)

        # Output dictionary with predictions and additional values
        result = {
            "boxes": x[0],
            "labels": x[1],
            "scores": x[2],
            "backbone_features": backbone_features,
            "proposals": proposals,
        }

        if self.has_keypoint_head:
            result.update({"keypoints": x[3]})

        # Add any other values you need to return

        if self.training:
            losses = {}
            losses.update(proposal_losses)
            losses.update(x[3])  # Assuming the last component of x is the losses from roi_heads
            return losses

        return result

# Load the pre-trained Faster R-CNN model with ResNet-50 backbone and FPN
model = models.detection.fasterrcnn_resnet50_fpn(pretrained=True)

# Modify the model to use the custom Faster R-CNN class
custom_model = CustomFasterRCNN(
    backbone=model.backbone,
    num_classes=model.roi_heads.box_predictor.cls_score.out_features,
    rpn_anchor_generator=AnchorGenerator(
        sizes=((32, 64, 128, 256, 512),),
        aspect_ratios=((0.5, 1.0, 2.0),)
    ),
)

# Put the custom model in evaluation mode
custom_model.eval()

# Forward pass with an example input
input_image = torch.randn(1, 3, 224, 224)  # Example input image
with torch.no_grad():
    predictions = custom_model(input_image)

# Access the prediction results and additional intermediate features
boxes = predictions["boxes"]
labels = predictions["labels"]
scores = predictions["scores"]
backbone_features = predictions["backbone_features"]
proposals = predictions["proposals"]

# ... (access any other values you added to the result dictionary)
def create_model(num_classes):
    
    # load Faster RCNN pre-trained model
    model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
    
    # get the number of input features 
    in_features = model.roi_heads.box_predictor.cls_score.in_features
    # define a new head for the detector with required number of classes
    model.roi_heads.box_predictor = FastRCNNPredictor(in_features, num_classes) 
    return model