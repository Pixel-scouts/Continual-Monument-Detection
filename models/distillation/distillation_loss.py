import torch.nn.functional as F

#FPN Distillation Loss Calculation
def fpn_distillation(st_features,tc_features,temperature=1):
    """
    Calculates the Feature Pyramid Network (FPN) distillation loss between student and teacher feature maps.

    Args:
        st_features (Dict[str, Tensor]): Student model's FPN feature maps at different levels.
        tc_features (Dict[str, Tensor]): Teacher model's FPN feature maps at corresponding levels.
        temperature (float, optional): Temperature parameter for distillation. Default is 1.

    Returns:
        Tensor: FPN distillation loss.
        
    The FPN distillation loss is computed by iterating over FPN levels, aligning the spatial resolutions of 
    student and teacher feature maps, and calculating the mean squared error (MSE) loss after interpolation.
    The losses for all levels are summed up and scaled by the temperature parameter.

    Example:
    ```python
    st_features = {'0': st_tensor0, '1': st_tensor1, '2': st_tensor2}
    tc_features = {'0': tc_tensor0, '1': tc_tensor1, '2': tc_tensor2}
    loss = fpn_distillation_loss(st_features, tc_features, temperature=2.0)
    ```

    """
    distillation_losses = []
    # Iterate over FPN levels
    for i in st_features.keys():  
        st_tensor = st_features[i]
        tc_tensor = tc_features[i]

        # Interpolate tensors to a common spatial resolution
        st_tensor_aligned = F.interpolate(st_tensor, size=(13, 13), mode='bilinear', align_corners=False)
        tc_tensor_aligned = F.interpolate(tc_tensor, size=(13, 13), mode='bilinear', align_corners=False)

        # Calculate distillation loss for the current FPN level
        distillation_loss = F.mse_loss(st_tensor_aligned, tc_tensor_aligned)
        distillation_loss *= temperature

        # Store the loss for this level
        distillation_losses.append(distillation_loss)

    # Sum the losses for all FPN levels
    fpn_distillation_loss = sum(distillation_losses)
    return fpn_distillation_loss

#FOI Distillation Loss Calculation
def roi_distillation(student_predictions, teacher_predictions, student_localization, teacher_localization, temperature=1):
    """
    Computes the region of interest (ROI) distillation loss between student and teacher predictions.

    Args:
        student_predictions (Tensor): Student model's objectness score predictions.
        teacher_predictions (Tensor): Teacher model's objectness score predictions.
        student_localization (Tensor): Student model's bounding box localization predictions.
        teacher_localization (Tensor): Teacher model's bounding box localization predictions.
        temperature (float, optional): Temperature parameter for distillation. Default is 1.

    Returns:
        Tensor: ROI distillation loss.
    """
    distillation_losses = []
    
    # Softmax along the objectness scores
    soft_student_objectness = F.softmax(student_predictions / temperature, dim=-1)
    soft_teacher_objectness = F.softmax(teacher_predictions / temperature, dim=-1)

    # L1 loss for bounding box regression
    localization_loss = F.smooth_l1_loss(student_localization, teacher_localization, reduction='none').sum(dim=-1)

    # KL divergence loss for objectness scores
    objectness_loss = F.kl_div(F.log_softmax(student_predictions / temperature, dim=-1), soft_teacher_objectness, reduction='batchmean')

    # Combined ROI distillation loss
    roi_distillation_loss = objectness_loss + localization_loss

    return sum(roi_distillation_loss)