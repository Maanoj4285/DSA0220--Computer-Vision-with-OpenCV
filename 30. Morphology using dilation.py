import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("data1.jpg", 0)

_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

kernel = np.ones((5, 5), np.uint8)

dilated_image = cv2.dilate(binary_image, kernel, iterations=1)

cv2.imshow("Original Image",image)
cv2.imshow("Binary Image",binary_image)
cv2.imshow("Dilated image",dilated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
