from time import sleep
import serial
import string

#ser = serial.Serial('/dev/ttyACM2',9600)


ang= 0.0
def sen_angle(dr,dl,dri,dli):
	ds = 50.0
 	global ang
	#ang= 0.0
	#pang = 0.0	
	dn = 35.0
	#print dl,dr,dli,dri
	#dl = 30.0	
	#dr = 60.0
	div = 0.0
	if ((dl>35.0 and dl<ds) or (dr<ds and dr>35.0)):
		if (dl < dr):
			#cons = ds-dl
			#print "dl<ds"
			#print dl
			#print cons
			cons=10
			div = cons/dl
			#print div
 			ang= ang-(90)*(div)
			#pang=ang
			return ang
			
		else:
			#cons = ds-dr
			cons=10
			#print cons
			#print "dr<ds"
			div = cons/dr
			ang= ang+(90)*(div)
			#pang=ang
			return ang
			
	
		#f.write(str(ang) +" "+\n)
        elif ((dli>15.0 and dl<dn) or (dr<dn and dr>15.0)):
		if (dli < dri):
			#cons = ds-dli
			cons=10
			#print "dl<ds"
			#print dl
			#print cons
			div = cons/dl
			#print div
 			ang= ang-(90)*(div)
			#pang=ang
			return ang
		else:
			#cons = ds-dri
			cons=10	
			#print cons
			#print "dr<ds"
			div = cons/dr
			ang= ang+(90)*(div)
			#pang=ang
			return ang
	else:
		#print "nothing"		
		return ang
	'''elif (dr<ds and dl>ds):
		cons = ds-dr
		print cons
		print "dr<ds"
		div = cons/dr
		ang= ang+(90)*(div)
		return ang

	elif(dr<ds and dl<ds):
		if(dr>10 and dl>10):
			if(dr>dl):
				cons = ds-dl
				print "dl<ds"
				print cons,dl
				div = cons/dl
 				ang= ang-(90)*(div)
				return ang
			elif(dl>dr):
				cons = ds-dr
				print "dr<ds"
				div = cons/dr
				ang= ang+(90)*(div)
				return ang
		elif(dr<15 and dl<15):
				return ang'''
				
				
	'''if(dli > dn and dri < dn ):
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
			return ang'''
			#between dsafe and dn

	
if __name__ == "__main__":
	f=open("sensor_angle.txt",'w')
	g=open("lrultra.txt",'r')
	a=[]
	for line in g:
		a.append(line)
	#print a 
	#print len(a)
	#print a 
	ultra_left = []
	ultra_right = []
	infra_left = []
	infra_right = []
	i=0
	aa = []
	
	for i in range(len(a)):
		aa = a[i].split(" ")
		ultra_left.append(aa[0])
		#print aa[3]
		ultra_right.append(aa[1])
		infra_left.append(aa[2]) 
		infra_right.append(aa[3])
	#print "*************"	
	#print ultra_left
	#print len(ultra_left)
	#print "*************"
	#print ultra_right
	#print len(ultra_right)
	angle =0 
	for i in range(len(ultra_right)):
		angle = sen_angle(float(ultra_left[i]),float(ultra_right[i]),float(infra_left[i]),float(infra_right[i]))
		print angle,"\n"
		#print i
		f.write(str(angle)+"\n")









	#while True:
	#	sen_angle()
