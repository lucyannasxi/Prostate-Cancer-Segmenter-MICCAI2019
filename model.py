import pytorch_lightning as pl
import torch
import torch.nn as nn
import torch.nn.functional as F

from utils import DiceLoss


# 2D-Unet Model is adapted from https://github.com/milesial/Pytorch-UNet/blob/master/unet/unet_model.py
class DoubleConv(nn.Module):
    '''(conv => BN => ReLU) * 2'''

    def __init__(self, in_ch, out_ch):
        super(DoubleConv, self).__init__(