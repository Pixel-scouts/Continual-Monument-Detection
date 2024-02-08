import argparse
import os
import cv2
import xml.etree.ElementTree as ET
import albumentations as A

def image_augmentation(images_dir, annotations_dir, output_dir,target_class,n):
    augmentation = [
        A.Rotate(limit=5, p=0.7),
        A.RandomBrightnessContrast(brightness_limit=(-0.1, 0.1), contrast_limit=0, p=0.8),
        A.HueSaturationValue(hue_shift_limit=10, sat_shift_limit=10, val_shift_limit=10, p=0.8),
        A.MedianBlur(blur_limit=3, p=0.8),
        A.MotionBlur(p=0.6),
    ]
    transform = A.Compose(augmentation, bbox_params=A.BboxParams(format='pascal_voc', label_fields=['category_id']))

    output_images_dir = os.path.join(output_dir, "augmented_images")
    output_annotations_dir = os.path.join(output_dir, "augmented_labels")

    os.makedirs(output_images_dir, exist_ok=True)
    os.makedirs(output_annotations_dir, exist_ok=True)

    image_files = os.listdir(images_dir)
    save_img = n
    img_count = 0
    for image_file in image_files:
        image_path = os.path.join(images_dir, image_file)

        xml_file = os.path.join(annotations_dir, os.path.splitext(image_file)[0] + ".xml")
        tree = ET.parse(xml_file)
        root = tree.getroot()

        bboxes = []
        class_labels = []
        for object_elem in root.findall('object'):
            class_label = object_elem.find('name').text
            # print(class_label)
            if class_label == target_class:
                if img_count % save_img != 0:
                    img_count += 1
                    continue

                image = cv2.imread(image_path)
                image_height, image_width = image.shape[:2]

                bndbox = object_elem.find('bndbox')
                x_min = int(bndbox.find('xmin').text)
                y_min = int(bndbox.find('ymin').text)
                x_max = int(bndbox.find('xmax').text)
                y_max = int(bndbox.find('ymax').text)
                bboxes.append([x_min, y_min, x_max, y_max])
                class_labels.append(class_label)
                # print("augmenting")

                augmented = transform(image=image, bboxes=bboxes, category_id=class_labels)
                transformed_image = augmented['image']
                transformed_bboxes = augmented['bboxes']

                output_image_file = os.path.join(output_images_dir, f"{os.path.splitext(image_file)[0]}_s_augmentation.jpg")
                cv2.imwrite(output_image_file, transformed_image)

                output_xml_file = os.path.join(output_annotations_dir, f"{os.path.splitext(image_file)[0]}_s_augmentation.xml")

                for i, bbox in enumerate(transformed_bboxes):
                    x_min, y_min, x_max, y_max = bbox

                    x_min = max(0, x_min)
                    y_min = max(0, y_min)
                    x_max = min(image_width, x_max)
                    y_max = min(image_height, y_max)
                    transformed_bboxes[i] = [x_min, y_min, x_max, y_max]

                    object_elem = root.findall('object')[i]
                    bndbox = object_elem.find('bndbox')
                    bndbox.find('xmin').text = str(int(x_min))
                    bndbox.find('ymin').text = str(int(y_min))
                    bndbox.find('xmax').text = str(int(x_max))
                    bndbox.find('ymax').text = str(int(y_max))

                tree.write(output_xml_file)
                img_count += 1

def augment_image(image_path,annot_path):
    '''neeeds to be properly implemented'''
    augmentation = [
        A.Rotate(limit=5, p=0.7),
        A.RandomBrightnessContrast(brightness_limit=(-0.1, 0.1), contrast_limit=0, p=0.8),
        A.HueSaturationValue(hue_shift_limit=10, sat_shift_limit=10, val_shift_limit=10, p=0.8),
        A.MedianBlur(blur_limit=3, p=0.8),
        A.MotionBlur(p=0.6),
    ]
    transform = A.Compose(augmentation, bbox_params=A.BboxParams(format='pascal_voc', label_fields=['category_id']))
    image = cv2.imread(image_path)
    image_height, image_width = image.shape[:2]

    tree = ET.parse(annot_path)
    root = tree.getroot()

    bboxes = []
    class_labels = []
    for object_elem in root.findall('object'):
        class_label = object_elem.find('name').text
        # print(class_label)
        if class_label == target_class:

            bndbox = object_elem.find('bndbox')
            x_min = int(bndbox.find('xmin').text)
            y_min = int(bndbox.find('ymin').text)
            x_max = int(bndbox.find('xmax').text)
            y_max = int(bndbox.find('ymax').text)
            bboxes.append([x_min, y_min, x_max, y_max])
            class_labels.append(class_label)
            # print("augmenting")

            augmented = transform(image=image, bboxes=bboxes, category_id=class_labels)
            transformed_image = augmented['image']
            transformed_bboxes = augmented['bboxes']
            
    return(transformed_image,transformed_bboxes)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Augment images and labels")
    parser.add_argument("-i", "--images_dir", type=str, help="Path to the images directory")
    parser.add_argument("-a", "--annotations_dir", type=str, help="Path to the annotations directory")
    parser.add_argument("-o", "--output_dir", type=str, help="Path to the output directory")
    parser.add_argument("-t", "--target_class", type=str, help="Target class name")
    parser.add_argument("-n", "--num", type=str, help="nth image to augment")
    args = parser.parse_args()

    images_dir = args.images_dir
    annotations_dir = args.annotations_dir
    output_dir = args.output_dir
    target_class=args.target_class
    n = int(args.num)

    image_augmentation(images_dir, annotations_dir, output_dir, target_class,n)
    print("Augmentation Complete")
