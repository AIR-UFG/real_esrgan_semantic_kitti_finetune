from tqdm import tqdm # pip 
from PIL import Image
import numpy as np #pip
import shutil
import os

def split_aux(splited_list):
    splited_array = np.array(splited_list)
    # splited_array = splited_array.reshape(16, 1024)
    print(splited_array.shape)
    splited_array = splited_array.reshape(16, 256)  # Invert the dimensions
    img = Image.fromarray(splited_array)
    return img
    
def split_image_columns(image): 
    list_1, list_2, list_3, list_4 = [[] for _ in range(4)]
    np_image = np.array(image)
    for index in range(np_image.shape[1]):  # iterate over columns
        if index % 4 == 0:
            list_1.append(np_image[:, index]) # selects all rows for the given column index
        if index % 4 == 1:
            list_2.append(np_image[:, index])
        if index % 4 == 2:
            list_3.append(np_image[:, index])
        if index % 4 == 3:
            list_4.append(np_image[:, index])

    img_1 = split_aux(np.transpose(list_1))  # The np.transpose function is used to transpose the list of columns into a list of rows.
    img_2 = split_aux(np.transpose(list_2))
    img_3 = split_aux(np.transpose(list_3))
    img_4 = split_aux(np.transpose(list_4))

    return img_1, img_2, img_3, img_4

source_folder = '/mnt/d/Dev/Projects/Lume/super_resolution/datasets/input/splited_images/01/_LR'
target_folder = '/mnt/d/Dev/Projects/Lume/super_resolution/datasets/input/splited_images/01/LR'
images = {}

if not os.path.exists(target_folder):
    os.makedirs(target_folder)

for imgFile in os.listdir(source_folder):
    imgPath = os.path.join(source_folder, imgFile)
    print(f"{imgPath}")

    for index in range(1, 6):
            # loading the images and performing the split
            img = Image.open(imgPath)
            images["1"], images["2"], images["3"], images["4"] = split_image_columns(img)
            images["1"].save(os.path.join(target_folder, imgFile))