
import glob
import os
import random
import shutil
import time

import imageio
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F


def make_dirs(path):
    if os.path.exists(path):
        shutil.rmtree(path)
        os.mkdir(path)
    else:
        os.makedirs(path)


def read_img(img_path):
    """
    Reads a .png image and returns it as a numpy array.
    """
    return imageio.imread(img_path)


def check_path_in_list(key, list):
    """
    Checks a path if exist in the other list
    """
    # remove file.png from the end of the path
    path_base = list[0].split('/')[0:-1]
    # add desired key-path
    path_base.append(key)
    desired_path = '/'.join(path_base)
    # check if it exists in the list
    if desired_path in list:
        image_numpy = read_img(desired_path)
        return image_numpy
    return None


def get_majority_vote(a):
    """
    Returns the majority vote element of a list
    """
    return max(map(lambda val: (a.count(val), val), set(a)))[1]


def vote(stacked_labels):
    """
    Performs majority voting on the stacked labels
    """
    voters, height, width = stacked_labels.shape
    final_labels = stacked_labels.sum(axis=0)
    for i in range(height):
        for j in range(width):
            votes = stacked_labels[:, i, j]
            value = get_majority_vote(votes.tolist())
            final_labels[i, j] = value
    return final_labels


def preprocess_labels(maps, image_paths, path_to_save_labels):
    """
    Majority labeling vote to produce ground truth labels