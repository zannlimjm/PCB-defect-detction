import cv2
import numpy as np
image = cv2.imread('/Users/zannlim/Desktop/PCB_CV/thermal_actual.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower = np.array([0, 50, 255], dtype="uint8")
upper = np.array([70, 250, 255], dtype="uint8")
mask = cv2.inRange(image, lower, upper)

cv2.imshow('mask', mask)
cv2.waitKey()