import numpy as np
import cv2
from scipy.signal import wiener
from skimage.metrics import mean_squared_error, peak_signal_noise_ratio, structural_similarity
import matplotlib.pyplot as plt

# Path to your image
path = r'C:\\Users\\susmi\\OneDrive\\Documents\\project\\girl.png'

# Read the original image
image = cv2.imread(path)

# Convert the image to grayscale
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Wiener Filter to remove noise
denoised_image = wiener(grayscale_image)


# Histogram using adjusted bar width
plt.figure(figsize=(12, 6))

# Histogram before denoising
plt.subplot(1, 2, 1)
plt.gca().set_facecolor('#f0f0f0')  # Set background color
plt.hist(grayscale_image.ravel(), bins=2, range=(0, 256),
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

# Display the original and denoised images
cv2.imshow("Original Grayscale Image", grayscale_image)
cv2.imshow("Denoised Image (Wiener Filter)",
           denoised_image.astype(np.uint8))

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()

# Evaluate the denoising performance (MSE, PSNR, SSIM)
mse_value = mean_squared_error(grayscale_image, denoised_image)
psnr_value = peak_signal_noise_ratio(
    grayscale_image, denoised_image, data_range=255)
ssim_value, _ = structural_similarity(
    grayscale_image, denoised_image, full=True)

# Print results
print(f"Mean Squared Error (MSE): {mse_value}")
print(f"Peak Signal-to-Noise Ratio (PSNR): {psnr_value} dB")
print(f"Structural Similarity Index Measure (SSIM): {ssim_value}")
