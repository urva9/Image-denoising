# LOW LIGHT IMAGE DENOISING 

![WhatsApp Image 2024-06-16 at 8 36 39 PM](https://github.com/urva9/LLID-2/assets/159683192/be6384f7-53fd-41b9-9344-46518b8fcd32)



Introduction :-

A novel deep neural network that jointly performs noise reduction on low-light images and enhances illumination and texture details. The architecture is divided into two stages: the image enhancement stage and the refinement stage.

Image Enhancement Stage:

Latent Subspace Denoising Block (LSDB): Uses a low-rank representation of low-light features to suppress noise and predict a noise-free grayscale image. This block is based on Convolutional Neural Networks (CNNs).
Color Space Conversion: Enhances an RGB image by eliminating noise. This is done by converting the image into YCbCr color space and replacing the noisy luminance (Y) channel with the predicted noise-free grayscale image.
Atmospheric Model Prediction: Predicts the transmission map and atmospheric light in this stage, producing an enhanced image with rich color and illumination. The prediction utilizes a U-Net architecture for better feature extraction and image reconstruction.

Refinement Stage:

Spatial Feature Transform (SFT) Layer: Incorporates texture information from the grayscale image into the improved image. This layer integrates the texture details using a mechanism similar to GANs (Generative Adversarial Networks) to refine the final output.

![WhatsApp Image 2024-06-16 at 8 27 09 PM](https://github.com/urva9/LLID-2/assets/159683192/b34b9ee6-c62d-4b68-bcd3-9bad5339070f)



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
