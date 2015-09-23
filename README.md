# ColorDetect

This is a simple project which detects the color of the object infront of the webcam and then send that information to Arduino which lights an RGB-LED to that color. Its not very accurate, but it is decently accurate given its simplicity. 

The way it works is, python call a terminal command to capture a photo via the webcam, then copies that photo to the htdocs folder in which the php is placed, then the python calls the php which is running on localhost and php reads the image and returns its average RGB values. Now the python sends these values to Arduino using USB or bluetooth, and a sketch running in Arduino will light the LED.

Usage: 

cd path-to-main.py
python3 main.py /dev/ttyACM0 link-to-localhost-php path-to-php

for eg:

python3 main.py /dev/ttyACM0 http://localhost/colordetect/getcolor.php /opt/lampp/htdocs/colordetect/

All the code in this was written by me, and can be used/modified by anyone, just give me credit, if you can.
