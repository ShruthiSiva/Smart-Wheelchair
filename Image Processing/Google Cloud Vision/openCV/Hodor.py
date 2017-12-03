#This is the last year's team and their final code.
#After capturing 

import cv2
import numpy as np
import os
import picamera
import sys
import picamera.array
import time
import serial
import pyuarm

sys.path.append('/usr/local/lib/python3.4/site-packages')

#Variables
dpi = 96
w = 640
w1 = 640
h = 480
h1 = 480
flagg = 1
sp = 50

#Bluetooth communication
ser = serial.Serial('/dev/rfcomm0')
x = ser.read(2)
if (x==x):
    print('Open Request Received')
ser.close()

#Image Processing
camera = picamera.PiCamera()
camera.resolution = (640,480)
camera.framerate =32
rawCapture = picamera.array.PiRGBArray(camera, size=(640,480))
time.sleep(0.5)
i = 0

for frame in camera.capture_continuous(rawCapture, format="bgr" , use_video_port=True):
    img = frame.array
    img = cv2.medianBlur(img,5)
    #cv2.imshow("image",img)
    key = cv2.waitKey(2) & 0xFF
    rawCapture.truncate(0)
    if (key == ord("q") or flagg == 0):
        exit()

    count = 0
    edge = cv2.Canny(img,100,200)
    circles = cv2.HoughCircles(edge,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=40,maxRadius=100)

    try:
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            flagg=1
        # draw the outer circle
            count = count + 1
            #while(flagg ==1):
            if (count <= 10):
                    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
                # draw the center of the circle
                    cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
                    cv2.imwrite("/home/pi/Desktop/EC601_door/ip/output/opt.jpg",img)
                    cx = i[0]*25.4/(2*dpi)
                    cy = i[1]*25.4/(2*dpi)
                    flagg = 0
                    print ("Center Coordinates", i[0],i[1])
        if (flagg == 0):
            break

    except AttributeError:
        print (" Not able to detect the radius")

print("Uarm")
#Uarm commands
uarm = pyuarm.get_uarm()
ch = w1*25.4/(2*dpi)
cv = h1*25.4/(2*dpi)
print("Ch =",ch)
print("Ch =",cx)
print("Cv =",cv)
print("Cv =",cy)
x, y, z = uarm.get_position()
print("Current arm position",x,y,z)

#Slope
if cx >= ch/2 and cy <= cv/2:
    sl = 1
    print(sl)
    print("Move to",0.7*(x + abs(cx-ch)),y+200,0.7*(z + abs(cy-cv)))
    uarm.set_position(0.7*(x + abs(cx-ch)),y+200,0.7*(z + abs(cy-cv)),sp)
elif cx < ch/2 and cy <= cv/2:
    sl = 2
    print(sl)
    print("Move to",0.7*(x - abs(cx-ch)),y+200,0.7*(z + abs(cy-cv)))
    uarm.set_position(0.7*(x - abs(cx-ch)),y+200,0.7*(z + abs(cy-cv)),sp)
elif cx < ch/2 and cy > cv/2:
    sl = 3
    print(sl)
    print("Move to",0.7*(x - abs(cx-ch)),y+200,0.7*(z - abs(cy-cv)))
    uarm.set_position(0.7*(x - abs(cx-ch)),y+200,0.7*(z - abs(cy-cv)),sp)
elif cx > ch/2 and cy > cv/2:
    sl = 4
    print(sl)
    print("Move to",0.7*(x + abs(cx-ch)),y+200,0.7*(z - abs(cy-cv)))
    uarm.set_position(0.7*(x + abs(cx-ch)),y+200,0.7*(z - abs(cy-cv)),sp)

'''print("Difference")
print("Slope",sl)
print("CX - CH",cx-ch)
print("CY - CV",cy-cv)'''
time.sleep(5)
#x1, y1, z1 = uarm.get_position()
#print("New arm position",x1,y1,z1)

uarm.set_position(30,134,150)
#plt.show()
uarm.disconnect()
