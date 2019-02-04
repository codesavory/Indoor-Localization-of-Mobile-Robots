from bstem.platform import AdCord
from math import *
#from gyro_calib_kalman	import *
import time
import threading
import math

ad=AdCord()

offsetX=0
offsetY=0
offsetZ=0
for i in range(1,500): #500 values mean offset 
	#print(ad.gyroscope.z)
	offsetX+=ad.gyroscope.x
	offsetY+=ad.gyroscope.y
	offsetZ+=ad.gyroscope.z
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
	
	if((ad.gyroscope.x)-offsetX)>noiseX:
		noiseX=((ad.gyroscope.x)-offsetX)
	elif((ad.gyroscope.z)-offsetX)< -noiseX:
		noiseX=-((ad.gyroscope.x)-offsetX)

	if((ad.gyroscope.y)-offsetY)>noiseY:
		noiseY=((ad.gyroscope.y)-offsetY)
	elif((ad.gyroscope.z)-offsetY)< -noiseY:
		noiseY=-((ad.gyroscope.y)-offsetY)

	if((ad.gyroscope.z)-offsetZ)>noiseZ:
		noiseZ=((ad.gyroscope.z)-offsetZ)
	elif((ad.gyroscope.z)-offsetZ)< -noiseZ:
		noiseZ=-((ad.gyroscope.z)-offsetZ)

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
def gyro():
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
	
		if (gyroRate-offset >= noise or gyroRate-offset <= -noise):		
			x=1
			gyroRate=((gyroRate) - offset)*(dt/1000)
			#print gyroRate,offset,noise
			angle=(p_gyroRate + gyroRate)/2 #((p_gyroRate + gyroRate)*dt*57.2957795)/2000
			p_gyroRate=gyroRate
			#angle/=8.75
			'''if (angle < 0):
				angle += 360;
			elif (angle >= 360):
				angle -= 360;'''
	
			if axis=='x':
				angleX=angle
			elif axis=='y':
				angleY=angle
			elif axis=='z':
				angleZ=angle
	
			return (x,angle)
		return(x,':P')
	
	while(True):
		time.sleep(dt/1000)
		z,gZ=g_angle('z',ad.gyroscope.z)
		if z==1:
			print("Gyro:"+str(gZ))
			return gZ

def orientation():
        #Racc - is the inertial force vector as measured by accelerometer, that consists of following components (projections on X,Y,Z axes):

        Racc=[]
        Rxacc=[]
        Ryacc=[]
        Rzacc=[]
        Racc.append(ad.accelerometer.value)
        Rxacc.append(Racc[0][0])
        Ryacc.append(Racc[0][1])
        Rzacc.append(Racc[0][2]) #not used value

        magRacc=sqrt(pow(Rxacc[0],2)+pow(Ryacc[0],2))
        #|Racc| = SQRT(RxAcc^2 +RyAcc^2 + RzAcc^2),

        lst=list(Racc[0])
        lst[0]=Rxacc[0]/magRacc
        lst[1]=Ryacc[0]/magRacc
        Racc[0]=tuple(lst)


        #Next we'll introduce a new vector and we'll call it

        #Rest = [RxEst,RyEst,RzEst]
        Rest=[]
        Rxest=[]
        Ryest=[]
        #Rzest=[]

        Rest.append(Racc[0])
        Rxest.append(Rest[0][0])
        Ryest.append(Rest[0][1])

        n=0
        Axy=[]
        GAxy=[]
        GAxy.append(ad.gyroscope.z)
        Axy.append({Rxest[0],Ryest[0]})
        f=open("reading.txt",'w')
	print("hey !!")
        while(True):
                gz=gyro()
                if((ad.accelerometer.x==0 and ad.accelerometer.y==0) or gz==0):
                        continue
                n+=1
                Racc.append(ad.accelerometer.value)
                Rxacc.append(Racc[n][0])
                Ryacc.append(Racc[n][1])
                magRacc=sqrt(pow(Rxacc[n],2)+pow(Ryacc[n],2))
                
                lst=list(Racc[n])
                lst[0]=Rxacc[n]/magRacc
                lst[1]=Ryacc[n]/magRacc
                Racc[n]=tuple(lst)

                #gyroscope
                #Rgyro=ad.gyroscope.value
                GAxy.append(gz)
                Axy.append((atan2(Rxest[n-1],Ryest[n-1])) + GAxy[n]) #Axy[n]
                #RateAxyAvg=((RateAxy[n]+RateAxy[n-1])/2)
                #Axy[n]=((atan2(Rxest[n-1],Ryest[n-1]))+(RateAxyAvg*(.01)))
		
		
                Rxgyro=sin(Axy[n])*magRacc #using accelerometer to try with encoders also
                Rygyro=cos(Axy[n])*magRacc

                wGyro=20#5-20
                Rxest.append((Rxacc[n] + Rxgyro * wGyro ) / (1 + wGyro))
                Ryest.append((Ryacc[n] + Rygyro * wGyro ) / (1 + wGyro))
                magRest=sqrt(pow(Rxest[n],2)+pow(Ryest[n],2))
                Rxest[n]=Rxest[n]/magRest
                Ryest[n]=Ryest[n]/magRest
                #finally
                #print("x:",Rxest[n]," y:",Ryest[n])
                #print('.')
                angle=atan2(Rxest[n],Ryest[n])
		angle*=57.2957795131

		if (angle < 0):
			angle += 360;
		elif (angle >= 360):
			angle -= 360;

                f.write("x:")
                f.write(str(Rxest[n]))
                f.write("     ,y:")
                f.write(str(Ryest[n]))
		f.write("     ,angle:")
		f.write(str(angle))
		#f.write("     ,degrees:")
		#f.write(str(angle*57.2957795131))
                f.write('\n')

        f.close()

if __name__ == "__main__":
	orientation()
