Right now, we are working on 2 different versions for the image recognition parts. The Google Cloud Vision OCR detection will
be used with the OpenCV detection as well. For GCloudVision, we are using OCR to read the text of the image, and check if "PUSH TO OPEN"
is in it in any form. If so, the detection will output a 1.

For OpenCV we are working on detecting the button using a combination of filtering, thresholding and contour detection.
