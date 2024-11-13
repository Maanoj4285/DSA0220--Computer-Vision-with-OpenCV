import cv2
import numpy as np

image = cv2.imread('data1.jpg', 0) 

kernel = np.ones((15, 15), np.uint8)

top_hat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)

cv2.imshow("Top Hat Image",top_hat)

cv2.waitKey(0)
cv2.destroyAllWindows()
