import cv2
import numpy as np
import matplotlib.pyplot as plt

# Path to your image
path = r'C:\\Users\\susmi\\OneDrive\\Documents\\project\\girl.png'

# Read the original image in color
original_color_image = cv2.imread(path, cv2.IMREAD_COLOR)

# Convert the color image to grayscale
grayscale_image = cv2.cvtColor(original_color_image, cv2.COLOR_BGR2GRAY)

# Convert grayscale image to binary
_, binary_image = cv2.threshold(grayscale_image, 127, 255, cv2.THRESH_BINARY)

# Display the binary image
cv2.imshow("Binary Image", binary_image)

# Function to add salt-and-pepper noise


def add_salt_pepper_noise(image, salt_prob, pepper_prob):
    noisy_image = np.copy(image)
    total_pixels = image.size

    # Adding Salt noise
    num_salt = int(total_pixels * salt_prob)
    salt_coords = [np.random.randint(0, i - 1, num_salt) for i in image.shape]
    noisy_image[salt_coords[0], salt_coords[1]] = 255

    # Adding Pepper noise
    num_pepper = int(total_pixels * pepper_prob)
    pepper_coords = [np.random.randint(
        0, i - 1, num_pepper) for i in image.shape]
    noisy_image[pepper_coords[0], pepper_coords[1]] = 0

    return noisy_image


# Add salt-and-pepper noise
salt_prob = 0.02  # Probability of salt noise
pepper_prob = 0.02  # Probability of pepper noise
noisy_image = add_salt_pepper_noise(binary_image, salt_prob, pepper_prob)

# Display the noisy image
cv2.imshow("Noisy Image", noisy_image)

# Function to plot histogram


def plot_histogram(image, title):
    plt.figure(figsize=(6, 4))
    # Flatten the image to 1D array
    pixel_values = image.ravel()
    # Plot the histogram
    plt.hist(pixel_values, bins=256, range=[0, 256], color='black', alpha=0.7)
    plt.title(title)
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3)  # Add a light grid for better visibility
    plt.show()


# Plot histograms
plot_histogram(binary_image, "Original Binary Image Histogram")
plot_histogram(noisy_image, "Noisy Image Histogram")

# Denoising using a median filter
denoised_image = cv2.medianBlur(noisy_image, 3)

# Display the denoised image
cv2.imshow("Denoised Image (Grayscale)", denoised_image)

# Plot histogram of denoised image
plot_histogram(denoised_image, "Denoised Image Histogram")

# Function to restore the denoised grayscale image to the original color image


def restore_to_color(original_color, denoised_gray):
    # Ensure denoised image is the same size as the original
    denoised_gray_resized = cv2.resize(
        denoised_gray, (original_color.shape[1], original_color.shape[0]))

    # Split the original color image into channels
    b, g, r = cv2.split(original_color)

    # Replace the blue channel with the denoised grayscale image
    restored_color = cv2.merge((denoised_gray_resized, g, r))

    return restored_color


# Restore the denoised grayscale to color
restored_color_image = restore_to_color(original_color_image, denoised_image)

# Display the restored color image
cv2.imshow("Restored Color Image", restored_color_image)

# Function to calculate MSE and PSNR


def calculate_metrics(original, processed):
    mse = np.mean((original - processed) ** 2)
    psnr = 10 * np.log10(255 ** 2 / mse) if mse > 0 else float('inf')
    return mse, psnr


# Calculate metrics
mse, psnr = calculate_metrics(grayscale_image, denoised_image)
print(f"MSE: {mse:.2f}, PSNR: {psnr:.2f} dB")

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
