import cv2
import numpy as np

im = cv2.imread('6632749D-F045-4866-89A2-88EDF54477E5.jpeg')
print(im.shape)
# (225, 400, 3)

print(im.dtype)
# uint8
im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
print(im_gray.shape)
# (225, 400)

print(im_gray.dtype)
# uint8

cv2.imwrite('opencv_gray_cvtcolr.jpg', im_gray)