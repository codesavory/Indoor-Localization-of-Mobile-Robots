Q_angle  =  0.4; '''//0.001'''
Q_gyro   =  0.3;  #//0.003
R_angle  =  0.3;  #//0.03

x_angle = 0.0
x_bias = 0.0
P_00 = 1
P_01 = 0.0
P_10 = 0.0
P_11 = 1
y = 0.0
S =0.0
K_0 = 0.5
K_1 = 0.5


def kalmanCalculate( encoderangle,  gyrorate):
    global Q_angle,Q_gyro,R_angle,x_angle,x_bias,P_00,P_01,P_10,P_11,y,S,K_0,K_1
    x_angle = x_angle + (encoderangle - x_bias)
    #print x_angle,encoderangle,x_bias
    P_00 = P_00+  -(P_10 + P_01) + Q_angle 
    P_01 = P_01 - P_11
    P_10 = P_10 - P_11
    P_11 = P_11  + Q_gyro

    y = gyrorate- x_angle
    S = P_00 + R_angle
    K_0 = P_00 / S
    K_1 = P_10 / S

    x_angle =  x_angle +( K_0 * y)
    x_bias =  x_bias  + (K_1 * y)
    P_00 =  P_00 -(K_0 * P_00)
    P_01 =  P_01 - (K_0 * P_01)
    P_10 =  P_10 - ( K_1 * P_00)
    P_11 = P_11 -(K_1 * P_01)

    return x_angle

if __name__ == '__main__':
    f = open('kalman.txt')
    g=open('kalmanangle.txt','w')
    List=[]
    for l in f:
        m=l.split()
        #print m[0]
        x=kalmanCalculate(float(m[0]),float(m[1]))
        g.write(str(x) + '\n')
        #n=m[0].split()
        #print n[0]
    
