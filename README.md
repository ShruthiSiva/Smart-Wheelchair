# Smart-Wheelchair


=======
## Userstory
We want to design a wheelchair which can use new technologies to empower physically disabled people. 

Our typical user might be someone with partial paralysis, or someone who has mobility impairments. 

=======
## Modules

Our project has several folders. The arm for the wheelchair was designed in Solidworks and the drawings are in the Arm Design - Solidworks folder. The code for interfacing the arm to the arduino mega is in the Arduino Files for ARM folder. They are a basic version for controlling the arm depending on the value of 3 output pins of the raspberry pi.

The Image Processing folder has two sub-trees, one being Google Cloud Vision and the second being OpenCV. We are considering both for a viable solution. The benefit of having a custom openCV implementation, is that it will be available offline and can be optimized for faster results. 

The UI folder has the files for generating the User interface on the raspberry pi touchscreen. We are using Kivy as the platform for the UI.

=======
