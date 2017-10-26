# Smart-Wheelchair

The TrialVision.py file is a compilation of the several features of the Cloud Vision API by Google such as web detection, text detection, detection of properties and document reading. 
We used the web detection property to gather a bunch of labels from images of handicap buttons. This list of possible labels will be used by PushButtonWhen.py to compare a given image with those that were run through TrialVision.py

The PushButtonWhen.py program combines the text detection and web detection featured of the clous vision API. If our image happens to contain a list of consecutive letters that either read "PUSH" or "OPEN", the program detects a match. Likewise, if the labels obtained from web detection match at least one of the predetermined  list of labels from trialVision.py, the program detects a match.

******************************************************************************************************************************

Format of running PushButtonWhen.py:
------------------------------------

python3 PushButtonWhen.py <nameofimage.jpg>

 <nameofimage.jpg> can be changed to your choice of image.

