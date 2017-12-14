from time import sleep
import picamera
import sys
from GoogleCloudVision import googleCloud
from distance_measure import distance
import serial
import math
import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image

def get_coordinates(obj):
    print("Button Pressed")
    ser=serial.Serial('/dev/ttyACM0',9600)
    sleep(2)
    ser.write(b'p')
    sleep(6)
    camera=picamera.PiCamera()
    camera.resolution=(2560,1920)
    camera.vflip=True
    camera.hflip=True
    sleep(2)
    camera.capture('Image.jpg',resize=(640,480))
    camera.close()
    try:
        k=googleCloud()
    except IndexError:
        return 0
    z=distance()
    print(z)
    pixels = [k[0]-320,240-k[1]]
    distance_3d = [((kit * z)/520) for kit in pixels]
    x=distance_3d[0]
    print("x: ",x)
    y=distance_3d[1]-3
    print("y: ",y)
    alpha=45
    l=42

    lx = l*math.cos(alpha/57.32)
    ly = l*math.sin(alpha/57.32)
    extension = 5


    ytheta=(alpha-57.32*math.atan((ly-y)/(lx+z-extension)))
    print("ytheta: ",ytheta)
    total_length = (ly-y) / math.sin(((alpha-ytheta)/57.32))
    length_extend = math.ceil(total_length - l) - 5
    print("length_extend: ",length_extend)
    #xtheta=57.32*math.asin(x/(total_length*math.cos(ytheta/57.32)))
    xtheta = 57.32*math.atan(x/(total_length))
    print("xtheta: ",xtheta)
    xtheta=math.ceil(xtheta)
    ytheta=math.ceil(ytheta)
    print(x,total_length,ytheta)
    print("xtheta: ",xtheta," ytheta :",ytheta)
    print("Total length :",total_length, "length_extend: ",length_extend)

    if(length_extend>35):
        length_extend=35
    length_extend_copy=length_extend
    xtheta_copy=xtheta
    ytheta_copy=ytheta
    #Move the arm sideways
    while xtheta!=0:
        #e,f = +/-
        if(xtheta>0):
            ser.write(b'f')
            xtheta=xtheta-1
        else:
            ser.write(b'e')
            xtheta=xtheta+1
        sleep(0.5)
    #Move the arm down
    print("xtheta done")
    sleep(1)

    while ytheta!=0:
        if(ytheta>0):
            ser.write(b'd')
            ytheta=ytheta-1
        else:
            ser.write(b'c')
            ytheta=ytheta+1
        sleep(0.5)
    print("ytheta done")
    sleep(1)

#Move the arm forward - main actuators
    while length_extend!=0:
        ser.write(b'a')
        length_extend=length_extend-1.0
        sleep(1.0)
    print("Extension for main arm done")
    sleep(1)
    sleep(5)
    small_actuator=distance()-3
    if(small_actuator>12):
        small_actuator=12
    print("Small Actuator ",small_actuator)
    copy_small_actuator=small_actuator

    while small_actuator!=0:
        ser.write(b'g')
        small_actuator=small_actuator-1.0
        sleep(1)
    print("Small actuator starting")
    sleep(1)

    while copy_small_actuator!=0:
        ser.write(b'h')
        copy_small_actuator=copy_small_actuator-1
        sleep(1)
    print("Small actuator retracting")
    sleep(1)

    while length_extend_copy!=0:
        if length_extend_copy>0:
            ser.write(b'b')
            length_extend_copy=length_extend_copy-1
            sleep(1)
    sleep(1)

    print("Came back")
    while(ytheta_copy!=0):
        if ytheta_copy>0:
            ser.write(b'c')
            ytheta_copy=ytheta_copy-1
        if ytheta_copy<0:
            ser.write(b'd')
            ytheta_copy=ytheta_copy+1
        sleep(0.5)

    print("Fix orientation thetay")
    sleep(1)
    while(xtheta_copy!=0):
        if xtheta_copy>0:
            ser.write(b'e')
            xtheta_copy=xtheta_copy-1
        if xtheta_copy<0:
            ser.write(b'f')
            xtheta_copy=xtheta_copy+1
        sleep(0.5)
    print("Fix orientation thetax")
    print("All done")
    sleep(2)
    ser.write(b'q')
    time.sleep(10)

class FloatLayoutApp(App):
    def build(self):
        layout = FloatLayout(size=(800, 480))
        # Create the rest of the UI objects (and bind them to callbacks, if necessary):
        wimg = Image(source='hodor.jpg', pos_hint={
                     'x': 0, 'y': 0.4}, size_hint=(0.5, 0.5))
        forward = Button(text="Forward", size_hint=(0.15, 0.2),
                         font_size=24, pos_hint={'x': 0.65, 'y': 0.65})
        goBack = Button(text="goBack", size_hint=(0.15, 0.2),
                         font_size=24, pos_hint={'x': 0.65, 'y': 0.65})
        reverse = Button(text="Reverse", size_hint=(0.15, 0.2),
                         font_size=24, pos_hint={'x': 0.65, 'y': 0.15})
        turnRight = Button(text="Turn right", size_hint=(
            0.15, 0.2), font_size=24, pos_hint={'x': 0.8, 'y': 0.4})
        turnLeft = Button(text="Turn left", size_hint=(
            0.15, 0.2), font_size=24, pos_hint={'x': 0.5, 'y': 0.4})
        doorActivate = Button(text="HODOR!", size_hint=(
            0.15, 0.2), font_size=24, pos_hint={'x': .1, 'y': 0.15})
        doorActivate.bind(on_press=get_coordinates)
        # Add the UI elements to the layout:
        layout.add_widget(wimg)
        layout.add_widget(doorActivate)
        layout.add_widget(forward)
        layout.add_widget(reverse)
        layout.add_widget(turnLeft)
        layout.add_widget(turnRight)
        return layout

if __name__ == '__main__':
    FloatLayoutApp().run()
