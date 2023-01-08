
# Import Required libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

model = 'Model/super_resolution.onnx'
net = cv2.dnn.readNetFromONNX(model)

img = cv2.imread('/Users/zannlim/Desktop/PCB_CV/marker_test.jpg')

# Create a Copy of Image for preprocessing.
img_copy = img.copy()
 
# Resize the image into Required Size
img_copy = cv2.resize(img_copy, (224,224), cv2.INTER_CUBIC)
 
# Convert image into YcbCr
image_YCbCr = cv2.cvtColor(img_copy, cv2.COLOR_BGR2YCrCb)
 
# Split Y,Cb, and Cr channel 
image_Y, image_Cb, image_Cr = cv2.split(image_YCbCr)
 
# Covert Y channel into a numpy arrary
img_ndarray = np.asarray(image_Y)
 
# Reshape the image to (1,1,224,224) 
reshaped_image = img_ndarray.reshape(1,1,224,224)
 
# Convert to float32 and as a normalization step divide the image by 255.0
blob = reshaped_image.astype(np.float32) / 255.0