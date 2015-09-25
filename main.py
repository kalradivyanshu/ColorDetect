import numpy as np
import cv2
import serial
import sys
import time
def show(values):
	image = np.zeros((300, 300, 3), np.uint8)
	blue, green, red = values
	image[:] = (blue, green, red)
	font = cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(image,str(values),(140,290), font, 0.6,(255-blue,255-green,255-red),2,cv2.LINE_AA)
	cv2.imshow('Color Detected',image)
def transmitdata(values):
	serialport = sys.argv[1]
	ser = serial.Serial(serialport, 9600)
	blue, green, red = values
	InputString = str(blue)+","+str(green)+","+str(red)
	ser.write(str.encode(InputString))
	time.sleep(0.5)
def getcolor(img):
	blue = int(img[:,:,0].mean())
	green = int(img[:,:,1].mean())
	red = int(img[:,:,2].mean())
	if abs(green-blue) <20 and abs(red-blue)<20 and abs(blue-green)<30:
		green=blue=red=250
	elif green==max(blue,green,red):
		green=250
		if blue>150 and red<150:
			blue = 250
			red = 0
		elif blue<150 and red>150:
			blue =0
			red=250
		else:
			blue=0
			red=0
	elif red==max(blue,green,red):
		red=250
		if blue>100 and green<100:
			blue = 250
			green = 0
		elif blue<100 and green>100:
			blue =0
			green=250
		else:
			blue=0
			green=0
	elif blue==max(blue,green,red):
		blue=250
		if red>100 and green<100:
			red = 250
			green = 0
		elif red<100 and green>100:
			red =0
			green=250
		else:
			red=0
			green=0
	return blue, green, red
cap = cv2.VideoCapture(0)
while(True):
# Capture frame-by-frame
	ret, frame = cap.read()
	# Our operations on the frame come here
	gray = cv2.cvtColor(frame,0)
	# Display the resulting frame
	cv2.imshow('LiveFeed',gray)
	transmitdata(getcolor(gray))
	show(getcolor(gray))
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()