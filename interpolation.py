import cv2
import numpy as np
import matplotlib as plt
from cv2 import dnn_superres

img = cv2.imread('/Users/zannlim/Desktop/PCB_CV/marker_test.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# sr = dnn_superres.DnnSuperResImpl_create()

# path = "/Users/zannlim/EDSR_Tensorflow/models/EDSR_x4.pb"

# sr.readModel(path)

# sr.setModel("edsr",4)

# result = sr.upsample(img)

# Resized image
resized = cv2.resize(img,dsize=None,fx=4,fy=4, interpolation=cv2.INTER_CUBIC)
cv2.imshow("interpolation",resized)
# cv2.imshow("results", result)
cv2.waitKey(0)
# cv2.imshow("img",img)s
# plt.figure(figsize=(12,8))
# plt.subplot(1,3,1)
# # Original image
# plt.imshow(img[:,:,::-1])
# plt.subplot(1,3,2)
# # SR upscaled
# plt.imshow(result[:,:,::-1])
# plt.subplot(1,3,3)
# # OpenCV upscaled
# plt.imshow(resized[:,:,::-1])
# plt.show()

# cv2.imshow("Detected Circle", gray)
