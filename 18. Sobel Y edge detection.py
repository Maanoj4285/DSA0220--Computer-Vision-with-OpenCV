import cv2
import numpy as np

# Load the image in grayscale
img = cv2.imread("data1.jpg")
image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
if image is None:
    print("Error loading image.")
    exit()
# Apply Sobel filter along the Y axis to detect vertical edges
sobel_y = cv2.Sobel(image, cv2.CV_64F, dx=0, dy=1, ksize=3)  # dx=0, dy=1 for Y axis
sobel_y = cv2.convertScaleAbs(sobel_y)  # Convert to 8-bit format
cv2.imshow("Original image ", img)

cv2.imshow("Sobel Y Edge Detection", sobel_y)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
