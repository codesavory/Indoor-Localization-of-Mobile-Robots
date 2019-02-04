r=open("newdata.txt","r")
f=open("encoderangle.txt",'w')
sepFile = r.read().split('\n')
for ag in sepFile:
	gyro=ag.split(',')
	f.write(gyro[2]+"\n")
