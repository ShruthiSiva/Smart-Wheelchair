import cv2
import numpy as np


def case1_adaptive(name):
	image=cv2.imread('{}'.format(name))
	image=cv2.resize(image,(int(0.2*image.shape[0]), int(0.2*image.shape[1])))
	blurred=cv2.pyrMeanShiftFiltering(image, 31, 91)

	gray=cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
	gauss_threshold=cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
	#_, binary_threshold= cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
	area_temp=0
	_, contours, _ = cv2.findContours(gauss_threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
	for cnt in contours:
		approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
		if len(approx)==4:
				
			area=cv2.contourArea(cnt)
			if area>area_temp:
				area_temp=area

				x,y,w,h = cv2.boundingRect(cnt)	
				image=cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

	return image, area_temp, gauss_threshold

def case2_binary(name):
	image=cv2.imread('{}'.format(name))
	image=cv2.resize(image,(int(0.2*image.shape[0]), int(0.2*image.shape[1])))
	
	blurred=cv2.pyrMeanShiftFiltering(image, 31, 91)
	gray=cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
	
	#gauss_threshold=cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
	_, binary_threshold= cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
	
	area_temp=0
	_, contours, _ = cv2.findContours(binary_threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
	for cnt in contours:
		approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
		if len(approx)==4:
				
			area=cv2.contourArea(cnt)
			if area>area_temp:
				area_temp=area

				x,y,w,h = cv2.boundingRect(cnt)	
				image=cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

	return image, area_temp, binary_threshold


image, area_temp, threshold=case1_adaptive('Images/test1.jpg')

cv2.imshow('Display', image)
cv2.waitKey(0)
cv2.destroyAllWindows()