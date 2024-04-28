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

def get_sorted_classes(path):
    """
    counts the number of instance of each class present in the dataset and returns it as a dictionary.
    
    Args:
        path: path to folder containing the annotation in XML format
        
    """
    classes=get_classes(path)
    classes = dict(sorted(classes.items(), key=lambda item: item[1], reverse=True))
    for key in classes:
        print(f"{key}:{classes[key]}")

    return classes



def get_file(path:str,label:str):
    """
    Search for the given label in the dataset and returns the files containing that label
    
    Args:
        path: path to folder containing the annotation in XML format
        label: The label to search for
        
    """
    files=[]

    for xml_file in glob.glob(path + '/*.xml'):
        tree = et.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            class_name = member.find('name').text
            if(class_name=='\\'):
               files.append(xml_file.encode("unicode_escape"))
            elif(class_name==label):
                files.append(xml_file.encode("unicode_escape"))

    return files

            

def get_null_file(path:str):
    """
    Search for the given label in the dataset and returns the files containing that label
    
    Args:
        path: path to folder containing the annotation in XML format
        label: The label to search for
        
    """
    null_files=[]
    for xml_file in glob.glob(path + '/*.xml'):
        tree = et.parse(xml_file)
        root = tree.getroot()

        if (len(root.findall('object'))==0):

            null_files.append(xml_file.encode("unicode-escape"))
    return null_files
            

