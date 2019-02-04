import math
import time
x=0
y=0
s=0
s_ge=0
count=0
p_gyro=0

tstamp=open("tstamp.txt",'w')

ge = open("(g,e)readings.txt",'r')


gyro=[]
g_diff=[]
lge = []
rge = []
tge = []

k = open("(g+e)readings.txt",'r')

rc=[]
l=[]
r=[]
ts1=[]

w = open("o_e_g,e.txt",'w',0)


for val in k:
        reading = val.split(",")
        rc.append(reading[0])
        encoder = (reading[1].split(" "))
        l.append(float(encoder[0]))
        r.append(float(encoder[1]))
        ts1.append(float(encoder[2]))
        #tstamp.write(encoder[2])
        s = s + 1
print s 
                
        
for val1 in ge:
        geread = (val1.split(","))
        #gyro.append(float(geread[0]))
        #if(gyro[val1]+gyro[val1] )     
        #g_diff.append(gyro[s_ge] - p_gyro)
        #p_gyro = gyro[s_ge]
        encoderge=(geread[1].split(" "))
        lge.append(float(encoderge[0]))
        rge.append(float(encoderge[1]))
        tge.append(float(geread[3]))
        s_ge = s_ge + 1

#for num in range (s):
                #tstamp.write(str(ts1[num])+"\n")

cou = []
sum =0
x=0
y=0
count = open("angle_count.txt",'r')
for line in count:
        cou.append(line)
        x=x+1
        sum = sum + int(line)

darr = []
g = open("(g,e)readings.txt",'r')
for kl in g:
        reading = kl.split(",")
        #read = reading[2].split(" ")
        darr.append(float(reading[2]))
#print sum
print darr
obs_ang = []
angle = open("sensor_angle.txt",'r')
for line1 in angle:
        obs_ang.append(math.radians(float(line1)))
        y=y+1
print(x,y)
p_ts=ts1[0]
p_tge=tge[0]
j=0
i=0
print s_ge
while(i <> s+1):
        #print(i,j)
        if float(cou[i]) == 0:
                i=i+1
                j=j+1
                print i
                continue
                
        obsang = float(obs_ang[i])/float(cou[i])
        if rc[i] =='w':
                while(tge[j]>=p_ts and tge[j]<=ts1[i+1]):
                        #w.write("w" + "," + str(lge[j]) + " " + str(rge[j]) +"\n")
                        w.write(str("0") + "\n")
                        j=j+1
                i=i+1
                #p_ts=ts1[i+1]
        elif rc[i]=='s':#back
                while(tge[j]>=p_ts and tge[j]<=ts1[i+1]):
                        #w.write("s" + "," + str(lge[j]) + " " + str(rge[j]) +"\n")
                        w.write(str("0")+"\n")
                        j=j+1
                i=i+1
                #p_ts=ts1[i+1]
        
                        
        elif rc[i]=='a':#left
                while(tge[j]>=p_ts and tge[j]<=ts1[i+1]):
                        if obsang == 0:
                                comp_filter = darr[j]
                        elif float(cou[i])== 24:
                                print "Bingo"
                                comp_filter = (1.5* darr[j]) -(0.5* obsang)
                        else:
                                comp_filter = (0.975* darr[j]) +(0.025* obsang)
                        #w.write("a" + "," + str(lge[j]) + " " + str(rge[j]) + "," + str(comp_filter)+"\n")
                        w.write(str(comp_filter)+"\n")
                        j=j+1
                i=i+1
                #p_ts=ts1[i+1]

                        
        elif rc[i]=='d':#right
                while(tge[j]>=p_ts and tge[j]<=ts1[i+1]):
                        if obsang == 0:
                                comp_filter = darr[j]
                        else:
                                comp_filter = (1.2*darr[j])+(-0.2*obsang)                     
                        #w.write("d" + "," + str(lge[j]) + " " + str(rge[j]) + "," + str(comp_filter)+"\n")
                        w.write(str(comp_filter)+"\n")
                        j=j+1
                i=i+1
                #p_ts=ts1[i+1]
                
                                                        
                                
                        

                
                        
        
                
                
