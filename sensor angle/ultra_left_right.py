from time import sleep
import serial


while True:
	ser = serial.Serial('/dev/ttyACM0',9600)
	
	#print str(ser.readline())
	f = open("lrultra.txt",'a')
	a=ser.readline()
	print a
	i=0
	f.write(str(a))
	sleep(0.5)
	#f.write(str(a))
f.close()



