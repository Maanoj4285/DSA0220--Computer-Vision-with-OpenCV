import cv2
import numpy as np

# Load the image in grayscale
img = cv2.imread("data1.jpg")
image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
if image is None:
    print("Error loading image.")
    exit()

# Apply Sobel filter along the X axis to detect horizontal edges
sobel_x = cv2.Sobel(image, cv2.CV_64F, dx=1, dy=0, ksize=3)  # dx=1, dy=0 for X axis
sobel_x = cv2.convertScaleAbs(sobel_x)  # Convert to 8-bit format
cv2.imshow("Original image ", img)
# Display both the Sobel X and Sobel Y edge-detected images
cv2.imshow("Sobel X Edge Detection", sobel_x)
# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
