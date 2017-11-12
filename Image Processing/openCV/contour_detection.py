import cv2
import numpy as np
import os

img=cv2.imread('Images/query1.jpg')
img=cv2.resize(img, (int(img.shape[0]*0.2), int(img.shape[1]*0.2)))
blur=cv2.medianBlur(img, 5)
edge=cv2.Canny(blur, 100, 200)

cv2.imshow('blur', blur)
cv2.imshow('Edge', edge)
area_temp=0

_, contours, _ = cv2.findContours(edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
for cnt in contours:
  approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
  if len(approx)==4:

    area=cv2.contourArea(cnt)
    if area>area_temp:
      area_temp=area

      x,y,w,h = cv2.boundingRect(cnt)
img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
roi=edge[y:y+h, x:x+w]
count = 0

circles = cv2.HoughCircles(edge,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=40,maxRadius=150)
try:

  circles = np.uint16(np.around(circles))
  print(circles)
  for i in circles[0,:]:
    print("I: {}".format(i))
  # draw the outer circle
    count = count + 1
    print ("Center Coordinates", i[0],i[1])
    if (count <= 1):
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
    print ("Center Coordinates", i[0],i[1])

  cv2.imshow('Display', img)

  cv2.waitKey(0)
  cv2.destroyAllWindows()

except AttributeError:
  print (" Not able to detect the radius")