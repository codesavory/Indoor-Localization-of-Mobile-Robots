from bstem.platform import AdCord
import threading
import serial_read as sr
import angle_calculate_obstacle as aco
import plot_klaus_brenner as pkb
from motor import *
import sys

g=threading.Thread(target=sr.serial_read) #serial read thread
g.daemon=True
g.start()

h=threading.Thread(target=aco.angle_calculate) #to dynamicaly calculate angle during obstacle alone
h.daemon=True
h.start()

i=threading.Thread(target=erun) #erun thread to get user input for controlling robot
i.daemon=True
i.start()

f=open('(g+e)readings.txt','w',0)
rc='w'
scalar=0.2
tscalar=0.35
newscalar=0.05

def run():
	global rc
	while True:
		rc = sr.qr.get()
		print rc
		#print("Leftwheel:",-adr.encoder[2].position*3.38)#left motor
		#print("Rightwheel:",adr.encoder[0].position*3.38)#right motor
		#f.write(str(-adr.encoder[2].position*3.38)+" "+str(adr.encoder[0].position*3.38)+"\n")
		if rc =='w':#forward
			#print(rc)
			aco.adr.motor[0].speed=scalar #right motor 
			aco.adr.motor[2].speed=-scalar #left motor

			l = -aco.adr.encoder[2].position
			r = aco.adr.encoder[0].position
			f.write('w'+","+str(l)+" "+str(r)+"\n")

		elif rc=='a':#left
			aco.adr.motor[0].speed=tscalar
			aco.adr.motor[2].speed=-newscalar
			#z,gZ=g_angler('z',adr.gyroscope.z)

		elif rc=='d':#right
			aco.adr.motor[0].speed=newscalar
			aco.adr.motor[2].speed=-tscalar
			#z,gZ=g_angler('z',adr.gyroscope.z)
			
		elif rc=='s':#back
			aco.adr.motor[0].speed=-scalar
			aco.adr.motor[2].speed=scalar
			
			l = -(aco.adr.encoder[2].position)
			r = (aco.adr.encoder[0].position)
			f.write('s'+","+str(l)+" "+str(r)+"\n")

		elif rc==' ':#stop
			aco.adr.motor[0].speed=0
			aco.adr.motor[2].speed=0

		elif rc =='x':#quit
			aco.adr.motor[0].speed=0
			aco.adr.motor[2].speed=0
			sys.exit()
	f.close()

if __name__ == "__main__":
    run()
