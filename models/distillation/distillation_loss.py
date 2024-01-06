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

#ROI Distillation Loss Calculation
def roi_distillation(student_logits, teacher_logits, student_localization, teacher_localization, temperature=1):
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
    soft_student_objectness = F.softmax(student_logits / temperature, dim=-1)
    soft_teacher_objectness = F.softmax(teacher_logits / temperature, dim=-1)
    
    
    sampled_pos_inds_subset = torch.where(teacher_logits > 0.7)[0]
    labels_pos = labels[sampled_pos_inds_subset]
    N, num_classes = student_logits.shape
    student_localization = student_localization.reshape(N, student_localization.size(-1) // 4, 4)
    teacher_localization = teacher_localization.reshape(N, teacher_localization.size(-1) // 4, 4)

    loc_distil_loss = F.smooth_l1_loss(
        student_localization[sampled_pos_inds_subset, labels_pos],
        teacher_localization[sampled_pos_inds_subset],
        beta=1 / 9,
        reduction="sum",
    )
     # L1 loss for bounding box regression
    loc_distil_loss = loc_distil_loss / (teacher_logits.numel()*num_classes)
    

    # KL divergence loss for objectness scores
    objectness_loss = F.kl_div(F.log_softmax(student_logits / temperature, dim=-1), soft_teacher_objectness, reduction='batchmean')

    # Combined ROI distillation loss
    roi_distillation_loss = objectness_loss + loc_distil_loss

    return sum(roi_distillation_loss)


def total_batch_loss(model_student, model_teacher,images,targets):
    imgs,targets =model_student.transform(images,targets)

    st_features = model_student.backbone(imgs.tensors)

    tc_features = model_teacher.backbone(imgs.tensors)

    if isinstance(st_features, torch.Tensor):
        st_features = OrderedDict([("0", st_features)])
    if isinstance(tc_features, torch.Tensor):
        tc_features = OrderedDict([("0", tc_features)])

    st_proposals,st_proposal_losses  = model_student.rpn(imgs,st_features,targets)
    tc_proposals,_  = model_teacher.rpn(imgs,st_features,None)

    st_proposals, matched_idxs, labels, regression_targets = model_student.roi_heads.select_training_samples(st_proposals, targets)
    st_box_features = model_student.roi_heads.box_roi_pool(st_features, st_proposals, imgs.image_sizes)
    st_box_features = model_student.roi_heads.box_head(st_box_features)
    st_class_logits, st_box_regression = model_student.roi_heads.box_predictor(st_box_features)

    loss_classifier, loss_box_reg = fastrcnn_loss(st_class_logits, st_box_regression, labels, regression_targets)

    losses = {"loss_classifier": loss_classifier, "loss_box_reg": loss_box_reg}

    tc_proposals, matched_idxs, _, _ = model_teacher.roi_heads.select_training_samples(tc_proposals, targets)
    tc_box_features = model_teacher.roi_heads.box_roi_pool(tc_features, tc_proposals, imgs.image_sizes)
    tc_box_features = model_teacher.roi_heads.box_head(tc_box_features)
    tc_class_logits, tc_box_regression = model_teacher.roi_heads.box_predictor(tc_box_features)
    
    fpn_distillation_loss = fpn_distillation(st_features,tc_features,temperature=1)
    roi_distillation_loss = roi_distillation(st_class_logits,tc_class_logits,st_box_regression,tc_box_regression)

    loss = loss_classifier+loss_box_reg+fpn_distillation_loss+roi_distillation_loss
    losses = {"loss_classifier": loss_classifier, 
              "loss_box_reg": loss_box_reg,
              "fpn_distillation_loss":fpn_distillation_loss,
              "roi_distillation_loss":roi_distillation_loss
             }
    return losses