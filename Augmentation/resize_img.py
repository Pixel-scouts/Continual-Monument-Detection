
import tensorflow as tf
import cv2
import numpy as np
import os
import argparse


def resize_image(source_dir:str,output_dir:str):
    """
    resize images from the given folder and saves to output directory.
    
    Parameters:
    - source_dir (String): Path to source directory with original images
    - output_dir (String): Path to directory to save resized images
    """

    # list all the files in given folder
    files = os.listdir(source_dir)
    # get the images from list of all the files in given folder
    image_files = [file for file in files if file.lower().endswith(('.jpg', '.jpeg', '.png'))]
    # create output directory if not exist
    os.makedirs(output_dir, exist_ok=True)

    # iterate through each image and resize it
    for image_file in image_files:
        image_path = os.path.join(source_dir, image_file)
        # Load each image
        try:
            img = cv2.imread(image_path)

            # Resize the image with padding
            res_img = tf.image.resize_with_pad(
                img,
                512,
                512,
                method='bilinear',
                antialias=False
            )
        except:
            # shows which files couldn't be resized
            print(f"error in {image_file}")
            continue
        # Convert EagerTensor to NumPy array
        res_img_np = res_img.numpy()

        # Save the resized image
        output_path = os.path.join(output_dir, image_file)
        cv2.imwrite(output_path, res_img_np)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Resize',description="Resizes Images in the given folder")
    parser.add_argument("-s", "--source", type=str, help="Path to the directory containing original Images")
    parser.add_argument("-o", "--output", type=str, help="Path to the output directory")
    args = parser.parse_args()
    source_path = args.source
    output_dir = args.output

    resize_image(source_path,output_dir)
    