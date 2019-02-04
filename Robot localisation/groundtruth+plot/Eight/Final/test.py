import math
import time

k = open("(g+e)readings.txt",'r')

rc=[]
l=[]
r=[]
ts1=[]


for val in k:
	print "jhgjmhg"
	reading = val.split(",")
	rc.append(reading[0])
	encoder = (reading[1].split(" "))
	print (encoder[0])
	l.append(float(encoder[0]))
	r.append(float(encoder[1]))
	ts1.append(float(encoder[2]))
	s = s + 1
	
