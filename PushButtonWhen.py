import argparse
import io
from PIL import Image
import glob
import os, os.path

from google.cloud import vision
from google.cloud.vision import types

def detect_web(path):
    desc=[]
    """Detects web annotations given an image."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.web_detection(image=image)
    notes = response.web_detection

    if notes.web_entities:
        for i in range (0,(len(notes.web_entities))):
            if notes.web_entities[i].score>=0.7:

                score=1
            else:
                score=0
            

            if score==1:
                desc.append(notes.web_entities[i].description)
    return desc

    print(desc)

def detect_text(path):
    case=0

    finaltext=[]
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:

        finaltext.append(text.description)

    finaltext=''.join(finaltext[1:])

    finaltext=list(finaltext)
    print(finaltext)
    for i in range (0, len(finaltext)-3):
        desired_word= finaltext[i]+finaltext[i+1]+ finaltext[i+2]+finaltext[i+3]
        if desired_word.lower() == 'push' or desired_word.lower()== 'open':
            case=1
    if case==1:

        string="PUSH BUTTON TO OPEN DOOR"
    else:
        string="WON'T OPEN DOOR"

    return string

case=0

    
desc= detect_web('Test7.jpg')
string=detect_text('Test7.jpg')
values=['Push-button', 'Product', 'Disability', 'Switch', 'Product design', 'Door']
for element in desc:
    for elem in values:
        if element==elem:
            case=1

if string=="PUSH BUTTON TO OPEN DOOR":
    case=1

if case==1:
    print("PUSH BUTTON TO OPEN DOOR")
else:
    print("BUTTON NOT DETECTED")
