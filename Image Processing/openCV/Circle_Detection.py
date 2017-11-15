import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

img=cv2.imread('../Images/Feature.jpg')
#Resizing the image to make it easier for analysis on laptops. It will be removed for the raspberry pi.
img=cv2.resize(img, (int(img.shape[0]*0.2), int(img.shape[1]*0.2)))

# Converting the image to HSV color Space for color analysis
hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# Min B: 100 Max B: 255
# Min R: 0   Max R: 50
# Min G: 0   Max G: 50
lower_blue=np.array([0,0,100])
upper_blue=np.array([50,50,255])

lower_blue1=np.array([80,50,50])
upper_blue2=np.array([130,255,255])

mask=cv2.inRange(hsv, lower_blue, upper_blue)
mask2=cv2.inRange(img,lower_blue1,upper_blue2)
res=cv2.bitwise_and(img,img, mask=mask)
res1=cv2.bitwise_and(img,img,mask=mask2)
cv2.imshow('Masked Image',res)
cv2.imshow('Mask - Original',res1)
res=cv2.Canny(res, 100, 200)

#res=cv2.fastNlMeansDenoising(res, None, 65, 5, 21)
cv2.imshow('res1', res)
pixelpoints=cv2.findNonZero(res)

x,y,w,h = cv2.boundingRect(pixelpoints)
res=cv2.rectangle(res,(x,y), (x+w, y+h),(255,255,255),2)
cv2.imshow('res', res)
cv2.imwrite('Feature.jpg', res[y:y+h, x:x+w])

#*************************COLOR_THRESHOLD***********************

cv2.imshow('opening', res)

####### RECTANGLE DETECTION ########################################

# blur=cv2.medianBlur(img, 5)
# edge=cv2.Canny(blur, 100, 200)

# area_temp=0

# _, contours, _ = cv2.findContours(edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
# for cnt in contours:
#   approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
#   if len(approx)==4:

#     area=cv2.contourArea(cnt)
#     if area>area_temp:
#       area_temp=area

#       x,y,w,h = cv2.boundingRect(cnt)
# img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

# cv2.imshow('img', img)

# roi=img[y:y+h, x:x+w]
# roi=cv2.Canny(roi, 100, 200)
# cv2.imshow('roi', img)
####### RECTANGLE DETECTION #####################################################



cv2.waitKey(0)
cv2.destroyAllWindows()
