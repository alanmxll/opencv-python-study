import cv2
import numpy as np

img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)

img2 = np.full((250, 500, 3), 255, dtype=np.uint8)
img2 = cv2.rectangle(img2, (0, 0), (250, 250), (0, 0, 0), -1)
# img2 = cv2.imread('image_1.png')

# bit_and = cv2.bitwise_and(img2, img1)
# bit_or = cv2.bitwise_or(img2, img1)
# bit_xor = cv2.bitwise_xor(img2, img1)
bit_not_one = cv2.bitwise_not(img1)
bit_not_two = cv2.bitwise_not(img2)


cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
# cv2.imshow('bit_and', bit_and)
# cv2.imshow('bit_or', bit_or)
# cv2.imshow('bit_xor', bit_xor)
cv2.imshow('bit_not_one', bit_not_one)
cv2.imshow('bit_not_two', bit_not_two)

cv2.waitKey(0)
cv2.destroyAllWindows()
