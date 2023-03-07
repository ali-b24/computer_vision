import cv2 as cv
import numpy as np

img1 = cv.imread('PROJECTS/photos/3.jpg', 0)
img = cv.rotate(img1, cv.ROTATE_90_CLOCKWISE)
mask1 = np.repeat(np.tile(np.linspace(1, 0, img.shape[1]), (img.shape[0], 1))[:, :, np.newaxis], 3, axis=2)

cv.imshow('MASK', mask1)
cv.waitKey()