import cv2
import numpy as np
import matplotlib.pyplot as plt

# Path to the image
path = r'C:\\Users\\susmi\\OneDrive\\Documents\\project\\girl.png'

# Read the original image
original_color_image = cv2.imread(path, cv2.IMREAD_COLOR)

# Convert the color image to grayscale
grayscale_image = cv2.cvtColor(original_color_image, cv2.COLOR_BGR2GRAY)

# Function to add salt-and-pepper noise to a grayscale image


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
salt_prob = 0.02
pepper_prob = 0.02
noisy_image = add_salt_pepper_noise(grayscale_image, salt_prob, pepper_prob)

# Function to plot histogram


def plot_histogram(image, title):
    plt.figure(figsize=(6, 4))
    plt.hist(image.ravel(), bins=256, range=[0, 256], color='black', alpha=0.7)
    plt.title(title)
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3)
    plt.show()


# Plot histograms
plot_histogram(grayscale_image, "Original Grayscale Image Histogram")
plot_histogram(noisy_image, "Noisy Image Histogram")

# Denoise the image using a median filter
denoised_image = cv2.medianBlur(noisy_image, 3)

# Plot histogram of the denoised image
plot_histogram(denoised_image, "Denoised Image Histogram")

# Function to restore grayscale denoised image to color


def restore_to_color(original_color, denoised_gray):
    denoised_gray_resized = cv2.resize(
        denoised_gray, (original_color.shape[1], original_color.shape[0]))
    b, g, r = cv2.split(original_color)
    restored_color = cv2.merge((denoised_gray_resized, g, r))
    return restored_color


# Restore the denoised grayscale to color
restored_color_image = restore_to_color(original_color_image, denoised_image)

# Display all images
cv2.imshow("Original Color Image", original_color_image)
cv2.imshow("Noisy Grayscale Image", noisy_image)
cv2.imshow("Denoised Grayscale Image", denoised_image)
cv2.imshow("Restored Color Image", restored_color_image)

# Metrics Calculation (Optional)


def calculate_metrics(original, processed):
    mse = np.mean((original - processed) ** 2)
    psnr = 10 * np.log10(255 ** 2 / mse) if mse > 0 else float('inf')
    return mse, psnr


# Calculate MSE and PSNR for grayscale comparison
mse, psnr = calculate_metrics(grayscale_image, denoised_image)
print(f"MSE: {mse:.2f}, PSNR: {psnr:.2f} dB")

cv2.waitKey(0)
cv2.destroyAllWindows()
