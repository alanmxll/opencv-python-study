import cv2 as cv
import numpy as np

img = cv.imread('sudoku.png', 0)
_, th_one = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
th_two = cv.adaptiveThreshold(
    img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
th_three = cv.adaptiveThreshold(
    img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

cv.imshow('Image', img)
cv.imshow('th_one', th_one)
cv.imshow('th_two', th_two)
cv.imshow('th_three', th_three)

cv.waitKey(0)
cv.destroyAllWindows()
