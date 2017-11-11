import cv2
import numpy as np

#I intend to threshold a low light image
#1--> white(255), 0--> black. Above 12, it is set to 1. Low light image has 
img=cv2.imread('Images/query1.jpg')
print(img.shape)
img=cv2.resize(img,(int(0.2*img.shape[0]), int(0.2*img.shape[1])))
retvalue, threshold= cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)

grayscaled=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retvalue2, threshold2= cv2.threshold(grayscaled, 120, 255, cv2.THRESH_BINARY)
gauss=cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115,1)
cv2.imshow('threshold', threshold)
cv2.imshow('threshold2', threshold2)
cv2.imshow('Gauss', gauss)
cv2.waitKey(0)
cv2.destroyAllWindows()