import os
import shutil
import argparse
from sklearn.model_selection import train_test_split
import random

def split_dataset(img_folder,annot_folder, split_folder, test_size=0.1,val_size=0.1, random_state=42):
    # List all subfolders (class names) in the root folder
    class_folders = [folder for folder in os.listdir(img_folder) if os.path.isdir(os.path.join(img_folder, folder))]

    train_folder=os.path.join(split_folder,'train_set')
    test_folder=os.path.join(split_folder,'test_set')
    val_folder=os.path.join(split_folder,'val_set')
    # Create the train, test and validatoon folders if they don't exist
    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(os.path.join(train_folder, "images"), exist_ok=True)
    os.makedirs(os.path.join(train_folder, "annotations"), exist_ok=True)
    os.makedirs(test_folder, exist_ok=True)
    os.makedirs(os.path.join(test_folder, "images"), exist_ok=True)
    os.makedirs(os.path.join(test_folder, "annotations"), exist_ok=True)
    os.makedirs(val_folder, exist_ok=True)
    os.makedirs(os.path.join(val_folder, "images"), exist_ok=True)
    os.makedirs(os.path.join(val_folder, "annotations"), exist_ok=True)

    # Loop through each class folder and split the images and annotations into trai, test and validation set
    for class_folder in class_folders:
        print(f"Spliting Images in {class_folder} folder")
        image_folder = os.path.join(img_folder, class_folder)
        annotation_folder = os.path.join(annot_folder, class_folder)
        # Get a list of file names in each folder
        image_files = os.listdir(image_folder)
        
        image_files = [os.path.join(image_folder,img) for img in image_files]
        
        #  Calculate the number of elements to select 
        test_num = int(len(image_files) * test_size)
        val_num = int(len(image_files) * val_size)
       
        # randomly select test images
        test_images = random.sample(image_files, test_num)
        image_files = [element for element in image_files if element not in test_images]

        # randomly select val_images 
        val_images = random.sample(image_files, val_num)
        image_files = [element for element in image_files if element not in val_images]
       
        for image in test_images:
            annot=os.path.splitext(os.path.basename(image))[0]+ '.xml'
            annot_path=os.path.join(annotation_folder,annot)
            shutil.copy(image,os.path.join(test_folder, "images"))
            shutil.copy(annot_path,os.path.join(test_folder, "annotations"))
        
        for image in val_images:
            annot=os.path.splitext(os.path.basename(image))[0]+ '.xml'
            annot_path=os.path.join(annotation_folder,annot)
            shutil.copy(image,os.path.join(val_folder, "images"))
            shutil.copy(annot_path,os.path.join(val_folder, "annotations"))

        for image in image_files:
            annot=os.path.splitext(os.path.basename(image))[0]+ '.xml'
            annot_path=os.path.join(annotation_folder,annot)
            shutil.copy(image,os.path.join(train_folder, "images"))
            shutil.copy(annot_path,os.path.join(train_folder, "annotations"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split dataset images and annotation files into train and test sets.")
    parser.add_argument("-i","--img_folder", type=str, help="Path to the root folder containing class-wise images.")
    parser.add_argument("-a","--annot_folder", type=str, help="Path to the root folder containing class-wise annotations.")
    parser.add_argument("-s","--split_folder", type=str, help="Path to the folder where splited data will be stored.")
    parser.add_argument("-ts","--test_size", type=float, default=0.1, help="Proportion of test data (default: 0.1)")
    parser.add_argument("-vs","--val_size", type=float, default=0.1, help="Proportion of validation data (default: 0.1)")
    parser.add_argument("--random_state", type=int, default=42, help="Random state for data splitting (default: 42)")

    args = parser.parse_args()
    split_dataset(args.img_folder, args.annot_folder, args.split_folder, args.test_size,args.val_size, args.random_state)
    print("Spliting Complete")
