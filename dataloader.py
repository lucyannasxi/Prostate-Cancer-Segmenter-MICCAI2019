
import os

import imageio
import numpy as np
import torch
from torch.utils.data import Dataset
import pickle
from utils import make_dirs


class Gleason2019(Dataset):
    """
    Code for reading Gleason 2019 MICCAI Challenge
    """

    def __init__(self, mode, image_paths, label_paths, split=(0.8, 0.2), crop_dim=(512, 512), samples=100):
        """
        :param mode: 'train','val'
        :param image_paths: image dataset paths