import cv2

source_image = cv2.imread('watermark.png')
destination_image = cv2.imread('data1.jpg')
cv2.imshow("Original image 1", source_image)
cv2.imshow("Original image 2", destination_image)

x, y, width, height = 50, 50, 100, 100
cropped_image = source_image[y:y + height, x:x + width]

paste_x, paste_y = 150, 150

dest_h, dest_w = destination_image.shape[:2]
if paste_x + width <= dest_w and paste_y + height <= dest_h:
    destination_image[paste_y:paste_y + height, paste_x:paste_x + width] = cropped_image
else:
    print("Cropped area does not fit within the destination image at the specified location.")

cv2.imshow('cropped image', cropped_image)
cv2.imshow('Copy and pasted Image', destination_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
