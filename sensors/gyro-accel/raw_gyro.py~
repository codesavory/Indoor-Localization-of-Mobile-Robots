from bstem.platform import AdCord
import time
ad=AdCord()
f=open("gyro_readings_raw",'w',0)
while True:
	time.sleep(20/1000)
	f.write(str(ad.gyroscope.x)+","+str(ad.gyroscope.y)+","+str(ad.gyroscope.z)+"\n")
	print(ad.gyroscope.value)
