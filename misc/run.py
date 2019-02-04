from bstem.platform import AdCord
while(1):
	mes = input("Please enter the message::")
	ad =AdCord()
	if (mes == 8):
		
		ad.motor[0].speed=0.5
		ad.motor[2].speed=-0.5
	if (mes == 2):
		
		ad.motor[0].speed=0
		ad.motor[2].speed=-0
	if (mes == 4):#left
		ad.motor[0].speed=0.5
		ad.motor[2].speed=0.5
	if (mes == 6):
		ad.motor[0].speed=-0.5
		ad.motor[2].speed=-0.5 
	if (mes==5):
		ad.motor[0].speed=-0.5
		ad.motor[2].speed=0.5


