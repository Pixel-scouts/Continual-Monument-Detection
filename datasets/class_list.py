from xml.etree import ElementTree as et
import glob as glob

def get_classes(path):
    """
    counts the number of instance of each class present in the dataset and returns it as a dictionary.
    
    Args:
        path: path to folder containing the annotation in XML format
        
    """
    classes={}
    for xml_file in glob.glob(path + '/*.xml'):
        tree = et.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            class_name = member.find('name').text
            if(class_name=='\\'):
               print(xml_file)
            classes[class_name] = classes.get(class_name, 0) + 1
    return classes

def get_file(path:str,label:str):
    """
    Search for the given label in the dataset and returns the files containing that label
    
    Args:
        path: path to folder containing the annotation in XML format
        label: The label to search for
        
    """

    for xml_file in glob.glob(path + '/*.xml'):
        tree = et.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            class_name = member.find('name').text
            if(class_name=='\\'):
               print(xml_file)
            elif(class_name==label):
                print(xml_file)
            

def get_null_file(path:str,label:str):
    """
    Search for the given label in the dataset and returns the files containing that label
    
    Args:
        path: path to folder containing the annotation in XML format
        label: The label to search for
        
    """

    for xml_file in glob.glob(path + '/*.xml'):
        tree = et.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            class_name = member.find('name').text
            if(class_name=='\\'):
               print(xml_file)
            elif(class_name==label):
                print(xml_file)
            
