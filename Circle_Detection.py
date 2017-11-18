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
#cv2.imshow('img', img)
#*************************COLOR_THRESHOLD*********************************


#&&&&&&&&&&&&&&&&&&&&&&&&&& CONTINUOUS CURVE &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
#res=cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
kernel = np.array([[0,0,0], [0,1,0], [0,0,0]], np.float32)
#dilation = cv2.dilate(res,kernel,iterations = 1)
#kernel = np.ones((2,2),np.uint8)
#erosion = cv2.erode(dilation,kernel,iterations = 1)
#kernel=(np.ones((2,2), np.uint8)
#opening = cv2.morphologyEx(res, cv2.MORPH_OPEN, kernel)
#closing = cv2.morphologyEx(res, cv2.MORPH_CLOSE, kernel)
# opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)

#dilation = cv2.dilate(res,kernel,iterations = 1)
#res=cv2.erode(res,-1, kernel)
#cv2.imshow('opening', res)

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



#$$$$$$$$$$$$$$$$$$$$ FEATURE MATCHING $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# MIN_MATCH_COUNT = 10
# img1 = cv2.imread('Template_Button.jpg',0)         # queryImage
# img2 =cv2.imread('queryimage.jpg',0) # trainImage

# # Initiate SIFT detector
# sift = cv2.xfeatures2d.SIFT_create()
# # find the keypoints and descriptors with SIFT
# kp1, des1 = sift.detectAndCompute(img1,None)
# kp2, des2 = sift.detectAndCompute(img2,None)
# FLANN_INDEX_KDTREE = 1
# index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
# search_params = dict(checks = 50)
# flann = cv2.FlannBasedMatcher(index_params, search_params)
# matches = flann.knnMatch(des1,des2,k=2)
# # store all the good matches as per Lowe's ratio test.
# good = []
# for m,n in matches:
#     if m.distance < 0.7*n.distance:
#         good.append(m)
# if len(good)>MIN_MATCH_COUNT:
#     src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
#     dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)
#     M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
#     matchesMask = mask.ravel().tolist()
#     h,w = img1.shape
#     pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
#     dst = cv2.perspectiveTransform(pts,M)
#     img2 = cv2.polylines(img2,[np.int32(dst)],True,255,3, cv2.LINE_AA)
# else:
#     print( "Not enough matches are found - {}/{}".format(len(good), MIN_MATCH_COUNT) )
#     matchesMask = None

# draw_params = dict(matchColor = (0, 255, 0), # draw matches in green color
#                    singlePointColor = None,
#                    matchesMask = matchesMask, # draw only inliers
#                    flags = 2)
# img3 = cv2.drawMatches(img1,kp1,img2,kp2,good,None,**draw_params)
# plt.imshow(img3, 'gray'),plt.show()

#$$$$$$$$$$$$$$$$$$$$ FEATURE MATCHING $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


#@@@@@@@@@@@@@@@@@@@ CIRCLE DETECTION @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#circles = cv2.HoughCircles(roi,cv2.HOUGH_GRADIENT,1,20,
                            #param1=50,param2=30,minRadius=40,maxRadius=150)
# try:

#   circles = np.uint16(np.around(circles))
#   coord=[0,0,0]
#   #print(circles)
#   for i in circles[0,:]:

    
#   # draw the outer circle
#     count = count + 1
#     print ("Center Coordinates", i[0],i[1])
#     radius=i[2]
#     if radius<temprad:
#       temprad=radius
#       coord=i
#     #if (count <= 1):
#   cv2.circle(img,(coord[0]+x,coord[1]+y),temprad,(0,255,0),2)
#     # draw the center of the circle
#   cv2.circle(img,(coord[0]+x,coord[1]+y),2,(0,0,255),3)
#   print ("Center Coordinates", i[0],i[1])

#   cv2.imshow('Display', img)

#   cv2.waitKey(0)
#   cv2.destroyAllWindows()

# except AttributeError:
#   print (" Not able to detect the radius")

#@@@@@@@@@@@@@@@@@@@CIRCLE DETECTION@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

cv2.waitKey(0)
cv2.destroyAllWindows()

