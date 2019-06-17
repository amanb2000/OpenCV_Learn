import cv2
import numpy as np

img = cv2.imread('assets/aman_copy.png', 1)

img = cv2.line(img, (0, 0), (255, 255), (255, 0, 0), 1) # image, start, end, color(BGR), thickness

img = cv2.rectangle(img, (10, 10), (400, 500), (255, 255, 255), 1)

font = cv2.FONT_HERSHEY_SIMPLEX

img = cv2.putText(img, 'hello world', (10, 500), font, 1, (255, 255, 255), 1, cv2.LINE_AA) # image, position, font, size, color, thickness, line type

cv2.imshow('hey', img)

cv2.waitKey(0)