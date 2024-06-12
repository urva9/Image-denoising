# LOW LIGHT IMAGE DENOISING 

![3EBB3317-A3DA-4C27-AE47-290FFD36FC8D_1_201_a](https://github.com/urva9/LLID/assets/159683192/79e096b5-e444-41e2-bb51-5427a3d7c2e8)


Introduction :-

A novel deep neural network that jointly performs noise reduction on low-light images and enhances illumination and texture details. The architecture is divided into two stages: the image enhancement stage and the refinement stage.

Image Enhancement Stage:

Latent Subspace Denoising Block (LSDB): Uses a low-rank representation of low-light features to suppress noise and predict a noise-free grayscale image. This block is based on Convolutional Neural Networks (CNNs).
Color Space Conversion: Enhances an RGB image by eliminating noise. This is done by converting the image into YCbCr color space and replacing the noisy luminance (Y) channel with the predicted noise-free grayscale image.
Atmospheric Model Prediction: Predicts the transmission map and atmospheric light in this stage, producing an enhanced image with rich color and illumination. The prediction utilizes a U-Net architecture for better feature extraction and image reconstruction.

Refinement Stage:

Spatial Feature Transform (SFT) Layer: Incorporates texture information from the grayscale image into the improved image. This layer integrates the texture details using a mechanism similar to GANs (Generative Adversarial Networks) to refine the final output.

Example of image in these conditions :- Low light, denoised and enhanced, ground truth image

![WhatsApp Image 2024-06-12 at 11 36 04 AM](https://github.com/urva9/LLID/assets/159683192/493cd828-e52b-493a-9987-ff3c00ff9c9a)



Conda Environment Configuration

Create a conda environment with dependencies

 ```
conda env create -f environment.yml
conda activate LLID 
```
Training :-

To train model, Run following command from /src directory.
```
python train.py -opt cfs/lolv1.yaml
```
All the trained checkpoints will be saved in checkpoints directory.

All the logs and tensorboard events will be saved in logs directory.

Inference :-

To test model, Run following command from /src directory.
```
python test.py -opt cfs/lolv1.yaml
```
Above command will predict the test images and print PSNR, SSIM, MAE and LPIPS score.


