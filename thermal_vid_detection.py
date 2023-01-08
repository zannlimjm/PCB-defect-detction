# import the necessary packages
from email.mime import image
from imutils import contours
from skimage import measure
import numpy as np
import argparse
import imutils
import cv2
import os

# from pathlib import Path

# script_path = Path( __file__ ).absolute()

# print( script_path )

# construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
# 	help="path to the image file")
# args = vars(ap.parse_args())
# os.chdir('/Users/zannlim/Desktop/PCB_CV/')


# The function cv2.imread() is used to read an image.
# img = cv2.imread('/Users/zannlim/Desktop/PCB_CV/thermal_test.jpg')
cap = cv2.VideoCapture('/Users/zannlim/Desktop/PCB_CV/actl_thermal.mp4')
while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (11, 11), 0)
    thresh = cv2.threshold(blurred, 175, 255, cv2.THRESH_BINARY)[1] #175 value can change, it picks up the range of value u want
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=4)
    labels = measure.label(thresh, 8, 0)
    mask = np.zeros(thresh.shape, dtype="uint8")
    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = contours.sort_contours(cnts)[0]
    cv2.drawContours(frame, cnts, -1, (0, 255, 0), 3)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, 
            'oh no! hot spot detected!!', 
            (200, 200), 
            font, 2, 
            (0, 255, 255), 
            4, 
            cv2.LINE_4)    
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
# # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# blurred = cv2.GaussianBlur(gray, (11, 11), 0)

# # threshold the image to reveal light regions in the
# # blurred image
# thresh = cv2.threshold(blurred, 175, 255, cv2.THRESH_BINARY)[1] #175 value can change, it picks up the range of value u want
# thresh = cv2.erode(thresh, None, iterations=2)
# thresh = cv2.dilate(thresh, None, iterations=4)

# # contours, hierarchy  = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# # cv2.drawContours(img, contours, -1, (0,255,75), 2)


# # perform a connected component analysis on the thresholded
# # image, then initialize a mask to store only the "large"
# # components
# labels = measure.label(thresh, 8, 0)
# mask = np.zeros(thresh.shape, dtype="uint8")
# # # loop over the unique components
# # for label in np.unique(labels):
# # 	# if this is the background label, ignore it
# # 	if label == 0:
# # 		continue
# # 	# otherwise, construct the label mask and count the
# # 	# number of pixels 
# # 	labelMask = np.zeros(thresh.shape, dtype="uint8")
# # 	labelMask[labels == label] = 255
# # 	numPixels = cv2.countNonZero(labelMask)
# # 	# if the number of pixels in the component is sufficiently
# # 	# large, then add it to our mask of "large blobs"
# # 	if numPixels > 10:
# # 		mask = cv2.add(mask, labelMask)

# # find the contours in the mask, then sort them from left to
# # right
# # cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
# # 	cv2.CHAIN_APPROX_SIMPLE)
# cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cnts = imutils.grab_contours(cnts)
# cnts = contours.sort_contours(cnts)[0]
# # loop over the contours
# # for (i, c) in enumerate(cnts):
# # 	# draw the bright spot on the image
# # 	(x, y, w, h) = cv2.boundingRect(c)
# # 	((cX, cY), radius) = cv2.minEnclosingCircle(c)
# # 	cv2.circle(img, (int(cX), int(cY)), int(radius),
# # 		(0, 0, 255), 3)
# # 	cv2.putText(img, "#{}".format(i + 1), (x, y - 15),
# # 		cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

# cv2.drawContours(img, cnts, -1, (0, 255, 0), 3)


# # The function cv2.imshow() is used to display an image in a window.
# cv2.imshow('graycsale image',img)

# # waitKey() waits for a key press to close the window and 0 specifies indefinite loop
# cv2.waitKey(0)

# # cv2.destroyAllWindows() simply destroys all the windows we created.
# cv2.destroyAllWindows()

# # The function cv2.imwrite() is used to write an image.
# cv2.imwrite('grayscale.jpg', img)