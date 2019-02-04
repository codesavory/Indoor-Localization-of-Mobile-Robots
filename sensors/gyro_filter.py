from bstem.platform import AdCord
import time
global i,count
i=0
count=0.0000000001
ad=AdCord()

def gyro_filter():
	global i,count
	i=0
	count=0.0000000001
	global pnoise
	global snoise
	global error 	
	pnoise=0.128
	snoise=1
	error=0
	gx=(ad.gyroscope.x)
	gy=(ad.gyroscope.y)
	gz=(ad.gyroscope.z)
	x = (ad.gyroscope.x)
	y = (ad.gyroscope.y)
	z = (ad.gyroscope.z)	
	error=error+pnoise
	k=error/(error+snoise)
	gx = gx+k*(x-gx)
	gy = gy+(k*(y-gy))
	gz =gz+k*(z-gz)
	error=(1-k)*error
	time.sleep(0.015)
	print (gx,gy,gz)
	print(x,y,z)
	print("\n")	
	return(gx,gy,gz)
if __name__ == "__main__":
	while(True):
		gyro_filter()
