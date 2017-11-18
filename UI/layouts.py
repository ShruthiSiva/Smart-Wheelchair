#File name: floatlayout.py
#Have to define callback functions to trigger from buttons press.
#
# import imageRecognition
import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image

import RPi.GPIO as GPIO
#Setup pins for Raspberry Pi-ARduino Interface

arduino_pin_S2=11
arduino_pin_S1=13
arduino_pin_S0=15
ultrasonicSensor=12

# the three input control direction input recieved from thr rasp pi
#
#           S2 S1 S0
#
# Nothing   0  0  0
# Up        0  0  1
# Down      0  1  0
# Left      0  1  1
# Right     1  0  0
# Forward   1  0  1
# Back      1  1  0
# Press     1  1  1


#Set GPIO mode as Board
GPIO.setmode(GPIO.BOARD)

#Setup the pins as outputs and inputs
GPIO.setup(arduino_pin_S2,GPIO.OUT)
GPIO.setup(arduino_pin_S1,GPIO.OUT)
GPIO.setup(arduino_pin_S0,GPIO.OUT)
GPIO.setup(ultrasonicSensor,GPIO.IN)

#Setup pins as default states set to low(0)
GPIO.output(arduino_pin_S2,LOW)
GPIO.output(arduino_pin_S1,LOW)
GPIO.output(arduino_pin_S0,LOW)

#Declare global variables for distance_from_object,

def range_check():
#Convert ultrasound sensor to distance, and return distance.
#Function to drive pins for a fixed amount of time.
def driver(pinNumber,driveTime):
	for i in range (0,driveTime):
		GPIO.output(pinNumber,HIGH)
	GPIO.output(pinNumber,LOW)

def press_callback(obj):
	#Define function to obtain drivetime
	if obj.text=='UP':
		driver(arduino_pin_S0,driveTime)
	if obj.text=='DOWN':
		driver(arduino_pin_S1,driveTime)
	if obj.text=='LEFT':
		driver(arduino_pin_S1,driveTime)
		driver(arduino_pin_S0,driveTime)
	if obj.text=='RIGHT':
		driver(arduino_pin_S2,driveTime)

class FloatLayoutApp(App):
	def build(self):
		return FloatLayout()

if __name__=='__main__':
	FloatLayoutApp().run()
