
"""AI Summer pathology MICCAI competition 2019"""
import glob
import os

from pytorch_lightning import Trainer
from torch.utils.data import DataLoader

from dataloader import Gleason2019SaveDISK
from model import Unet