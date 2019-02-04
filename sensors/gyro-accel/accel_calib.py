from bstem.platform import AdCord

ad=AdCord()
def accel():
		global pnoise
		global snoise
		global error 	
		pnoise=0.1	
		snoise=0.8
		error=0
		gx=ad.accelerometer.x
		gy=ad.accelerometer.y
		gz=ad.accelerometer.z

		while(True):
			x = (ad.accelerometer.x)
			y = (ad.accelerometer.y)
			z = (ad.accelerometer.z)	
			error=error+pnoise
			k=error/(error+snoise)
			gx = gx+k*(x-gx)
			gy = gy+(k*(y-gy))
			gz = gz+k*(z-gz)
			error=(1-k)*error
			#print(gx,gy,gz)
			#print(x,y,z)
			print(str("%.2f" %gx)+","+str("%.2f" %gy)+","+str("%.2f" %gz))
			print("#######")
			#print("Raw: "+str("%.5f" %y) + "  y" + str("%.5f" %gy))# + "Y: 	"+"LA: "+str("%.5f" %gy) + "Z: "+"LA: "+str("%.5f" %gz))
			ystr=str("%.2f" %y)
			gystr=str("%.2f" %gy)
			#return(float(ystr),float(gystr))

if __name__ == "__main__":
	accel()
