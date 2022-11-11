import os
import yaml
from tqdm import tqdm
import numpy as np
import re


def walkdir(folder):
    """
    Walk through all the files in a directory and its subfolders.

    Parameters
    ----------
    folder : str
        Path to the folder you want to walk.

    Returns
    -------
        For each file found, yields a tuple having the path to the file
        and the file name.
    """
    for dirpath, _, files in os.walk(folder):
        for filename in files:
            yield (dirpath, filename)


def listfiles(folder):
    """
    get the list of files inlcuded in the dataset
    """
    train_list = []
    class_list = []
    for dirpath, filename in tqdm(walkdir(folder)):
        # files_to_process = os.path.join(dirpath, filename)
        type_of_img = re.split("_", filename)
        print(type_of_img[0])
        if type_of_img[0] == "train":
            train_list
        # img = keras.utils.load_img(files_to_process, target_size=input_size)
        # img_array = keras.preprocessing.image.img_to_array(img)
        # img_array = np.expand_dims(img_array, axis=0)
        # prediction = model.predict(img_array)
        # predicted_class = class_names[np.argmax(prediction)]
    #     pred_list.append(predicted_class)
    #     _, true_label = os.path.split(dirpath)
    #     class_list.append(true_label)
    # predictions = pred_list
    # labels = class_list

    # return predictions, labels
