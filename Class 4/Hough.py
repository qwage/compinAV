import cv2
import numpy as np

img = cv2.imread('road.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray,50,200,apertureSize = 3)

minLineLength = 10
maxLineGap = 10

lines = cv2.HoughLinesP(edges,1,np.pi/180,200,minLineLength=minLineLength,maxLineGap=maxLineGap)
for x in range(0, len(lines)):
    for x1,y1,x2,y2 in lines[x]:
        cv2.line(img,(x1,y1),(x2,y2),(255,0,0),2)

cv2.imshow('Edges', cv2.resize(edges,(int(1920*.8),int(.8*1080))))
cv2.imshow('houghlines3.jpg',cv2.resize(img,(int(1920*.8),int(.8*1080))))
cv2.waitKey(0)
