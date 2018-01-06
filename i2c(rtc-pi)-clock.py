#!/usr/bin/python -tt

import smbus
import time
import os

def main():
	bus=smbus.SMBus(1)
	bus.write_byte_data(0x68,0x00,0x50)
	bus.write_byte_data(0x68,0x01,0x59)
	bus.write_byte_data(0x68,0x02,0x23)
        while(1):
		os.system("clear")
		hr=bus.read_byte_data(0x68,0x2)
		m =bus.read_byte_data(0x68,0x1)
		s =bus.read_byte_data(0x68,0x0)
		print hex(hr)[2:],":",hex(m)[2:],":",hex(s)[2:]
		time.sleep(1)
if __name__ == "__main__":
	main()

