from itertools import izip

r1 = open("(g,e)readings.txt",'r')
r2 = open("kalman_chumma.txt","r")

w = open("kalman.txt",'w',0)

for gyro,encoder in zip(r1,r2):
	reading = gyro.split(",")
	w.write(str(reading[0])+" "+str(encoder))
