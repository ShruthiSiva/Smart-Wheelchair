import numpy as np
import cv2

img = cv2.imread('test5.jpg',0)
img=cv2.resize(img,None,fx=0.1, fy=0.1, interpolation = cv2.INTER_CUBIC)
kernel = np.ones((5,5),np.uint8)
img = cv2.erode(img,kernel,iterations = 1)
#img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
#img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)


ret,thresh = cv2.threshold(img,127,255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#cnt = contours[4]
#img = cv2.drawContours(img, [cnt], 0, (0,255,0), 3)
img = cv2.drawContours(img, contours, -1, (0,255,0), 3)
for cnt in contours:
	approx=cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
	if len(approx)==4:
		x,y,w,h=cv2.boundingRect(cnt)
		img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

	
		

#cv2.drawContours(img, contours, -1, (0,255,0), 3)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
