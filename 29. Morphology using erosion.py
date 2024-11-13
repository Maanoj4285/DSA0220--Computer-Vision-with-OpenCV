import cv2
import numpy as np

image = cv2.imread('data1.jpg', cv2.IMREAD_GRAYSCALE)

_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

kernel = np.ones((5, 5), np.uint8)

eroded_image = cv2.erode(binary_image, kernel, iterations=1)

cv2.imshow("Binary image",binary_image)
cv2.imshow("Eroded image",eroded_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
