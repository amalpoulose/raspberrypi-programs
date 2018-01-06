#!/usr/bin/python2.7 -tt
import sys
import RPi.GPIO as gpio

def setup():
	gpio.setmode(gpio.BCM)
	gpio.setup(17,gpio.OUT)


def led(arg):
	if arg:
		gpio.output(17,True)
		print "LED ON"
	else:	
		gpio.output(17,False)
		print "LED OFF"


def main():
	if len(sys.argv) !=2:
		print "Usage : python led.py ON/OFF"
		return -1
	setup()
	if sys.argv[1].upper()=="ON":
		led(1)
	else:	led(0)

if __name__=="__main__":
	main()	
