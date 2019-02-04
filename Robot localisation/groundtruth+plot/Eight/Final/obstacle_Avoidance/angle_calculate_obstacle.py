import threading
import math
from gyro_obstacle import *#returns gyro for every 20ms without summation

i=threading.Thread(target=gyror) #calling the gyroscope thread
i.daemon=True
i.start()

def angle_calculate():
	import obstacle_avoided as obs
	global ang
	global theta
	global p_dist
	global x,y
	while True:
		gz = qg.get()
		if obs.rc == 'a':#left
			l = -adr.encoder[2].position
			r = adr.encoder[0].position
			obs.f.write("a"+","+str(l)+" "+str(r)+","+str(gz)+"\n")

		elif obs.rc == 'd':#right
		        l = -adr.encoder[2].position
			r = adr.encoder[0].position
			obs.f.write("d"+","+str(l)+" "+str(r)+","+str(gz)+"\n")


