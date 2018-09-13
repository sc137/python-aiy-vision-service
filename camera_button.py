#!/usr/bin/env python3
#
# camera-button.py 
# 
# run this in the terminal
# push the button to take pics
# for the aiy vision kit

from gpiozero import Button
from picamera import PiCamera
from datetime import datetime
import time
from aiy.vision.leds import Leds
from aiy.vision.leds import RgbLeds
from aiy.vision.leds import PrivacyLed
from subprocess import check_call

# led colors
RED = (0xFF, 0x00, 0x00)
GREEN = (0x00, 0xFF, 0x00)
YELLOW = (0xFF, 0xFF, 0x00)
BLUE = (0x00, 0x00, 0xFF)
PURPLE = (0xFF, 0x00, 0xFF)
CYAN = (0x00, 0xFF, 0xFF)
WHITE = (0xFF, 0xFF, 0xFF)

button = Button(23, hold_time=3)
camera = PiCamera()
leds = Leds()

# turn privacy light on
leds.update(Leds.privacy_on())

def capture():
    #print('button pressed')
    leds.update(Leds.rgb_on(GREEN))
    time.sleep(0.5)
    camera.resolution = (1920, 1080)
    timestamp = datetime.now().isoformat()
    camera.capture('/home/pi/Pictures/{}.jpg'.format(timestamp))
    print('captured {}.jpg'.format(timestamp))
    leds.update(Leds.rgb_off())

while True:
    button.when_released= capture
    n = input('push the button to capture. press any key to exit\n')
    if n:
        break

leds.update(Leds.privacy_off())
camera.close()
