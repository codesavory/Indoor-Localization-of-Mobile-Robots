#This  is a very big program with great potential, dont judge by the number of lines of this code.
#If you dont believe me, go see the obstacle_avoided file that this file imports

from bstem.platform import AdCord
import threading
import time
import gyro_calib as gc
import gyro_obstacle as go
from obstacle_avoided import *

e=threading.Thread(target=gc.gyro) #gyro thread
e.daemon=True
e.start()

i=threading.Thread(target=go.gyror) #calling the gyroscope thread
i.daemon=True
i.start()

f=threading.Thread(target=run) #run thread to control motor in obstacle autonomouosly
f.daemon=True
f.start()

r1=open("(g,e)readings.txt","w",0)
while True:
	t= time.time()
	gz=gc.q.get()
	gzz=go.qg.get()
	r1.write(str(gz)+","+str(-gc.ad.encoder[2].position)+" "+str(gc.ad.encoder[0].position)+","+str(gzz)+"," + str(t)+"\n")
r1.close()
