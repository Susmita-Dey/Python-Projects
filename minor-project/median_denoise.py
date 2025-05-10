import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import median_filter
from skimage.metrics import mean_squared_error, peak_signal_noise_ratio, structural_similarity
import cv2

# Path to your image
path = r'C:\\Users\\susmi\\OneDrive\\Documents\\project\\girl.png'

# Read the original image
image = cv2.imread(path)

# Convert the image to grayscale
grayscaleImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert grayscale image to binary
thresholdVal = 127
binaryImage = cv2.threshold(
    grayscaleImage, thresholdVal, 255, cv2.THRESH_BINARY)[1]

# Apply median filter for denoising
denoised_image = median_filter(binaryImage, size=3)

# MSE
mse_value = mean_squared_error(grayscaleImage, denoised_image)

# PSNR
psnr_value = peak_signal_noise_ratio(
    grayscaleImage, denoised_image, data_range=255)

# SSIM
ssim_value, _ = structural_similarity(
    grayscaleImage, denoised_image, full=True)

# Print results
print(f"Mean Squared Error (MSE): {mse_value}")
print(f"Peak Signal-to-Noise Ratio (PSNR): {psnr_value} dB")
print(f"Structural Similarity Index Measure (SSIM): {ssim_value}")

# Histogram using adjusted bar width
plt.figure(figsize=(12, 6))

# Histogram before denoising
plt.subplot(1, 2, 1)
plt.gca().set_facecolor('#f0f0f0')  # Set background color
plt.hist(binaryImage.ravel(), bins=2, range=(0, 256),
         color='blue', rwidth=0.8)  # Adjust bar width
plt.title("Histogram Before Denoising")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")

# Histogram after denoising
plt.subplot(1, 2, 2)
plt.gca().set_facecolor('#f0f0f0')  # Set background color
plt.hist(denoised_image.ravel(), bins=2, range=(0, 256),
         color='green', rwidth=0.8)  # Adjust bar width
plt.title("Histogram After Denoising")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()

# Display the images using OpenCV
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", grayscaleImage)
cv2.imshow("Binary Image", binaryImage)
cv2.imshow("Denoised Image", denoised_image)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
