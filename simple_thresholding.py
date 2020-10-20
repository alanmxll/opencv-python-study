import cv2 as cv
import numbers as np

img = cv.imread('gradient.png', 0)
_, th_one = cv.threshold(img, 50, 255, cv.THRESH_BINARY)
_, th_two = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV)
_, th_three = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
_, th_four = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
_, th_five = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)


cv.imshow('Image', img)
cv.imshow('th_one', th_one)
cv.imshow('th_two', th_two)
cv.imshow('th_three', th_three)
cv.imshow('th_four', th_four)
cv.imshow('th_five', th_five)

cv.waitKey(0)
cv.destroyAllWindows()
