def complimentCalculate(gyroangle,encoderang):
	angle= 0.0
	angle = .50 *(angle + gyroangle) + .50 * encoderang
	return angle
if __name__ == '__main__':
    f = open('kalman.txt')
    g=open('compliangle.txt','w')
    List=[]
    for l in f:
        m=l.split()
        #print m[0]
        x=complimentCalculate(float(m[0]),float(m[1]))
        g.write(str(x) + '\n')
        #n=m[0].split()
        #print n[0]
    
