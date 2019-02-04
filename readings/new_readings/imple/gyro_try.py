from math import * 
#import tty, sys, termios

print "Enter the initial position of the robot:"
k= 1500#input('Enter X:')
l= 1500#input('Enter Y:')

p_dist=0
p_ang=0

f=open("newdata.txt","w",0)
r1=open("gyroscope.txt","r")
#r2=open("encoders.txt","r")
for gz in r1:#zip(r1,r2):
	#dist=((((en.split(','))[1]*3.38)+((en.split(','))[2]*3.38))/2)
	r=5
	#r=dist-p_dist
	#p_dist=dist
	#print("Left:"+str(-ad1.encoder[2].position*3.38))
	#print("Right:"+str(ad1.encoder[1].position*3.38))
	#print(dist)
	print("deg+"+str(gz))
	theta=(radians(float(gz)))
	print("rad:"+str(radians(float(gz))))
	#theta=ang-p_ang
	#p_ang=ang
	#print (dist,p_dist,r)
	#print (ang,p_ang,theta)
	k+=(r*(sin(theta)))
	l+=(r*(cos(theta)))
	print("x+:"+str(r*(sin(theta))))
	print("y+:"+str(r*(cos(theta))))	
	print("---------------------------")
	f.write(str(k) + "," +str(l) + "\n")
f.close()
