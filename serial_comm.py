#!/usr/bin/python2.7 -tt

import serial as s
import sys

def setup(baud):
	sp=s.Serial("/dev/ttyAMA0")
	sp.baudrate = baud
	return sp

def send_data(sp,data):
	sp.write(data)
	print "data txted suceffuly"

def rcv_data(sp,num=100):
	data=sp.read(num)
	return data

def main():
	if len(sys.argv) != 3 and len(sys.argv) != 4 :
		print"usage : python serial_comm.py r/w baudrate [,data]"
		return -1
	if len(sys.argv) == 3 and sys.argv[1] =='w':
		print"usage : python serial_comm.py r/w baudrate [,data]"
		return -1
        if sys.argv[1]!='r' and sys.argv[1] != 'w':
		print "invalid option ",sys.argv[1] 
		return -1
	sp=setup(sys.argv[2])
        if(sys.argv[1]=='r'):
		data=rcv_data(sp,25)
		print data," is recieved"
	else:	send_data(sp,sys.argv[3])
	sp.close()

if __name__=="__main__":
	main()
	

