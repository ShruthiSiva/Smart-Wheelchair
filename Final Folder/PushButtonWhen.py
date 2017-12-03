import io
import sys
import os, os.path
import numpy as np
from google.cloud import vision
from google.cloud.vision import types
import time
import cv2

def detect_text(path):
    case=0
    allvertices=[]
    finaltext=[]
    xvertices=[]
    yvertices=[]
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    for text in texts:
        finaltext.append(text.description)
        allvertices.append(text.bounding_poly.vertices)
    allvertices=list(allvertices[0])
    finaltext=finaltext[1:]
    finaltext=[k.lower() for k in finaltext]
    text_desired=['press','push','open','to']

#or all(x in finaltext for x in text_desired2) or all(x in finaltext for x in text_desired3) or all(x in finaltext for x in text_desired4):
    if any(x in finaltext for x in text_desired):
        case=1
    if case==1:
        string="PUSH BUTTON TO OPEN DOOR"
    else:
        string="WON'T OPEN DOOR"

    return string,allvertices

case=0

start_time = time.time()
if len(sys.argv)>2:
    print("Enter only one image value at a time, please!")
elif len(sys.argv)==1:
    print("Enter a valid image name to go on")
strin=sys.argv[1]

#desc= detect_web('{}'.format(strin))
string,vertices=detect_text('{}'.format(strin))
print("--- %s seconds ---" % (time.time() - start_time))

if string=="PUSH BUTTON TO OPEN DOOR":
    res=cv2.imread('../Images/Feature.jpg')
    res=cv2.rectangle(res,(vertices[0].x,vertices[0].y),(vertices[2].x,vertices[2].y),(0,0,255),5)
    cv2.namedWindow('res',cv2.WINDOW_NORMAL)
    cv2.imshow('res',res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print("PUSH BUTTON TO OPEN DOOR")
else:
    print("BUTTON NOT DETECTED")
