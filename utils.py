
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