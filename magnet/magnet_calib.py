import math
from bstem.sensor import Magnetometer
from bstem import compass_calibration
from bstem.platform import AdCord
import time
a= AdCord()
while(True):
	x=a.magnetometer.x
	y=a.magnetometer.y
	z=a.magnetometer.z
	n = sqrt((x*x)+(y*y)+(z*z))
	x=x/n
	y=y/n
	z=z/n
	print (x,"\t",y,"\t",z,"\n")
