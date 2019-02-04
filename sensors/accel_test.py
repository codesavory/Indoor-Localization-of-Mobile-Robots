from bstem.platform import AdCord
import time
ad=AdCord()

while(True):
	print(ad.accelerometer.value[0]*9.8,ad.accelerometer.value[1]*9.8,ad.accelerometer.value[2]*9.8)
	time.sleep(.5)

