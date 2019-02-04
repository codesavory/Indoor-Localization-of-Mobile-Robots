from bstem.platform import AdCord
import time
ad=AdCord()
i=0
dt=20
while True:
	time.sleep(dt/1000)
	i+=1
	gyro = ad.gyroscope.value
	if i>0:
		print(gyro[0],gyro[1],gyro[2])
