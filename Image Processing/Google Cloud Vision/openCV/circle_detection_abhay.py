import cv2
import numpy as np
import sys
def main():
    img=cv2.imread(sys.argv[1])
    img_shape=(img.shape[0],img.shape[1])
    cv2.imshow('img',img)
    #img=cv2.resize(img,(int(img.shape[0]*0.2),int(img.shape[1]*0.2)))
    #cv2.imshow('resized_img',img)
    img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    lower_blue=np.array([80,50,50])
    upper_blue=np.array([130,255,255])
    mask=cv2.inRange(img_hsv,lower_blue,upper_blue)

    res=cv2.bitwise_and(img,img,mask=mask)
    res=cv2.medianBlur(res,7)
    cv2.imshow('res2',res)
    res=cv2.Canny(res,150,150)

    #To eliminate the black spaces
    pixelpoints=cv2.findNonZero(res)

    x,y,w,h=cv2.boundingRect(pixelpoints)
    res=cv2.rectangle(res,(x,y),(x+w,y+h),255,2)

    cv2.imshow('res',res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()
