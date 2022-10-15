from utils import *

# fill your path from your local folder path here
root_path = './MICCAI_2019_pathology_challenge/'
path_to_save_labels = './labels'
make_dirs(path_to_save_labels)

# Read paths from 6 annotators
maps = read_labels(root_path)
img_paths =