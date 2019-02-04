from time import sleep
import serial

ser = serial.Serial('/dev/ttyACM2',9600)
counter = 32
while True:
	counter +=1
	ser.write(str(chr(counter))) #convert the decimal number to ASCII and send it to arduino
	print ser.read() #read the newest output from the arduino
	sleep(100.0/1000) #100milllisecond which is 1/10th of a second
	if counter == 255:
		counter= 32
