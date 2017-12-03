# Smart-Wheelchair


=======
## Userstory
We want to design a wheelchair which can use new technologies to empower physically disabled people. 

Our typical user might be someone with partial paralysis, or someone who has mobility impairments. 

=======
## Modules

Our project has several folders. The arm for the wheelchair was designed in Solidworks and the drawings are in the Arm Design - Solidworks folder. The code for interfacing the arm to the arduino mega is in the Arduino Files for ARM folder. They are a basic version for controlling the arm depending on the value of 3 output pins of the raspberry pi.

The Image Processing folder has two sub-trees, one being Google Cloud Vision and the second being OpenCV. We are considering both for a viable solution. The benefit of having a custom openCV implementation, is that it will be available offline and can be optimized for faster results. We have also developed and tested a tensorflow MobileNet SSD detector on our data set, however the raspberry pi is not able to process the images in real time, hence we are going with a hybrid solution for now.

The UI folder has the files for generating the User interface on the raspberry pi touchscreen. We are using Kivy as the platform for the UI.

We have added a more reliable solution employing tensorflow object detection API to handle the image recognotion after Sprint 3. There are several advantages of using this API to using cloud vision or opencv:
1. The image recognition will be completely offline
2. Our error rate has decreased significantly
3. Delay has reduced from about 10s to an average of 3s ( On a PC/Mac). 


=======
