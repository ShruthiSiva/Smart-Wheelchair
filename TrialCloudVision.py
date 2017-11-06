import argparse
import io
from PIL import Image
import glob
import os, os.path

from google.cloud import vision
from google.cloud.vision import types

values=[]
finalvalues=['Disability']



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

    for i in range (0, len(finaltext)-3):
        desired_word= finaltext[i]+finaltext[i+1]+ finaltext[i+2]+finaltext[i+3]
        if desired_word.lower() == 'push' or desired_word.lower()== 'open':
            case=1

    print("PUSH BUTTON TO OPEN DOOR")

    return finaltext

        



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


def detect_document(path):
    """Detects document features in an image."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.document_text_detection(image=image)
    document = response.full_text_annotation

    for page in document.pages:
        for block in page.blocks:
            block_words = []
            for paragraph in block.paragraphs:
                block_words.extend(paragraph.words)

            block_symbols = []
            for word in block_words:
                block_symbols.extend(word.symbols)

            block_text = ''
            for symbol in block_symbols:
                block_text = block_text + symbol.text

            print('Block Content: {}'.format(block_text))
            print('Block Bounds:\n {}'.format(block.bounding_box))

os.chdir("images")
for file in glob.glob("*.jpg"):
    q=detect_web('{}'.format(file))
    for elem in q:
    
        values.append(elem)

values= list(set(i for i in values if values.count(i) > 1))


    
        

            





print(values)



