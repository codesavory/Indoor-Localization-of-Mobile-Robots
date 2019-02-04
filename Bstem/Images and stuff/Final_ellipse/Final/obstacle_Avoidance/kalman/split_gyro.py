r=open("newdata.txt","r")
f=open("encodersang.txt",'w')
sepFile = r.read().split('\n')
for ag in sepFile:
        m=0.0
        gyro =ag.split(' ')
        m=float(gyro[0])*(-1)
        if m < 0:
                m = 360-m
        f.write(str(m) +'\n')
