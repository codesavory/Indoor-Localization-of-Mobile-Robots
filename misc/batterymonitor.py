from bstem.platform import AdCord
from bstem.platform import Bstem
from datetime import datetime

ad=AdCord()
b=Bstem()

ad.gyroscope.enabled=False
ad.accelerometer.enabled=False
ad.barometer.enabled=False
ad.magnetometer.enabled=False

print(ad.gyroscope.enabled,ad.accelerometer.enabled,ad.barometer.enabled,ad.magnetometer.enabled)

ad.gyroscope.enabled=True
ad.accelerometer.enabled=True
ad.barometer.enabled=True
ad.magnetometer.enabled=True

print(ad.gyroscope.enabled,ad.accelerometer.enabled,ad.barometer.enabled,ad.magnetometer.enabled)

'''ad.motor[0].speed=0.5
ad.motor[2].speed=-0.5'''

t=datetime.time(datetime.now())
print("Time:",t)
print("Second:",t.second)
m=t.minute
mi=t.minute
print("Minute",m)
while(m!=mi+20):
	while(True):
		arr=[]
		t=datetime.time(datetime.now())
		if(m+1==t.minute):
			print("Incresed one minute")
			m=t.minute
			for i in range(100):
				arr.append(ad.battery)
				#print(arr[i])
			sum=0
			for i in range(100):
				sum+=arr[i]
			print(sum/100)
			break

ad.gyroscope.enabled=False
ad.accelerometer.enabled=False
ad.barometer.enabled=False
ad.magnetometer.enabled=False
ad.motor[0].speed=0
ad.motor[2].speed=0
print("End of pgm:)")
