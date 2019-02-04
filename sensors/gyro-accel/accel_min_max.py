from bstem.platform import AdCord

ad=AdCord()

i=0
accel_min,accel_max=1,0
while(i<10000):
	i+=1
	print(i)
	#accel_min,accel_max,i
	accel = ad.accelerometer
	if (accel.x < accel_min ):
		accel_min=accel.x
	if accel.x > accel_max:
		accel_max=accel.x

print("Done")
print("accelmin: "+str(accel_min)+ " Accelmax: "+str(accel_max	) )
