import xml.etree.ElementTree as et
import glob as glob
import os

# path = r"D:\Major\Dataset\check\annotation\IMG_20230729_164027_1.xml"  # Correct file path
# doc = et.parse(path)

# target_name = "taleju bell_BDS"
# target = doc.find(f'.//object[name="{target_name}"]')

# if target is not None:
#     # Target element found, remove it from the root
#     doc.getroot().remove(target)
#     et.ElementTree(doc.getroot()).write(path)  # Save the modified tree back to the file
#     # print(et.tostring(doc.getroot()).decode())
# else:
#     print(f"Element with name '{target_name}' not found.")


def remove_obj(path: str, label: str):
    """
    Remove the specified label from the dataset annotations.

    Args:
        path (str): Path to the folder containing the annotations in XML format.
        label (str): The label to remove.
    """
    for xml_file in glob.glob(os.path.join(path, '*.xml')):
        tree = et.parse(xml_file)
        root = tree.getroot()

        # Find all object elements with the specified label
        objects_to_remove = root.findall('.//object[name="{}"]'.format(label))

        # Remove each found object element
        for obj in objects_to_remove:
            root.remove(obj)

        # Save the modified XML tree back to the file
        et.ElementTree(root).write(xml_file)

# remove_obj(r"D:\Major\Dataset\subset3\base_set\annotations", "shveta bhairava")
        

def rename_label(path: str, old_label: str, new_label: str):
    """
    Rename the specified label in the dataset annotations.

    Args:
        path (str): Path to the folder containing the annotations in XML format.
        old_label (str): The label to rename.
        new_label (str): The new label to use.
    """
    for xml_file in glob.glob(os.path.join(path, '*.xml')):
        tree = et.parse(xml_file)
        root = tree.getroot()

        # Find all object elements with the specified old label
        objects_to_rename = root.findall('.//object[name="{}"]'.format(old_label))

        # Rename each found object element
        for obj in objects_to_rename:
            obj.find('name').text = new_label

        # Save the modified XML tree back to the file
        et.ElementTree(root).write(xml_file)

rename_label(r"D:\Major\Dataset\subset4\annotations", "bhimsen temple", "Bhimsen Temple")

