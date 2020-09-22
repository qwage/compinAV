import cv2 as cv
import sys
import numpy as np
from matplotlib import pyplot as plt

# Image Reading and Display

img = cv.imread(cv.samples.findFile("Night.jpg"))
img = cv.resize(img,dsize=(int(1920*.8),int(1080*.8)))

if img is None:
    sys.exit("Could not read the image.")
cv.imshow("Display window", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("Night.png", img)

# Image 2D Convolution
'''
img = cv.imread('X31.jpg')
kernel = np.ones((5,5),np.float32)/25
dst = cv.filter2D(img,-1,kernel)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()
'''

# Bluring an Image
'''
img = cv.imread('Night.jpg')
blur = cv.blur(img,(5,5))
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
'''