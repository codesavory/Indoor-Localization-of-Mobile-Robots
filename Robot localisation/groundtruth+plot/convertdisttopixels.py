w=open("newdata.txt",'r')
v=open("pixels.txt",'w',0)
x=[]
y=[]
for dist in w:
    reading = dist.split(",")
    x.append(float(reading[0]))
    y.append(float(reading[1]))
for i in range(len(x)):
    v.write(str(x[i])+","+str(y[i])+"\n")    
    
