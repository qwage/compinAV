import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# - - - Function Definitions - - - #

def colsp(img, col_space):
    if col_space == 'hsv':
        new_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    elif col_space == 'gray':
        new_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    else:
        new_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    return new_img

# - - - Main - - - #

img = cv.imread("X31.JPG") #Reading in image
img2 = colsp(img, "gray") #Converting to gray scale
img3 = colsp(img, "hsv") #Converting to HSV
img4 = colsp(img, "") #Converting to RGB

kernal_3 = np.ones((3,3)) #Setting up an array of 1s that is 3x3
kernal_5 = np.ones((5,5)) #Setting up an array of 1s that is 5x5

img_D_3 = cv.dilate(img,kernal_3,iterations=1) #Dilation using a 3x3 matrix on original image
img_E_3 = cv.erode(img,kernal_3,iterations=1) #Erosion using a 3x3 matrix on original image
img_D_5 = cv.dilate(img,kernal_5,iterations=1) #Dilation using a 5x5 matrix on original image
img_E_5 = cv.erode(img,kernal_5,iterations=1) #Erosion using a 5x5 matrix on original image
img_D_E_3 = cv.erode(cv.dilate(img,kernal_3,iterations=1),kernal_3,iterations=1) #Erosion followed by dilation using a 3x3 matrix on original image

# - - - Plot All Color Spaces - - - #
plt.figure(1)
plt.subplot(411),plt.imshow(cv.cvtColor(img,cv.COLOR_BGR2RGB)),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(412),plt.imshow(cv.cvtColor(img2,cv.COLOR_BGR2RGB)),plt.title('Gray Scaled')
plt.xticks([]), plt.yticks([])
plt.subplot(413),plt.imshow(cv.cvtColor(img3,cv.COLOR_BGR2RGB)),plt.title('HSV')
plt.xticks([]), plt.yticks([])
plt.subplot(414),plt.imshow(img4),plt.title('RGB')
plt.xticks([]), plt.yticks([])

# - - - Plot All Erosions and Dilations - - - #
plt.figure(2)
plt.subplot(411),plt.imshow(cv.cvtColor(img_D_3,cv.COLOR_BGR2RGB)),plt.title('Dilate 3x3')
plt.xticks([]), plt.yticks([])
plt.subplot(412),plt.imshow(cv.cvtColor(img_D_5,cv.COLOR_BGR2RGB)),plt.title('Dilate 5x5')
plt.xticks([]), plt.yticks([])
plt.subplot(413),plt.imshow(cv.cvtColor(img_E_3,cv.COLOR_BGR2RGB)),plt.title('Erosion 3x3')
plt.xticks([]), plt.yticks([])
plt.subplot(414),plt.imshow(cv.cvtColor(img_E_5,cv.COLOR_BGR2RGB)),plt.title('Erosion 5x5')
plt.xticks([]), plt.yticks([])

# - - - Plot Erosion and Dilation - - - #
plt.figure(3)
plt.imshow(cv.cvtColor(img_D_E_3,cv.COLOR_BGR2RGB)),plt.title('Dilation and Then Erosion')
plt.xticks([]),plt.yticks([])

plt.show() #Show Images
