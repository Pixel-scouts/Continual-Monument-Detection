
import tensorflow as tf
import cv2
import numpy as np
import os
import xml.etree.ElementTree as et
import matplotlib.pyplot as plt

# replace with the folder containing images to resize
images_path = 'E:\Major Project\Images\Original Images and Annotations\JPEGImages'  
annotations_path = 'E:\Major Project\Images\Original Images and Annotations\Annotations'  

# replace with the actual folder name to store resized images
output_image = "E:\Major Project\Images\Resized\\images"
output_annotation = "E:\Major Project\Images\Resized\\annotations"
os.makedirs(output_image, exist_ok=True)
os.makedirs(output_annotation, exist_ok=True)


image_list = os.listdir(images_path)
annotation_list = os.listdir(annotations_path)
image_files = [file for file in image_list if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
annotation_files = [file for file in annotation_list if file.lower().endswith('.xml')]
# print(image_files)
# print(annotation_files)
for i, (image_file, annotation_file) in enumerate(zip(image_files, annotation_files)):
    image_path = os.path.join(images_path, image_file)
    annot_filename = image_file[:-4] + '.xml'
    annotation_path = os.path.join(annotations_path, annot_filename)
    scale_factor=1
    # Load each imageh
    try:
        img = cv2.imread(image_path)
        # img = tf.image.decode_image(tf.io.read_file(image_path))

        # Load and parse the XML annotation
        tree = et.parse(annotation_path)
        root = tree.getroot()
        
        # Get the original image size from the XML
        width = int(root.find('size/width').text)
        height = int(root.find('size/height').text)
        if width>height:
            scale_factor=512/width
        else:
            scale_factor=512/height

       
    #    Resize the image to 512x512 using tf.image.resize_with_pad()
        res_img = tf.image.resize_with_pad(
            img,
            512,
            512,
            method='bilinear',
            antialias=False
        )
        
       
        new_width=int(width*scale_factor)
        new_height=int(height*scale_factor)

        # calculate the padding added during resizing
        padding_top=(512-new_height)//2
        padding_left=(512-new_width)//2
        padding_bottom=512-new_height-padding_top
        padding_right=512-new_width-padding_left
        
        # scale the new bounding box wrt resized image and padding added
        for obj in root.findall('object'):
            xmin = int(obj.find('bndbox/xmin').text)
            ymin = int(obj.find('bndbox/ymin').text)
            xmax = int(obj.find('bndbox/xmax').text)
            ymax = int(obj.find('bndbox/ymax').text)

            # Scale the coordinates
            xmin_scaled = int((xmin * scale_factor) + padding_left)
            ymin_scaled = int((ymin * scale_factor) + padding_top)
            xmax_scaled = int((xmax * scale_factor) + padding_left)
            ymax_scaled = int((ymax * scale_factor) + padding_top)

            # Update the XML with the scaled coordinates
            obj.find('bndbox/xmin').text = str(xmin_scaled)
            obj.find('bndbox/ymin').text = str(ymin_scaled)
            obj.find('bndbox/xmax').text = str(xmax_scaled)
            obj.find('bndbox/ymax').text = str(ymax_scaled)        
        
    except Exception as e:
        # shows which files couldn't be resized
        print(f"error in {image_path}\{str(e)}")
        continue

    # Convert EagerTensor to NumPy array
    res_img_np=res_img.numpy()
    output_path = os.path.join(output_image, image_file)

    # save thee resized image
    cv2.imwrite(output_path, res_img_np)
    

    updated_annotation_xml = et.tostring(root)
 
    output_xml_path = os.path.join(output_annotation, annot_filename)

    # Open the file in write mode
    with open(output_xml_path, "wb") as file:
    # Write the updated XML content into the file
        file.write(updated_annotation_xml)
    
    print(f"No. {i}: Image file - {image_file}, Annotation file - {annot_filename}")

print("Resizing Complete:")
   

