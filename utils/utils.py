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
    test_list = []
    val_list = []
    for dirpath, filename in tqdm(walkdir(folder)):
        # files_to_process = os.path.join(dirpath, filename)
        type_of_img = re.split("_", filename)
        # print(type_of_img[0])
        if type_of_img[0] == "train":
            train_list.append(filename)
        if type_of_img[0] == "test":
            test_list.append(filename)
        if type_of_img[0] == "val":
            val_list.append(filename)
    print(f"The total amount of TRAIN files are {len(train_list)}")
    print(f"The total amount of VALIDATION files are {len(val_list)}")
    print(f"The total amount of TEST files are {len(test_list)}")

    return train_list, test_list, val_list
