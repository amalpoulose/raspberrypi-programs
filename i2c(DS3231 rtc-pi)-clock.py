#!/usr/bin/python2.7

import smbus
import time
import os
import RPi.GPIO as gpio

def main():
	gpio.setmode(gpio.BCM)
	gpio.setup(17,gpio.OUT)
	bus=smbus.SMBus(1)
	t=time.strptime(time.ctime())
        sec=int(str(t[5]),16)
        m=int(str(t[4]),16)
        hr=int(str(t[3]),16)
	bus.write_byte_data(0x68,0x00,sec)
	bus.write_byte_data(0x68,0x01,m)
	bus.write_byte_data(0x68,0x02,hr)
	flag=-1
        while(1):
		os.system("clear")
		hr=bus.read_byte_data(0x68,0x2)
		m =bus.read_byte_data(0x68,0x1)
		s =bus.read_byte_data(0x68,0x0)
                if s==0 and flag ==-1:
			gpio.output(17,False)
		if s==0 and flag==1:
			gpio.output(17,True)
		flag = -flag	
		print hex(hr)[2:],":",hex(m)[2:],":",hex(s)[2:]
		time.sleep(1)
if __name__ == "__main__":
	main()

