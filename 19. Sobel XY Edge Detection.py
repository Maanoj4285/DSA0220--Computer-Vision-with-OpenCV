import cv2
import numpy as np

image = cv2.imread("data1.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Error loading image.")
    exit()

sobel_x = cv2.Sobel(image, cv2.CV_64F, dx=1, dy=0, ksize=3)
sobel_x = cv2.convertScaleAbs(sobel_x)

sobel_y = cv2.Sobel(image, cv2.CV_64F, dx=0, dy=1, ksize=3)
sobel_y = cv2.convertScaleAbs(sobel_y)

sobel_xy = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

cv2.imshow("Original Image", image)
cv2.imshow("Sobel X Edge Detection", sobel_x)
cv2.imshow("Sobel Y Edge Detection", sobel_y)
cv2.imshow("Sobel XY Edge Detection", sobel_xy)

cv2.waitKey(0)
cv2.destroyAllWindows()
