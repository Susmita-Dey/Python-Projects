import matplotlib.pyplot as plt
from skimage.metrics import mean_squared_error, peak_signal_noise_ratio, structural_similarity
import cv2

# Path to your image
path = r'C:\\Users\\susmi\\OneDrive\\Documents\\project\\couple-image.jpeg'

# Read the original image
image = cv2.imread(path)

# Convert the image to grayscale
grayscaleImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Total Variation Denoising (using Non-Local Means)
# Parameters: h (filter strength), templateWindowSize (size of patch), searchWindowSize
denoised_image = cv2.fastNlMeansDenoising(
    grayscaleImage, None, h=30, templateWindowSize=7, searchWindowSize=21)

# Histogram using adjusted bar width
plt.figure(figsize=(12, 6))

# Histogram before denoising
plt.subplot(1, 2, 1)
plt.gca().set_facecolor('#f0f0f0')  # Set background color
plt.hist(grayscaleImage.ravel(), bins=2, range=(0, 256),
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
cv2.imshow("Denoised Image", denoised_image)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
