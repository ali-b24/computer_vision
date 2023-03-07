import cv2

img = cv2.imread('PROJECTS/photos/3.jpg', 0)

ROT_img = cv2.rotate(img, cv2.ROTATE_180)

cv2.imshow('NORMAL', img)
cv2.imshow('ROTATED', ROT_img)
cv2.waitKey()
