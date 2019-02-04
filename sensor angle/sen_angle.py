from time import sleep
import serial
import string

#ser = serial.Serial('/dev/ttyACM2',9600)



def sen_angle(dl,dr,dli,dri):
	ds = 50
 	ang= 0.0
	cons=40
	dn = 10
	print dl,dr
	#dl = 30	
	#dr = 60
	if (dl<ds and dr>ds):
		print "dl<ds"
		div = cons/dl
		ang= ang-(90)*(div)
		return ang
		#f.write(str(ang) +" "+\n)

	elif (dr<ds and dl>ds):
		print "dr<ds"
		div = cons/dr
		ang= ang+(90)*(div)
		return ang

	elif(dr<ds and dl<ds):
		if(dli > dn and dri < dn ):
			print "dli > dn and dri < dn "
			div = cons/dri
			ang= ang+(90)*(div)
			return ang

		elif (dri > dn and dli < dn):
			print "dri > dn and dli < dn"
			div = cons/dli
			ang= ang-(90)*(div)
			return ang
		elif (dri < dn and dli < dn):
			print "dri < dn and dli < dn"
			return ang
		else:
			return ang
			#between dsafe and dn

	else:
		print "nothing"		
		return ang
if __name__ == "__main__":
	f=open("sensor_angle.txt",'w')
	g=open("lrultra.txt",'r')
	a=[]
	for line in g:
		a.append(line)
	#print a 
	print len(a)
	ultra_left = []
	ultra_right = []
	infra_left = []
	infra_right = []
	i=0
	aa = []
	aa = a.split(" ")
	for i in range(len(a)):
		ultra_left.append(aa[0])
		ultra_right.append(aa[1])
		infra_left.append(aa[2]) 
		infra_right.append(aa[3])
	print "*************"	
	#print ultra_left
	print len(ultra_left)
	print "*************"
	#print ultra_right
	print len(ultra_right)
	angle =0 
	for i in range(len(ultra_right)):
		angle = sen_angle(ultra_left[i],ultra_right[i],infra_left[i],infra_right[i])
		print angle










	#while True:
	#	sen_angle()
