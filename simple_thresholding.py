import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('gradient.png', 0)
_, th_one = cv.threshold(img, 50, 255, cv.THRESH_BINARY)
_, th_two = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV)
_, th_three = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
_, th_four = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
_, th_five = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)


titles = ['Original Image', 'BINARY',
          'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, th_one, th_two, th_three, th_four, th_five]

for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[í])
    plt.xticks([]), plt.yticks([])
# cv.imshow('Image', img)
# cv.imshow('th_one', th_one)
# cv.imshow('th_two', th_two)
# cv.imshow('th_three', th_three)
# cv.imshow('th_four', th_four)
# cv.imshow('th_five', th_five)

plt.show()

# cv.waitKey(0)
# cv.destroyAllWindows()
