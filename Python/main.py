import urllib.request
import serial
import sys
import os
import time
from tkinter import *
def send():
	serialport = sys.argv[1]
	link = str(sys.argv[2])
	path = str(sys.argv[3])
	ser = serial.Serial(serialport, 9600)
	red = urllib.request.urlopen(link+"?red").read().decode("utf-8") 
	green = urllib.request.urlopen(link+"?green").read().decode("utf-8") 
	blue = urllib.request.urlopen(link+"?blue").read().decode("utf-8") 
	InputString = blue+","+green+","+red
	print(str.encode(InputString))
	ser.write(str.encode(InputString))
	print(ser.readline())
def capture():
	os.system("fswebcam -r 1280x720 --jpeg 85 -D 1 image.jpeg --no-banner")
	time.sleep(1)
	print("Captured")
	os.system("cp image.jpeg "+path)
	time.sleep(1)
def justdoit():
	capture()
	send()
b = Button(text="Capture", command=justdoit)
b.pack()

mainloop()