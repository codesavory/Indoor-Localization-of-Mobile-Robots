import math
f = open("kalmanangle.txt",'r')
g = open("encoder_.txt",'r')
h= open("encoder_left.txt",'r')
angle = []
l = []
r = []
if __name__ == '__main__':
        global angle
        global l
        global r
        angle = [line.strip('\n')for line in open('kalmanangle.txt')]
        le = [line.strip('\n')for line in open('encoder_left.txt')]
        r = [line.strip('\n')for line in open('encoder_.txt')]     
           
   
   
        #print angle
        p_dist = 0.0
        p_ang = 0.0
        m=0.0
        i=0
        k=1499.99999816
        l=1499.99115118
        x1=0.0
        x2=0.0
        dist=0.0
        theta=0.0
        gz=0.0
        o=open("gyroposfile.txt",'w')
        #print float(l[i]) 
        while True:
                gz=float(angle[i])
                x1=(float(le[i]))
                x2=(float(r[i]))
                dist=(x1+x2)/2
                print dist
                m=dist-p_dist
                p_dist=dist
                theta=(math.radians(gz))
                k+=(m*(math.sin(theta)))
                l+=(m*(math.cos(theta)))
                i=i+1         
                o.write(str(k) + "," +str(l) + "\n")
                if i == 4500:
                        break
