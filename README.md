
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

Read annotations and offline processing
This step generates training labels through majority voting for the provided annotations.
Check path names in the `generate_labels.py` script and then run `python generate_labels.py`. It roughly takes 2 hours.

## Baseline Experiment
After checking the paths, run `python train.py`.

This baseline approach includes: Majority label Voting from different domain experts, Random shuffling 80% train 20% val split, 512x512x3 input patches, Unet architecture, Generate 30 samples per train image and 10 per val img, Train with Unet without data augmentation, Multi class dice loss functions will be used.

After the baseline experiment further ideas/practices can be tested:

Split the dataset based on slice number and ID and not randomly!
Apply common data augmentation techniques
Examine input down-sampling option
Use more recent model architectures and compare them to the baseline

## Medical Zoo Pytorch
For medical imaging projects, visit [Medical Zoo Pytorch](https://github.com/black0017/MedicalZooPytorch 'MedZoo').

## Support
If you find this repo useful, consider starring it to help reach a broader audience.