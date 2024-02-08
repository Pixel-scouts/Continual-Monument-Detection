import xml.etree.ElementTree as et
import os
import glob
import shutil

def copy_files_for_class(xml_path: str, image_path: str, label: str, destination_path: str,n:int):
    """
    Copy the image and XML files for the specified label to a new location.

    Args:
        xml_path (str): Path to the folder containing the annotations in XML format.
        image_path (str): Path to the folder containing the images.
        label (str): The label to search for.
        destination_path (str): Path to the destination folder for copied files.
    """
    i=0
    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)

    if not os.path.exists(destination_path+"\\annotations"):
        os.makedirs(destination_path+"\\annotations")
    if not os.path.exists(destination_path+'\\images'):
        os.makedirs(destination_path+'\\images')


    for xml_file in glob.glob(os.path.join(xml_path, '*.xml')):
        tree = et.parse(xml_file)
        root = tree.getroot()

        # Find all object elements with the specified label
        objects_to_copy = root.findall('.//object[name="{}"]'.format(label))

        # If objects with the label are found, copy the corresponding XML file
        if objects_to_copy:
            i+=1
            # Copy XML file
            xml_destination = os.path.join(destination_path,"annotations", os.path.basename(xml_file))
            shutil.copy(xml_file, xml_destination)

            # Extract image filename from XML file
            image_filename = os.path.splitext(os.path.basename(xml_file))[0] + '.jpg'

            # Copy corresponding image file from the image_path
            image_source = os.path.join(image_path, image_filename)
            image_destination = os.path.join(destination_path, "images",image_filename)
            shutil.copy(image_source, image_destination)

            if i==n:
                break

# Example usage:
copy_files_for_class(r"D:\Major\Inc_16\train_set\annotations", r"D:\Major\Inc_16\train_set\images", "pratappur temple", r"D:\Major\Dataset\subset1\istore16",15)
