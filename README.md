
# Prostate Cancer Segmenter 
This LucentAI project is focused on segmenting high-resolution microscopic prostate cancer images.

A Google colab notebook is also [available](https://colab.research.google.com/drive/1biPE5drh_3TPMraykW2taJ7v7Gx3FuBx?usp=sharing).

The images are 2D but really high resolution ~5Kx5K pixels.

There are multiple annotators that manually segment the images. We map the annotators to images and perform majority voting to generate the labels.

The challenge data used are available [here](https://gleason2019.grand-challenge.org/). Creating an account is necessary to download the data.

## Installation Step
Clone the LucentAI project, create a new virtual environment, and then run `pip install -r requirements.txt`

## The Data
After downloading the data, place them in the project folder.
The folder is named 'MICCAI_2019_pathology_challenge'