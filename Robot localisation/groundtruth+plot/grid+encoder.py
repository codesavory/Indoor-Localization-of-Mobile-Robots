import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('grid.jpg')
rows=len(img1)
colums=len(img1[0])
print rows,colums
w=open("grnd.txt",'r')
v=open("pixels.txt",'w',0)
x=[]
y=[]
for dist in w:
    reading = dist.split(",")
    #print reading[0]
    #print reading[1]
    x.append(reading[0])
    y.append(reading[1])
    
for i in range(len(x)):
    print "hi"
    a=int(x[i])
    b=int(y[i])
    print a,b
    img1[a][b]=[97,6,255]
#img1[102][460]=[97,6,255]   
cv2.imshow('img1',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
