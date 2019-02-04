w=open("gyroscope.txt","w",0)
r=open("(g,e)readings.txt",'r')
#sepFile = r.read().split('\n')
for val in r: 
	w.write(val)

w.close()
