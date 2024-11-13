import cv2
import numpy as np

image = cv2.imread('data1.jpg', cv2.IMREAD_GRAYSCALE)

laplacian_mask = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])

sharpened_image = cv2.filter2D(image, -1, laplacian_mask)

cv2.imshow("Original Image",image)
cv2.imshow("Sharpened Image",sharpened_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
