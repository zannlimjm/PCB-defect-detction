import cv2
import numpy as np

img = cv2.imread('/Users/zannlim/Desktop/PCB_CV/square.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# blurred = cv2.GaussianBlur(gray, (11, 11), 0)
gray_blurred = cv2.blur(gray, (3, 3))

# cv2.imshow("blurred",blurred)
# cv2.waitKey(0)
ROI_number = 0
cnts = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for cnt in cnts:
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    if len(approx)==4:
        print("Red = square")
        cv2.drawContours(img,cnt,0,(0,255,0),1)
# cv2.imshow("cnts", cnt)
cv2.imshow('image', img)
cv2.imshow('Binary',gray)
cv2.waitKey()
# detected_circles = cv2.HoughCircles(gray_blurred, 
#                    cv2.HOUGH_GRADIENT, 8, 1, param1 = 150,
#                param2 = 12, minRadius = 1, maxRadius = 1000)
  
# # Draw circles that are detected.
# if detected_circles is not None:
  
#     # Convert the circle parameters a, b and r to integers.
#     detected_circles = np.uint16(np.around(detected_circles))
#     print(len(detected_circles)) ##CHECK
  
#     for pt in detected_circles[0, :]:
#         a, b, r = pt[0], pt[1], pt[2]
  
#         # Draw the circumference of the circle.
#         cv2.circle(img, (a, b), r, (0, 255, 0), 2)
  
#         # Draw a small circle (of radius 1) to show the center.
#         # cv2.circle(img, (a, b), 1, (0, 0, 255), 3)
#         cv2.imshow("Detected Circle", img)
#         cv2.waitKey(0)