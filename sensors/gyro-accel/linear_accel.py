from math import *
import numpy as np
import threading
from accel_calib1 import *
from gyro_calib import *

e=threading.Thread(target=gyro) #erun thread
e.daemon=True
e.start()

f=open("accel_no_gravity.txt",'w',0)
#accel_raw = ad.accelerometer
caccel = accelo()
accel = np.matrix([[caccel[0]],[caccel[1]],[caccel[2]]])
angx,angy,angz=0,0,0
theta=0
def check(a,b):
	if a>=min_accel or a<=-min_accel:
		if b>=min_accel or b<=-min_accel:
			return a,b
		else:
			return a,0
	else:
		if b>=min_accel or b<=-min_accel:
			return 0,b
		else:
			return 0,0
def linear_accel():
	#(dx,dy,dz)=gyro()
	dx=q.get()
	dy=q.get()
	dz=q.get()
	print("----------------------------------------------------------------------------------------")
	print("Raw angle:"+str(dx),str(dy),str(dz))
	global angx,angy,angz
	angx+=dx
	angy+=dy
	angz+=dz
	print("Angle:")
	print(angx,angy,angz)
	#accelerometer values when the bot is still...gravity acts in z direction....x-y plane
	accel_raw = accelo()
	#print(accel_raw)
	caccel = np.matrix([[accel_raw[0]],[accel_raw[1]],[accel_raw[2]]])
	print("Raw Accel: ")
	print(caccel)
	global accel
	#f.write("Raw: "+str(caccel[0])+","+str(caccel[1])+","+str(caccel[2])+"\n")
	rx=np.matrix([[1,0,0],[0,cos(radians(dx)),-sin(radians(dx))],[0,sin(radians(dx)),cos(radians(dx))]])
	ry=np.matrix([[cos(radians(dy)),0,sin(radians(dy))],[0,1,0],[-sin(radians(dy)),0,cos(radians(dy))]])
	rz=np.matrix([[cos(radians(dz)),-sin(radians(dz)),0],[sin(radians(dz)),cos(radians(dz)),0],[0,0,1]])
	Rx= rx * accel	#calucation of Rx,Ry,Rz ..i.r Rx =rx*caccel;
	Ry= ry * accel
	Rz= rz * accel
	#caluclation of Resultant Rx+Ry-Rz
	R=Rx + Ry - Rz
	print("Rotated Matrix:")
	print(R)
	#calculation of linear acceleration (current accelerometer values - Resultant)
	Linearaccel = caccel - R
	print("Linear Accel: ")
	print(Linearaccel)
	a,b=check(Linearaccel[0],Linearaccel[1])
	print(a,b)
	theta = atan2(a,b)
	print ("Orientation:",theta,degrees(theta))
	if theta!=0:
		f.write("linearAccel: "+str(Linearaccel[0])+","+str(Linearaccel[1])+","+"::"+str(a)+","+str(b))
		f.write("\nOrientation:"+"Radians:"+str(theta)+" ,Degrees:"+str(degrees(theta))+"\n")
	#f.write("-g: "+str(Linearaccel[0])+","+str(Linearaccel[1])+","+str(Linearaccel[2])+"\n")
	accel=R

if __name__ == "__main__":
	while(True):
		linear_accel()
