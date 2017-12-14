# Smart-Wheelchair


=======
## Userstory
We want to design a wheelchair which can use new technologies to empower physically disabled people. 

Our typical user might be someone with partial paralysis, or someone who has mobility impairments. 

=======
## Modules

Our project has several folders. The arm for the wheelchair was designed in Solidworks and the drawings are in the Arm Design - Solidworks folder. The code for interfacing the arm to the arduino mega is in the Arduino Files for ARM folder. They are a basic version for controlling the arm depending on the value of 3 output pins of the raspberry pi.

The Image Processing folder has three sub-trees: Google cloud vision, OpenCV and TensorFlow. Since we need to identify handicapped buttons, we can look for the phrase "PUSH TO OPEN" in the current image, hence the first solution using Optical Character Recognition. We tried implementing a Haar cascade filter following canny Edge detection in OpenCV, but it did not give satisfactory results. Finally, we decided to use the newly released TensorFlow MobileNet SSD released in June 2017 for the detection. For instructions on setting up TensorFlow on the Pi, check out the guide at https://github.com/samjabrahams/tensorflow-on-raspberry-pi. Check out some of the recent issues for the 1.4 wheel file for TensorFlow on Raspbian Jessie and above. 

The UI folder has the files for generating the User interface on the Raspberry Pi touchscreen. We are using Kivy as the platform for the UI. You can follow Matt Richardson's guide for the same at https://github.com/mrichardson23/rpi-kivy-screen, for enabling the touchscreen functions. 

Running the tensorflow program on the Pi, even with a frozen model is extremely slow. Two steps which greatly helped was loading the graph into memory once and reusing it, instead of calling the function repeated times. The second step was keeping the tensorflow session permanent, since the first run always takes extra time when everything is loaded up, but the second is on average 5 times fast. 

Finally the arm equations were derived from basic geometry and the design was completed.

The tests conducted were basically testing the model against the testing data. It gave an accuracy of 86.5% and the results are in the graph picture.
=======


Please refer to the Final Folder for the final working set of files!
