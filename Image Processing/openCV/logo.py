
import argparse
import io
import glob
import sys
import os, os.path
import cv2
import numpy as np


from google.cloud import vision
from google.cloud.vision import types

def detect_properties(path):
    """Detects image properties in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.image_properties(image=image)
    props = response.image_properties_annotation
    print('Properties:')

    for color in props.dominant_colors.colors:
        print('fraction: {}'.format(color.pixel_fraction))
        print('\tr: {}'.format(color.color.red))
        print('\tg: {}'.format(color.color.green))
        print('\tb: {}'.format(color.color.blue))
        print('\ta: {}'.format(color.color.alpha))



def detect_crop_hints(path):
    """Detects crop hints in an image."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content)

    crop_hints_params = types.CropHintsParams(aspect_ratios=[1.77])
    image_context = types.ImageContext(crop_hints_params=crop_hints_params)

    response = client.crop_hints(image=image, image_context=image_context)
    hints = response.crop_hints_annotation.crop_hints

    for n, hint in enumerate(hints):
        print('\nCrop Hint: {}'.format(n))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in hint.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))

def detect_logos(path):
    """Detects logos in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.logo_detection(image=image)
    logos = response.logo_annotations
    print('Logos:')

    for logo in logos:
        print(logo.description)

detect_crop_hints('test1.jpg')
#detect_properties('test1.jpg')
img=cv2.imread('test5.jpg')
x,y,w,h = cv2.boundingRect(img)
img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

#img= img[0:3455, 0:1934]
#img= cv2.resize(img,None,fx=0.1, fy=0.1, interpolation = cv2.INTER_CUBIC)
#cv2.imwrite('testcrop.jpg', img)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()