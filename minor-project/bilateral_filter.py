import numpy as np
import cv2
from skimage.metrics import mean_squared_error, peak_signal_noise_ratio, structural_similarity
import matplotlib.pyplot as plt

# Path to your image
path = r'C:\\Users\\susmi\\OneDrive\\Documents\\project\\girl.png'

# Read the original image
image = cv2.imread(path)

# Convert the image to grayscale
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Bilateral Filter to remove noise
denoised_image_bilateral = cv2.bilateralFilter(
    grayscale_image, d=9, sigmaColor=75, sigmaSpace=75)

# Display the original and denoised images
cv2.imshow("Original Grayscale Image", grayscale_image)
cv2.imshow("Denoised Image (Bilateral Filter)", denoised_image_bilateral)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()

# Evaluate the denoising performance (MSE, PSNR, SSIM)
mse_value = mean_squared_error(grayscale_image, denoised_image_bilateral)
psnr_value = peak_signal_noise_ratio(
    grayscale_image, denoised_image_bilateral, data_range=255)
ssim_value, _ = structural_similarity(
    grayscale_image, denoised_image_bilateral, full=True)

# Print results
print(f"Mean Squared Error (MSE): {mse_value}")
print(f"Peak Signal-to-Noise Ratio (PSNR): {psnr_value} dB")
print(f"Structural Similarity Index Measure (SSIM): {ssim_value}")
