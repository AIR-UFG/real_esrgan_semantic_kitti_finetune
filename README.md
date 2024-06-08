# Real-ESRGAN for Lidar Spherical Projections Images Finetune

This project aim to fine-tune the Real-ESRGAN model to handle low resolution images from lidar's spherical projection. We used Semantic Kitti dataset to finetuning the model.

## Repo Files

This repo contains the following files:

* Real_ESRGAN_architecture_finetune.ipynb. -- This file is used for training in order to define the parameters of the training process, like learning rate and validation frequncy.

* options/finetune_realesrgan_x4plus_architecture.yml -- This file is used for training in order to define the parameters of the training process, like learning rate and validation frequncy.

* realesrgan/train_finetune_architecture.py -- This is used to train new models.

* inference_realesrgan_architecture.py -- This file is used for inference or test trained networks.

* split_images.py -- This file is used to process and split images from 1024x16 to 256x16 dimension, setting the image with the right format for 4x upscaling.

* weigths/net_g_latest.pth -- The weigth provided from the finetune of real-esrgan with semantic kitti dataset

## Running The Code

To train the model in this git repo, one must first do these steps:

1. Download the original files from the Real-ESRGAN repo.
2. After downloading the files (Real-ESRGAN-master folder) to <your_dir>, add the files from this fine-tune repo in the Real-ESRGAN base folder in the exact folders they are in both reposetories i.e:
For all purposes
    * Real_ESRGAN_architecture_finetune.ipynb in the <your_dir>/Real-ESRGAN-master folder.
For training
    * finetune_realesrgan_x4plus_architecture.yml in the <your_dir>/Real-ESRGAN-master/options folder.
    * train_finetune_architecture.py in the <your_dir>/Real-ESRGAN-master/realesrgan folder.
For inference existing models
    * put the pre-trained models (.pth files) in the <your_dir>/Real-ESRGAN-master/weights folder. You can take our pre-trained model from here.

Open the Real_ESRGAN_architecture_finetune.ipynb file and from then you can run the code, needed explnations are in the notebook.