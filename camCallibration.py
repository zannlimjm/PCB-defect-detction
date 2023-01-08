# import cv2
# import numpy as np

# img = cv2.imread('/Users/zannlim/Desktop/PCB_CV/thermal_cam2.png')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# cv2.imshow("Detected Circle", gray)
# cv2.waitKey(0)

import cv2
import numpy as np
import os
import glob
 
# Defining the dimensions of checkerboard
CHECKERBOARD = (8,12)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
 
# Creating vector to store vectors of 3D points for each checkerboard image
objpoints = []
# Creating vector to store vectors of 2D points for each checkerboard image
imgpoints = [] 
 
 
# Defining the world coordinates for 3D points
objp = np.zeros((1, CHECKERBOARD[0] * CHECKERBOARD[1], 3), np.float32)
objp[0,:,:2] = np.mgrid[0:CHECKERBOARD[0], 0:CHECKERBOARD[1]].T.reshape(-1, 2)
prev_img_shape = None
 
# Extracting path of individual image stored in a given directory
images = glob.glob('/Users/zannlim/Desktop/PCB_CV/Cal_images/IR_cal.jpg')
for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # Find the chess board corners
    # If desired number of corners are found in the image then ret = true
    ret, corners = cv2.findChessboardCorners(gray, CHECKERBOARD, cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_FAST_CHECK + cv2.CALIB_CB_NORMALIZE_IMAGE)
     
    """
    If desired number of corner are detected,
    we refine the pixel coordinates and display 
    them on the images of checker board
    """
    if ret == True:
        objpoints.append(objp)
        # refining pixel coordinates for given 2d points.
        corners2 = cv2.cornerSubPix(gray, corners, (11,11),(-1,-1), criteria)
         
        imgpoints.append(corners2)
 
        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, CHECKERBOARD, corners2, ret)
     
    # cv2.imshow('img',img)
    # cv2.waitKey(0)
 
cv2.destroyAllWindows()
 
h,w = img.shape[:2]
 
"""
Performing camera calibration by 
passing the value of known 3D points (objpoints)
and corresponding pixel coordinates of the 
detected corners (imgpoints)
"""
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
 
print("Camera matrix : \n")
print(mtx)
print()
print("dist : \n")
print(dist)
print()
print("rvecs : \n")
print(rvecs)
print()
print("tvecs : \n")
print(tvecs)
print()
img_out = cv2.imread('/Users/zannlim/Desktop/PCB_CV/IR_actual.jpg')
h,  w = img_out.shape[:2]
print('h', h)
print('w', w)
# Refining the camera matrix using parameters obtained by calibration
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))
x, y, w, h = roi 
# Method 1 to undistort the image
dst = cv2.undistort(img_out, mtx, dist, None, newcameramtx)
 
# Method 2 to undistort the image
# mapx,mapy=cv2.initUndistortRectifyMap(mtx,dist,None,newcameramtx,(w,h),5)
 
# dst = cv2.remap(img_out,mapx,mapy,cv2.INTER_LINEAR)
# dst = dst[y:y+h, x:x+w]
# Displaying the undistorted image
cv2.imshow("undistorted image",dst)
cv2.waitKey(0)