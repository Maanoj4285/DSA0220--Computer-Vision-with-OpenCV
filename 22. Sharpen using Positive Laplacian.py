import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('data1.jpg', cv2.IMREAD_GRAYSCALE)

laplacian_positive_mask = np.array([[0, 1, 0],
                                    [1, -4, 1],
                                    [0, 1, 0]])

edges = cv2.filter2D(image, -1, laplacian_positive_mask)

sharpened_image = cv2.subtract(image, edges)

cv2.imshow("Original Image",image)
cv2.imshow("Sharpened Image",sharpened_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
