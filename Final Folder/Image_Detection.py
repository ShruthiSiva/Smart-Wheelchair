import cv2
import numpy as np
import sys
import io
from google.cloud import vision
from google.cloud.vision import types
import time
#from picamera import PiCamera
import base64

def main():
    vertices, finaltext=[],[]
    client = vision.ImageAnnotatorClient()
    # Uncomment this part for Raspberry Pi
    # camera=PiCamera()
    # camera.resolution=(800,600)
    # camera.start_preview()
    # sleep(1)
    # camera.capture('Image.jpg',resize=(320,240))
    # with io.open('Image.jpg', 'rb') as image_file:
    #     content = image_file.read()
    with io.open(sys.argv[1],'rb') as image_file:
        content=image_file.read()
    image = types.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    for text in texts:
        finaltext.append(text.description)
        vertices.append(text.bounding_poly.vertices)

    vertices=list(vertices[0])
    finaltext=finaltext[1:]
    finaltext=[k.lower() for k in finaltext]
    text_desired=['press','push','open','to']
    if any(x in finaltext for x in text_desired):
        res=cv2.imread(sys.argv[1])
        res=cv2.rectangle(res,(vertices[0].x,vertices[0].y),(vertices[2].x,vertices[2].y),(0,0,255),5)
        cv2.namedWindow('res',cv2.WINDOW_NORMAL)
        cv2.imshow('res',res)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("PUSH BUTTON TO OPEN DOOR")
    else:
        string="WON'T OPEN DOOR"
    # return string,allvertices
    #
    # img=cv2.imread(sys.argv[1])
    # img_shape=(img.shape[0],img.shape[1])
    # cv2.imshow('img',img)
    # #img=cv2.resize(img,(int(img.shape[0]*0.2),int(img.shape[1]*0.2)))
    # #cv2.imshow('resized_img',img)
    # img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #
    # lower_blue=np.array([80,50,50])
    # upper_blue=np.array([130,255,255])
    # mask=cv2.inRange(img_hsv,lower_blue,upper_blue)
    #
    # res=cv2.bitwise_and(img,img,mask=mask)
    # res=cv2.medianBlur(res,7)
    # cv2.imshow('res2',res)
    # res=cv2.Canny(res,150,150)
    #
    # #To eliminate the black spaces
    # pixelpoints=cv2.findNonZero(res)
    #
    # x,y,w,h=cv2.boundingRect(pixelpoints)
    # res=cv2.rectangle(res,(x,y),(x+w,y+h),255,2)
    #
    # cv2.imshow('res',res)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

main()
