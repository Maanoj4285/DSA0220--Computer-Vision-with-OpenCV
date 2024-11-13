import cv2
import numpy as np

image = cv2.imread('data1.jpg', cv2.IMREAD_GRAYSCALE)

blurred_image = cv2.GaussianBlur(image, (9, 9), sigmaX=2)

mask = cv2.subtract(image, blurred_image)

high_boost_image = cv2.addWeighted(image, 1, mask, 1.5, 0)

cv2.imshow("Original Image",image)
cv2.imshow("Sharpened image",high_boost_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
