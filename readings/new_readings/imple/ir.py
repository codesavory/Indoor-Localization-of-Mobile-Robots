from bstem.platform import AdCord
import time
ad = AdCord()
f=open("encoders.txt",'w')
while(True):
	ad.gpio[0].direction="in"
	val=ad.gpio[0].value
	print(val)
	f.write("M "+str(-ad.encoder[3].position*3.38)+" "+str(ad.encoder[1].position*3.38)+"\n")
	if (val==1):#black #straight
		ad.motor[1].speed=0.2#right motor
		ad.motor[3].speed=-0.2#left motor
	elif val==0:#white #left
		ad.motor[1].speed=0.2#right motor
		ad.motor[3].speed=0.2#left motor
	#time.sleep(0.05)
