import torch

def copy_weights(original_model, new_model, num_classes_original, num_classes_new, alpha=0.7, DEVICE='cpu'):
    """ 
    Copies weights from the original model to the new model
    """
    state_dict_original = original_model.state_dict()
    state_dict_new = new_model.state_dict()

    # Copy common layers
    for key in state_dict_original:
        if key in state_dict_new and state_dict_original[key].shape == state_dict_new[key].shape:
            state_dict_new[key] = state_dict_original[key]

    for key in state_dict_original:
        if key in state_dict_new and state_dict_original[key].shape == state_dict_new[key].shape:
            weighted_average = alpha * state_dict_original[key] + (1 - alpha) * state_dict_new[key]
            state_dict_original[key] = weighted_average

    # Copy class-specific layers with adjustment for the last class
    classes_difference = num_classes_new - num_classes_original
    
    # Copy weights and biases for the existing classes
    state_dict_new['roi_heads.box_predictor.cls_score.weight'][:num_classes_original] = state_dict_original['roi_heads.box_predictor.cls_score.weight']
    state_dict_new['roi_heads.box_predictor.cls_score.bias'][:num_classes_original] = state_dict_original['roi_heads.box_predictor.cls_score.bias']
    state_dict_new['roi_heads.box_predictor.bbox_pred.weight'][:num_classes_original*4] = state_dict_original['roi_heads.box_predictor.bbox_pred.weight']
    state_dict_new['roi_heads.box_predictor.bbox_pred.bias'][:num_classes_original*4] = state_dict_original['roi_heads.box_predictor.bbox_pred.bias']
    
    print("original weights and Bias Copied")
    
    # Load the updated state_dict into the new model
    new_model.load_state_dict(state_dict_new)

    return new_model

def copy_additional_weights(new_model, addition_model, num_classes_original, num_classes_new, alpha = 0.5,DEVICE='cpu'):
    # Copies weights from the additional model to the new model
    new_model.to(DEVICE)
    addition_model.to(DEVICE)
    state_dict_original = new_model.state_dict()
    state_dict_addition = addition_model.state_dict()

    for key in state_dict_original:
        if key in state_dict_addition and state_dict_original[key].shape == state_dict_addition[key].shape:
            weighted_average = alpha * state_dict_original[key] + (1 - alpha) * state_dict_addition[key]
            state_dict_original[key] = weighted_average
    # Copy class-specific layers with adjustment for the last class
    total_classes = num_classes_new + num_classes_original
    
    # Copy weights and biases for the existing classes
    state_dict_original['roi_heads.box_predictor.cls_score.weight'][num_classes_original:total_classes] = state_dict_addition['roi_heads.box_predictor.cls_score.weight']
    state_dict_original['roi_heads.box_predictor.cls_score.bias'][num_classes_original:total_classes] = state_dict_addition['roi_heads.box_predictor.cls_score.bias']
    state_dict_original['roi_heads.box_predictor.bbox_pred.weight'][num_classes_original*4:total_classes*4] = state_dict_addition['roi_heads.box_predictor.bbox_pred.weight']
    state_dict_original['roi_heads.box_predictor.bbox_pred.bias'][num_classes_original*4:total_classes*4] = state_dict_addition['roi_heads.box_predictor.bbox_pred.bias']
    
    print("Additional weights and Bias Copied")
    
    # Load the updated state_dict into the new model
    new_model.load_state_dict(state_dict_original)

    return new_model