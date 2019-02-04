w=open("encoders.txt","w",0)
r=open("(g,e)readings.txt",'r')
#sepFile = r.read().split('\n')
sepFile = r.read().split('\n')
for val in sepFile:
	reading = val.split(',')
	encoder = reading[1].split(' ')
	w.write("M "+str(encoder[0])+" "+str(encoder[1])+" "+str(reading[1])+"\n")

w.close()
