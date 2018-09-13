#!/usr/bin/env python3
#
# camera_button_svc.py 
# run this after boot using crontab -e 

from gpiozero import Button
from picamera import PiCamera
from datetime import datetime
from aiy.vision.leds import Leds
from aiy.vision.leds import RgbLeds
from aiy.vision.leds import PrivacyLed
from subprocess import check_call
import time

# led colors
RED = (0xFF, 0x00, 0x00)
GREEN = (0x00, 0xFF, 0x00)
YELLOW = (0xFF, 0xFF, 0x00)
BLUE = (0x00, 0x00, 0xFF)
PURPLE = (0xFF, 0x00, 0xFF)
CYAN = (0x00, 0xFF, 0xFF)
WHITE = (0xFF, 0xFF, 0xFF)

# setup vars
button = Button(23, hold_time=2)
camera = PiCamera()
leds = Leds()

# turn on the privacy light
leds.update(Leds.privacy_on())

def shutdown():
    leds.update(Leds.privacy_off())
    camera.close()
    for i in range(3):
        leds.update(Leds.rgb_on(RED))
        time.sleep(0.2)
        leds.update(Leds.rgb_off())
        time.sleep(0.2)
    check_call(['sudo', 'poweroff'])

def capture():
    time.sleep(0.1)
    camera.resolution = (1920, 1080)
    timestamp = datetime.now().isoformat()
    leds.update(Leds.rgb_on(GREEN))
    camera.capture('/home/pi/Pictures/{}.jpg'.format(timestamp))
    leds.update(Leds.rgb_off())

# blink ready
leds.update(Leds.rgb_on(RED))
time.sleep(0.15)
leds.update(Leds.rgb_off())
time.sleep(0.15)

leds.update(Leds.rgb_on(YELLOW))
time.sleep(0.15)
leds.update(Leds.rgb_off())
time.sleep(0.15)

leds.update(Leds.rgb_on(GREEN))
time.sleep(0.15)
leds.update(Leds.rgb_off())
time.sleep(0.15)

while True:
    # whenever the putton is pushed and released, take a photo
    button.when_released = capture
    # whenever the button is held for 2 seconds, shutdown
    button.when_held = shutdown
