# your code goes here
import kacc_gyro as l
from run1 import *
import sys
import time
import numpy as np
import math
import multiprocessing
import gyro_filter as g

def accelcalib():
	#calibrated accelerometer values from accelerometer of the bstem
	return (l.kacc())
def gyrocalib():
	#calculation of the the change of angle from gyroscope value
	return (l.gyro())
def distance(ang,i,accelx,accely):
	if i == 0:
		return(0,0)
	else:
		global velocityx,velocityy,positionx,positiony		
		print (accelx[i-1],accely[i-1])
		print (accelx[i])
		print (i)
		velocityx.append(velocityx[i-1] + accelx[i-1] * 0.01)
		positionx.append(velocityx[i]*0.01 + (accelx[i]*0.01*0.01)/2)
		velocityy.append(velocityx[i-1] + accelx[i-1] * 0.01)
		positiony.append(velocityy[i]*0.01 + (accely[i]*0.01*0.01)/2)
		return (round(positionx[i],5),round(positiony[i],5))
(ax,ay,az)=accelcalib()
rtd=57.2957795
accel=np.matrix([[ax],[ay],[az]])
accelx=[0]
accely=[0]
velocityx=[0]
velocityy=[0]
positionx=[0]
positiony=[0]
f=open("orientaion.txt",'w',0)
def orientationangle():
	global accel 
	i=0
	while(True):
		(ax,ay,az)=accelcalib()
		(dx,dy,dz)=gyrocalib()
		#print(ax,ay,az)
		#print("\n")
		#print(dx,dy,dz)
		f=open("orientaion.txt",'w')
		if i>200:
			#print("RateGyro:",dx,dy,dz)
			#accel=np.matrix([[0],[0],[az]])
			#accelerometer values when the bot is still...gravity acts in z direction....x-y plane
			caccel = np.matrix([[ax],[ay],[az]])
			#calculation of rotation matrix along the respective axis rx,ry,rz
			print i
			rx=np.matrix([[1,0,0],[0,math.cos(dy),-math.sin(dy)],[0,math.sin(dy),math.cos(dy)]])
			ry=np.matrix([[math.cos(dx),0,math.sin(dx)],[0,1,0],[-math.sin(dx),0,math.cos(dx)]])
			rz=np.matrix([[math.cos(dz),-math.sin(dz),0],[math.sin(dz),math.cos(dz),0],[0,0,1]])
			Rx= rx * accel	#calucation of Rx,Ry,Rz ..i.r Rx =rx*caccel;
			Ry= ry * accel
			Rz= rz * accel
			#caluclation of Resultant Rx+Ry-Rz
			R=Rx + Ry - Rz
			#print(Rx,Ry,Rz,R)
			#calculation of linear acceleration (current accelerometer values - Resultant)
			Linearaccel= caccel - R
			#print("Linearaccel:",Linearaccel)
			time.sleep(0.01)
			accel=R
			#print Linearaccel       
			#coversion of the matrix into array
			global accelx,accely
			angle=np.array(Linearaccel)
			accelx.append(Linearaccel[0])
			accely.append(Linearaccel[1])
			x,y=distance(angle,i-200,accelx,accely)
			#calculation of orientation angle
			print ("x,y",x,y)
			x1=np.array(abs(x))
			print(x1)
			y1=np.array(abs(y))
			print(y1)
			orientationangle = math.atan2(x1,y1)
			aid=orientationangle* 57.294
			#print ("accel",caccel) 
			#print ("LInear",Linearaccel)
			print ("orientation",aid)
			f.write("\n" +str(aid) +"\n")
			
		i=i+1
		f.close()	#f=open("orientaion.txt",'w')
			#print angle[0],angle[1]
			#f.write(str(ad1.encoder[3].position*3.38)+" "+str(ad1.encoder[1].position*3.38)+" "+str(aid)+"\n")
if __name__ == "__main__":
	orientationangle()
