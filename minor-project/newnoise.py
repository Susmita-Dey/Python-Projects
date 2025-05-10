# import pywt
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import median_filter
import cv2

# Path to your image
path = r'C:\\Users\\susmi\\OneDrive\\Documents\\project\\girl.png'

# Read the original image
image = cv2.imread(path)

# Display the binary image
cv2.imshow("Original Image", image)

# Convert the image to grayscale
grayscaleImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the binary image
cv2.imshow("Grayscale Image", grayscaleImage)

# Convert grayscale image to binary
thresholdVal = 127
binaryImage = cv2.threshold(
    grayscaleImage, thresholdVal, 255, cv2.THRESH_BINARY)[1]

# Display the binary image
cv2.imshow("Binary Image", binaryImage)

# # Find connected components
# num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(
#     binaryImage, connectivity=8)

# # Create an output binary image
# denoised_image = np.zeros_like(binaryImage)

# # Filter out small components (e.g., noise)
# for i in range(1, num_labels):  # Skip the background label (0)
#     if stats[i, cv2.CC_STAT_AREA] > 50:  # Keep components larger than 50 pixels
#         denoised_image[labels == i] = 255

# kernel = np.ones((3, 3), np.uint8)

# # Apply opening to remove white noise
# opened_image = cv2.morphologyEx(binaryImage, cv2.MORPH_OPEN, kernel)

# # Apply closing to fill black noise
# denoised_image = cv2.morphologyEx(opened_image, cv2.MORPH_CLOSE, kernel)

denoised_image = median_filter(binaryImage, size=3)

# Display the denoised color image
cv2.imshow("Denoised Image", denoised_image)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
