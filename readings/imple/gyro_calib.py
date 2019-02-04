from bstem.platform import AdCord
from math import *
import time
import sys
import Queue
#import sys.exitfunc

q=Queue.Queue()
ad=AdCord()
offsetX=0
offsetY=0
offsetZ=0
for i in range(1,500): #500 values mean offset 
	#print(ad.gyroscope.z)
	offsetX+=ad.gyroscope.x*57.2957795
	offsetY+=ad.gyroscope.y*57.2957795
	offsetZ+=ad.gyroscope.z*57.2957795
offsetX=offsetX/500
offsetY=offsetY/500
offsetZ=offsetZ/500
print("Offset:",offsetX,offsetY,offsetZ)

#----------------------------------------------------------------------

dt=20.0 #in milliseconds
noiseX=0
noiseY=0
noiseZ=0
print("Time:",(dt/1000))
for i in range(1,500):
	
	if((ad.gyroscope.x*57.2957795)-offsetX)>noiseX:
		noiseX=((ad.gyroscope.x*57.2957795)-offsetX)
	elif((ad.gyroscope.z*57.2957795)-offsetX)< -noiseX:
		noiseX=-((ad.gyroscope.x*57.2957795)-offsetX)

	if((ad.gyroscope.y*57.2957795)-offsetY)>noiseY:
		noiseY=((ad.gyroscope.y*57.2957795)-offsetY)
	elif((ad.gyroscope.z*57.2957795)-offsetY)< -noiseY:
		noiseY=-((ad.gyroscope.y*57.2957795)-offsetY)

	if((ad.gyroscope.z*57.2957795)-offsetZ)>noiseZ:
		noiseZ=((ad.gyroscope.z*57.2957795)-offsetZ)
	elif((ad.gyroscope.z*57.2957795)-offsetZ)< -noiseZ:
		noiseZ=-((ad.gyroscope.z*57.2957795)-offsetZ)

	#print("Noise:",noiseZ)
	#time.sleep(dt/1000)

#noiseZ=noiseZ*(dt/1000)
#print(noiseZ)
'''noiseX=noiseX*(dt/1000)
noiseY=noiseY*(dt/1000)
noiseZ=noiseZ*(dt/1000)'''

#time.sleep(dt/1000)
print("noisu:",noiseX,noiseY,noiseZ)

a=str(raw_input("Continue(y/n):"))
if(a=='n'):
	sys.exit()
#-----------------------------------------------------------------------

angleX=0
angleY=0
angleZ=0
#rotationThreshold=1
ad.gyroscope.dps=250
print(ad.gyroscope.dps)
p_gyroRate=0

def g_angle(axis,gyroRate):
	#global angle
	global p_gyroRate
	global angleX,angleY,angleZ
	global noiseX,noiseY,noiseZ
	global offsetX,offsetY,offsetZ
	x=0
	if axis=='x':
		noise=noiseX
		offset=offsetX
		angle=angleX

	elif axis=='y':
		noise=noiseY
		offset=offsetY
		angle=angleY

	elif axis=='z':
		noise=noiseZ
		offset=offsetZ
		angle=angleZ

	if (gyroRate*57.2957795-offset >= noise or gyroRate*57.2957795-offset <= -noise):		
		x=1
		gyroRate=((gyroRate*57.2957795) - offset)*(dt/1000)
		#print gyroRate,offset,noise
		angle+=(p_gyroRate + gyroRate)/2 #((p_gyroRate + gyroRate)*dt*57.2957795)/2000
		p_gyroRate=gyroRate
		#angle/=8.75
		if (angle < 0):
			angle += 360;
		elif (angle >= 360):
			angle -= 360;

		if axis=='x':
			angleX=angle
		elif axis=='y':
			angleY=angle
		elif axis=='z':
			angleZ=angle

		return (x,angle)
	return(x,':P')

def gyro():
	while(True):
		time.sleep(dt/1000)
		#gyroRate=ad.gyroscope.z
		#print("Grate: ",gyroRate)
		'''
		x,gX=g_angle('x',ad.gyroscope.x)
		y,gY=g_angle('y',ad.gyroscope.y)
		z,gZ=g_angle('z',ad.gyroscope.z)
		if(x==1 or y==1 or z==1):
			print("X:",gX," Y:",gY," Z:",gZ)
		
		'''
		z,gZ=g_angle('z',ad.gyroscope.z)
		if z==1:
			q.put(gZ)
			#print(gZ)
if __name__ == "__main__":
	gyro()
