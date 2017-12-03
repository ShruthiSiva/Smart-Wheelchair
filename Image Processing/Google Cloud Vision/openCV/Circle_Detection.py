import cv2
import numpy as np
import os
from matplotlib import pyplot as plt


img=cv2.imread('Images/Feature.jpg')
image_shape_coordinates=(img.shape[0], img.shape[1])
#img=cv2.resize(img, (int(img.shape[0]*0.2), int(img.shape[1]*0.2)))

#*****************COLOR_THRESHOLD AND BOUNDING RECTANGLE*********************************
area_temp=0
cv2.imshow('img', img)
hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_blue=np.array([80,50,50])
upper_blue=np.array([130,255,255])

mask=cv2.inRange(hsv, lower_blue, upper_blue)

res=cv2.bitwise_and(img, img, mask=mask)
res = cv2.medianBlur(img,5)

res=cv2.Canny(res, 100, 200)

#res=cv2.fastNlMeansDenoising(res, None, 65, 5, 21)

pixelpoints=cv2.findNonZero(res)

x,y,w,h = cv2.boundingRect(pixelpoints)
res=cv2.rectangle(res,(x,y), (x+w, y+h),(255,255,255),2)

Coordinates_to_push=(int(x+w/2), int(y+h/2))
cv2.imshow('res', res)
cv2.imwrite('Feature.jpg', res[y:y+h, x:x+w])
cv2.circle(img,Coordinates_to_push,5,(0,0,255),3)

kernel = np.array([[0,0,0], [0,1,0], [0,0,0]], np.float32)
cv2.waitKey(0)
cv2.destroyAllWindows()
