# AIY Vision Auto Cam

## camera_button_svc.py

This script simply runs a basic camera on the Google AIY Vision kit.

* The LED will blink Red, Yellow, then green when ready
* Push the button to take a photo. The green LED will light.
* Hold the button for 2 seconds to shutdown the pi. You will see the red LED blink.

Insert a line into your crontab to run this.

    crontab -e

At the bottom, put:

    @reboot sleep 10;python3 /home/pi/camera_button_svc.py

## camera_button.py

This script can be run from the command line. It will blink when you push the button to take a photo and will list the photo name it saved.

    ./camera_button.py
