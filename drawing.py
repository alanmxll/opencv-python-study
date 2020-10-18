import numpy as np
import cv2

# img = cv2.imread('lena.jpg', 0)
img = np.zeros([512, 512, 3], np.uint8)

img = cv2.line(img, (0, 0), (255, 255), (147, 96, 44), 10)  # 44, 96, 147
img = cv2.arrowedLine(img, (0, 255), (255, 255), (255, 0, 0), 10)

img = cv2.circle(img, (447, 63), 63, (0, 255, 0), -1)
img = cv2.rectangle(img, (400, 200), (200, 400), (0, 0, 0), 1)
font = cv2.FONT_HERSHEY_DUPLEX
img = cv2.putText(img, 'JS EH MEU PIRU', (150, 450),
                  font, 1.25, (0, 0, 0), 10, cv2.LINE_AA)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
