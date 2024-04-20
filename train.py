
"""AI Summer pathology MICCAI competition 2019"""
import glob
import os

from pytorch_lightning import Trainer
from torch.utils.data import DataLoader

from dataloader import Gleason2019SaveDISK
from model import Unet
from utils import shuffle_lists

# Data preparation
generate_sub_images = True
root_path = './MICCAI_2019_pathology_challenge/'
folder_to_save_train_samples = './train_samples'
folder_to_save_val_samples = './val_samples'
train_imgs = sorted(glob.glob(os.path.join(root_path, 'Train Imgs/Train Imgs/*.jpg')))
