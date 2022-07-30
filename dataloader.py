
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
        :param label_paths: label dataset paths
        :param crop_dim: 2 element tuple to decide crop values
        :param samples: number of sub-grids to create(patches of the input img)
        """
        self.slices = 244
        self.mode = mode
        self.crop_dim = crop_dim
        self.sample_list = []
        self.samples = samples
        train_idx = int(split[0] * self.slices)
        val_idx = int(split[1] * self.slices)

        if self.mode == 'train':
            self.list_imgs = image_paths[0:train_idx]
            self.list_labels = label_paths[0:train_idx]
            self.generate_samples()
        elif self.mode == 'val':
            self.list_imgs = image_paths[train_idx:(train_idx + val_idx)]
            self.list_labels = label_paths[train_idx:(train_idx + val_idx)]
            self.generate_samples()

    def __len__(self):
        return len(self.sample_list)

    def __getitem__(self, index):
        tuple_in = self.sample_list[index]
        img_tensor, segmentation_map = tuple_in
        return img_tensor, segmentation_map

    def generate_samples(self):
        total = len(self.list_imgs)
        print('Total ' + self.mode + ' data to generate samples:', total)
        for j in range(total):
            for i in range(self.samples):
                input_path = self.list_imgs[j]
                label_path = self.list_labels[j]

                img_numpy = imageio.imread(input_path)
                label_numpy = imageio.imread(label_path)

                img_numpy, label_numpy = self.crop_img(img_numpy, label_numpy)

                img_tensor = torch.from_numpy(img_numpy).float()
                label_tensor = torch.from_numpy(label_numpy).unsqueeze(0)

                img_tensor = img_tensor.permute(2, 0, 1)
                img_tensor = norm_img(img_tensor)
                self.sample_list.append(tuple((img_tensor, label_tensor)))
