import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from gyro_calib import *
from encoders import *
import math
import threading

print "Enter the initial position of the robot:"	
#Setting initial points
ix= input('Enter X:')
iy= input('Enter Y:')
f=open("data.txt","w",0)
f.write(str(ix) + "," +str(iy) + "\n")
f.close()

g=threading.Thread(target=gyro) 		#gyro thread
g.daemon=True
g.start()

e=threading.Thread(target=erun) #erun thread
e.daemon=True
e.start()

p_dist=0
p_ang=0

f=open("data.txt","w",0)
while True:
	gz=q.get()
	dist=(((-ad.encoder[2].position*3.38)+(ad.encoder[1].position*3.38))/2)-p_dist
	ang=math.radians(gz)-p_ang
	k=dist*math.sin(ang)+ix
	l=dist*math.cos(ang)+iy
	f.write(str(int(k)) + "," + str(int(l)) + "\n")
	p_dist=dist
	p_ang=ang
f.close()
