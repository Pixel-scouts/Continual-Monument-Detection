import argparse
import os
import cv2
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import albumentations as A
import numpy as np

def image_augmentation(images_dir,annotations_dir,output_dir):
    augmentation = [
        A.Rotate(limit=5, p=1),
        A.RandomBrightnessContrast (brightness_limit=(-0.5,-0.4), contrast_limit=0, p=1),
        A.HueSaturationValue(p=1),
        A.MedianBlur(blur_limit=9, p=1),
        A.Blur(blur_limit=9, p=1),
    ]

    output_images_dir = os.path.join(output_dir, "augmented_images")
    output_annotations_dir = os.path.join(output_dir, "augmented_labels")


    os.makedirs(output_images_dir, exist_ok=True)
    os.makedirs(output_annotations_dir, exist_ok=True)

    image_files = os.listdir(images_dir)

    for image_file in image_files:
        image_path = os.path.join(images_dir, image_file)
        image = cv2.imread(image_path)
        image_height, image_width = image.shape[:2]

        xml_file = os.path.join(annotations_dir, os.path.splitext(image_file)[0] + ".xml")
        tree = ET.parse(xml_file)
        root = tree.getroot()

        bboxes = []
        class_labels = []
        for object_elem in root.findall('object'):
            class_label = object_elem.find('name').text
            bndbox = object_elem.find('bndbox')
            x_min = int(bndbox.find('xmin').text)
            y_min = int(bndbox.find('ymin').text)
            x_max = int(bndbox.find('xmax').text)
            y_max = int(bndbox.find('ymax').text)
            bboxes.append([x_min, y_min, x_max, y_max])
            class_labels.append(class_label)

        for idx, transform in enumerate(augmentation):
            transformed = transform(image=image, bboxes=bboxes, category_id=class_labels)
            transformed_image = transformed['image']
            transformed_bboxes = transformed['bboxes']

            for i, bbox in enumerate(transformed_bboxes):
                x_min, y_min, x_max, y_max = bbox

            # Bounding the coordinates of the bounding boxes
                x_min = max(0, x_min)
                y_min = max(0, y_min)
                x_max = min(image_width, x_max)
                y_max = min(image_height, y_max)
                transformed_bboxes[i] = [x_min, y_min, x_max, y_max]

            # Updating the XML file with the new bounding box coordinates
                object_elem = root.findall('object')[i]
                bndbox = object_elem.find('bndbox')
                bndbox.find('xmin').text = str(int(x_min))
                bndbox.find('ymin').text = str(int(y_min))
                bndbox.find('xmax').text = str(int(x_max))
                bndbox.find('ymax').text = str(int(y_max))

            # Saving augmented images and labels
            output_image_file = os.path.join(output_images_dir, f"{os.path.splitext(image_file)[0]}_{idx}.jpg")
            cv2.imwrite(output_image_file, transformed_image)
            output_xml_file = os.path.join(output_annotations_dir, f"{os.path.splitext(image_file)[0]}_{idx}.xml")
            tree.write(output_xml_file)

            # fig, axs = plt.subplots(1, 2, figsize=(10, 5))
            # axs[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            # axs[0].set_title('Original Image')
            # axs[0].axis('off')
            # axs[1].imshow(cv2.cvtColor(transformed_image, cv2.COLOR_BGR2RGB))
            # axs[1].set_title('Transformed Image')
            # axs[1].axis('off')
            # plt.tight_layout()
            # plt.show()

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Augment images and labels")
    parser.add_argument("-i", "--images_dir", type=str, help="Path to the images directory")
    parser.add_argument("-a", "--annotations_dir", type=str, help="Path to the annotations directory")
    parser.add_argument("-o", "--output_dir", type=str, help="Path to the output directory")
    args = parser.parse_args()    
    images_dir = args.images_dir
    annotations_dir = args.annotations_dir
    output_dir=args.output_dir

    image_augmentation(images_dir,annotations_dir,output_dir)
    print("Augmentation Complete")