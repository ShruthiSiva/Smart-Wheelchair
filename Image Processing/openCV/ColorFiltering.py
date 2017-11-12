import cv2
import numpy as np 

#cap=cv2.VideoCapture(0)
img=cv2.imread('Images/test1.jpg')
img=cv2.resize(img, (int(img.shape[0]*0.2), int(img.shape[1]*0.2)))
#while True:
#img=img[80: 420, 300: 550]
#cv2.imshow('roi',roi)
#_, frame=cap.read()
hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red=np.array([0,10, 50])
upper_red=np.array([180,80,180])

#dark_red=np.uitn8([[[12,22,121]]])
#dark_red=cv2.cvtColor(dark_red, cv2.COLOR_BGR2HSV)

mask=cv2.inRange(hsv, lower_red, upper_red)

res=cv2.bitwise_and(img, img, mask=mask)

#cv2.imshow('frame', frame)
#cv2.imshow('mask', mask)
cv2.imshow('result', res)

cv2.waitKey(0)
#if k==27:
	#break
cv2.destroyAllWindows()
cap.release()
