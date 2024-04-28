import os
import shutil
import argparse
from sklearn.model_selection import train_test_split
import random
import xml.etree.ElementTree as ET
from class_list import get_classes


def check_class(xml_path,class_name):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    objects_to_copy = root.findall('.//object[name="{}"]'.format(class_name))
    # print(objects_to_copy)
    return bool(objects_to_copy)

def split_dataset(img_folder, annot_folder, split_folder, target_class, test_size=0.1, val_size=0.1, random_state=42):
    # class_folders = [folder for folder in os.listdir(img_folder) if os.path.isdir(os.path.join(img_folder, folder))]

    train_folder = os.path.join(split_folder, 'train_set')
    test_folder = os.path.join(split_folder, 'test_set')
    val_folder = os.path.join(split_folder, 'val_set')

    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(os.path.join(train_folder, "images"), exist_ok=True)
    os.makedirs(os.path.join(train_folder, "annotations"), exist_ok=True)
    os.makedirs(test_folder, exist_ok=True)
    os.makedirs(os.path.join(test_folder, "images"), exist_ok=True)
    os.makedirs(os.path.join(test_folder, "annotations"), exist_ok=True)
    os.makedirs(val_folder, exist_ok=True)
    os.makedirs(os.path.join(val_folder, "images"), exist_ok=True)
    os.makedirs(os.path.join(val_folder, "annotations"), exist_ok=True)

    print(f"Splitting Images in folder")
    image_folder = os.path.join(img_folder)
    annotation_folder = os.path.join(annot_folder)

    xml_files = os.listdir(annotation_folder)
    target_xml_files = [os.path.join(annotation_folder,xml_file) for xml_file in xml_files if check_class(os.path.join(annotation_folder,xml_file), target_class)]
    print(len(target_xml_files))
    # image_files = os.listdir(image_folder)
    # image_files = [os.path.join(image_folder, img) for img in image_files]

    # Filtering images by class
    # class_images = [img for img in image_files if target_class in img]

    test_num = int(len(target_xml_files) * test_size)
    val_num = int(len(target_xml_files) * val_size)

    test_xml = random.sample(target_xml_files, test_num)
    target_xml_files = [element for element in target_xml_files if element not in test_xml]

    val_xml = random.sample(target_xml_files, val_num)
    target_xml_files = [element for element in target_xml_files if element not in val_xml]
    print(f"Train : {len(target_xml_files)},Test: {test_num}, Val: {val_num}")

    for xml in test_xml:
        image = os.path.splitext(os.path.basename(xml))[0] + '.jpg'
        image_path = os.path.join(image_folder, image)

        shutil.move(image_path, os.path.join(test_folder, "images"))
        shutil.move(xml, os.path.join(test_folder, "annotations"))

    for xml in val_xml:
        image = os.path.splitext(os.path.basename(xml))[0] + '.jpg'
        image_path = os.path.join(image_folder, image)

        # Check if the target class exists in the XML file
        shutil.move(image_path, os.path.join(val_folder, "images"))
        shutil.move(xml, os.path.join(val_folder, "annotations"))

    for xml in target_xml_files:
        image = os.path.splitext(os.path.basename(xml))[0] + '.jpg'
        image_path = os.path.join(image_folder, image)

        # Check if the target class exists in the XML file
        shutil.move(image_path, os.path.join(train_folder, "images"))
        shutil.move(xml, os.path.join(train_folder, "annotations"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split dataset images and annotation files into train and test sets.")
    parser.add_argument("-i", "--img_folder", type=str, help="Path to the root folder containing class-wise images.")
    parser.add_argument("-a", "--annot_folder", type=str, help="Path to the root folder containing class-wise annotations.")
    parser.add_argument("-s", "--split_folder", type=str, help="Path to the folder where split data will be stored.")
    parser.add_argument("-c", "--target_class", type=str, help="Target class to filter XML files.")
    parser.add_argument("-ts", "--test_size", type=float, default=0.1, help="Proportion of test data (default: 0.1)")
    parser.add_argument("-vs", "--val_size", type=float, default=0.1, help="Proportion of validation data (default: 0.1)")
    parser.add_argument("--random_state", type=int, default=42, help="Random state for data splitting (default: 42)")

    args = parser.parse_args()
    classes=get_classes(args.annot_folder)
    # for class_name in classes:
        # print(f"Splitting {class_name} images")
        # split_dataset(args.img_folder, args.annot_folder, args.split_folder, class_name, args.test_size, args.val_size, args.random_state)
    split_dataset(args.img_folder, args.annot_folder, args.split_folder, args.target_class, args.test_size, args.val_size, args.random_state)
    print("Splitting Complete")