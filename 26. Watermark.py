import cv2
import numpy as np

image = cv2.imread('data1.jpg')
watermark = cv2.imread('watermark.png', cv2.IMREAD_UNCHANGED)

scale = 0.3
watermark = cv2.resize(watermark, (0, 0), fx=scale, fy=scale)

(wH, wW) = watermark.shape[:2]
(h, w) = image.shape[:2]

x = w - wW - 10 
y = h - wH - 10 

if watermark.shape[2] == 4:
    watermark_bgr = watermark[:, :, :3]
    alpha_channel = watermark[:, :, 3] / 255.0
else:
    watermark_bgr = watermark
    alpha_channel = np.ones((wH, wW))

for c in range(3):
    image[y:y + wH, x:x + wW, c] = (alpha_channel * watermark_bgr[:, :, c] +
                                    (1 - alpha_channel) * image[y:y + wH, x:x + wW, c])

cv2.imshow("Watermarked image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
