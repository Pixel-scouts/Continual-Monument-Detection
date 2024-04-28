import os

def check(annot_dir,img_dir):
    # print(annot_dir)
    # print(img_dir)
    annot_files = os.listdir(annot_dir)
    img_files = os.listdir(img_dir)
    annot_files = [os.path.splitext(file)[0] for file in annot_files]
    img_files = [os.path.splitext(file)[0] for file in img_files]
    # print(annot_files)
    # print(img_files)
    for file in annot_files:
        if file not in img_files:
            print(f"File {file} not found in images")
            return False
    for file in img_files:
        if file not in annot_files:
            print(f"File {file} not found in annotations")
            return False
    return True

if __name__ == "__main__":
    annot_dir = r"D:\Major\Dataset\subset4\base_set\annotations"
    img_dir = r"D:\Major\Dataset\subset4\base_set\images"
    print(check(annot_dir,img_dir))
    