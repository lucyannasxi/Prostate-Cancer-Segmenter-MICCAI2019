
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