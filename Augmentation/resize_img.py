
import tensorflow as tf
import cv2
import numpy as np
import os

# replace with the folder containing images to resize
folder_path = 'E:\Major Project\Images\Original Images\\Pashupati Baneshwor Naxal'  

# replace with the actual folder name to store resized images
output_folder = "E:\Major Project\Images\Resized Images\\Pashupati Baneshwor Naxal"
os.makedirs(output_folder, exist_ok=True)


files = os.listdir(folder_path)
image_files = [file for file in files if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
# print(image_files)
for image_file in image_files:
    image_path = os.path.join(folder_path, image_file)
    # Load each imageh
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
    output_path = os.path.join(output_folder, image_file)
    cv2.imwrite(output_path, res_img_np)

print("resizing complete")