import socket
import struct
import sys
import time

// references for USB:
// https://github.com/walac/pyusb/blob/master/docs/tutorial.rst

import usb.core
import usb.util


while True:

	dev = usb.core.find()

	dev.set_configuration()

	if ResetButton():
		Navigage()


def ResetButton():

	Reset = False
	Delay = 2
	
	if (): // receive reset button value

		Reset = True

		// send wait timer with delay

		Wait(Delay)

return Reset


def Wait(Delay)

	Timeout = 1000
	Data = False
	Expire = Timeout

	// send start wait timer with delay

	while (Expire > 0 & ~Done):
		// receive timer completion status

		if (Data):
			Expire = Timeout
		else:
			Expire = Expire - 1

	// send continue


def Navigate():

	Timer = 0.5
	Line = False
	Passed = False

	 quit = False

	while (~ResetButton() & ~quit):
		Floor = Sensors()

		if (Floor == -1):
			Line = True
		else if (Floor == 1 & Line):
			quit = True
			Wait(Timer)
				
	// send all stop


def Sensors():
	
	Bright = 67
	Dark = 33
	Floor = 0
	Speed = 0
	Theta = 15
	Radius = 5

	// receive floor line value

	if (Value > Bright):
		Floor = 1
	else if (Value < Dark):
		Flor = -1

	// receive right sensor value

	if (Right Sensor):
		// Send turn CCW with Theta
		Wait(0)
	else:
		// Send move forward and arc radius

