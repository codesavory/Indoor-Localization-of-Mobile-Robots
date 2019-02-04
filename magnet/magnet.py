from bstem.sensor import Magnetometer
from bstem import compass_calibration
from bstem.platform import AdCord
import time
a= AdCord()
while(True):
	x=a.magnetometer.x
	y=a.magnetometer.y
	z=a.magnetometer.z
	print(x ,"\t" ,y ,"\t", z, "\n")
	time.sleep(0.01)
