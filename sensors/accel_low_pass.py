from bstem.platform import AdCord
import time
ad=AdCord()

alpha=0.25	 #between 0-1
dt=20.0		#in milliseconds
gx=0.0
gy=0.0
gz=0.0
f=open("accel.txt","w",0)
while(True):
	x = (ad.accelerometer.x)
	y = (ad.accelerometer.y)
	z = (ad.accelerometer.z)
	gx = (1-alpha)*x + (alpha)*gx
	gy = (1-alpha)*y + (alpha)*gy
	gz = (1-alpha)*z + (alpha)*gz
	linear_accel_x = x - gx
	linear_accel_y = y - gy
	linear_accel_z = z - gz
	print("X: "+"LA: "+str("%.5f" %linear_accel_x) + "Y: "+"LA: "+str("%.5f" %linear_accel_y) + "Z: "+"LA: "+str("%.5f" %linear_accel_z))
	f.write(str("%.5f" %gx)+" "+str("%.5f" %gy)+" "+str("%.5f" %gz)+"\n")
	'''f.write("X: "+"LA: "+str("%.5f" %linear_accel_x) +" "+ str(x))
	f.write("\tY: "+"LA: "+str("%.5f" %linear_accel_y) +" "+ str(y))
	f.write("\tZ: "+"LA: "+str("%.5f" %linear_accel_z) +" "+ str(z))
	f.write("\n")'''
	time.sleep(dt/1000)
f.close()
