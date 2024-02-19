
from torchvision.ops import MultiScaleRoIAlign
from torchvision.models.detection import FasterRCNN
from torchvision.models.detection import FasterRCNN_ResNet50_FPN_V2_Weights
from torchvision.models.resnet import resnet50, ResNet50_Weights
from torchvision.models._utils import  _ovewrite_value_param
from torchvision.models.detection.anchor_utils import AnchorGenerator
from torchvision.models.detection._utils import  overwrite_eps
from torchvision.ops import misc as misc_nn_ops
from torch import nn
from torchvision.models.detection.backbone_utils import _validate_trainable_layers, _resnet_fpn_extractor
from torchvision.models.detection.rpn import RPNHead
from typing import Any, Optional, TypeVar
from .warpped_head import WarpedHead


def _default_anchorgen():
    anchor_sizes = ((32,), (64,), (128,), (256,), (512,))
    aspect_ratios = ((0.5, 1.0, 2.0),) * len(anchor_sizes)
    return AnchorGenerator(anchor_sizes, aspect_ratios)


def fasterrcnn_resnet50_fpn_meta(
    *,
    weights: Optional[FasterRCNN_ResNet50_FPN_V2_Weights] = None,
    progress: bool = True,
    num_classes: Optional[int] = None,
    weights_backbone: Optional[ResNet50_Weights] = None,
    trainable_backbone_layers: Optional[int] = None,
    **kwargs: Any,
) -> FasterRCNN:
    """
    Constructs an improved Faster R-CNN model with a ResNet-50-FPN backbone from `Benchmarking Detection
    Transfer Learning with Vision Transformers <https://arxiv.org/abs/2111.11429>`__ paper.

    .. betastatus:: detection module

    It works similarly to Faster R-CNN with ResNet-50 FPN backbone. See
    :func:`~torchvision.models.detection.fasterrcnn_resnet50_fpn` for more
    details.

    Args:
        weights (:class:`~torchvision.models.detection.FasterRCNN_ResNet50_FPN_V2_Weights`, optional): The
            pretrained weights to use. See
            :class:`~torchvision.models.detection.FasterRCNN_ResNet50_FPN_V2_Weights` below for
            more details, and possible values. By default, no pre-trained
            weights are used.
        progress (bool, optional): If True, displays a progress bar of the
            download to stderr. Default is True.
        num_classes (int, optional): number of output classes of the model (including the background)
        weights_backbone (:class:`~torchvision.models.ResNet50_Weights`, optional): The
            pretrained weights for the backbone.
        trainable_backbone_layers (int, optional): number of trainable (not frozen) layers starting from
            final block. Valid values are between 0 and 5, with 5 meaning all backbone layers are
            trainable. If ``None`` is passed (the default) this value is set to 3.
        **kwargs: parameters passed to the ``torchvision.models.detection.faster_rcnn.FasterRCNN``
            base class. Please refer to the `source code
            <https://github.com/pytorch/vision/blob/main/torchvision/models/detection/faster_rcnn.py>`_
            for more details about this class.

    .. autoclass:: torchvision.models.detection.FasterRCNN_ResNet50_FPN_V2_Weights
        :members:
    """
    weights = FasterRCNN_ResNet50_FPN_V2_Weights.verify(weights)
    weights_backbone = ResNet50_Weights.verify(weights_backbone)

    if weights is not None:
        weights_backbone = None
        num_classes = _ovewrite_value_param("num_classes", num_classes, len(weights.meta["categories"]))
    elif num_classes is None:
        num_classes = 91

    is_trained = weights is not None or weights_backbone is not None
    trainable_backbone_layers = _validate_trainable_layers(is_trained, trainable_backbone_layers, 5, 3)

    backbone = resnet50(weights=weights_backbone, progress=progress)
    backbone = _resnet_fpn_extractor(backbone, trainable_backbone_layers, norm_layer=nn.BatchNorm2d)
    rpn_anchor_generator = _default_anchorgen()
    rpn_head = RPNHead(backbone.out_channels, rpn_anchor_generator.num_anchors_per_location()[0], conv_depth=2)
    box_head = WarpedHead(
        (backbone.out_channels, 7, 7), [256, 256, 256], [1024])
    model = FasterRCNN(
        backbone,
        num_classes=num_classes,
        rpn_anchor_generator=rpn_anchor_generator,
        rpn_head=rpn_head,
        box_head=box_head,
        **kwargs,
    )

    if weights is not None:
        model.load_state_dict(weights.get_state_dict(progress=progress, check_hash=True))

    return model