import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('groundtruth.jpg')
rows=len(img1)
colums=len(img1[0])
print rows,colums
w=open("newdata2.txt",'r')
v=open("pixels.txt",'w',0)
x=[]
y=[]
for dist in w:
    reading = dist.split(",")
    x.append(float(reading[0]))
    y.append(float(reading[1]))
for i in range(len(x)):
    a=(x[i])
    b=(y[i])
    if b < 0:
        b = -int(y[i])
        #print b
    if a < 0:
        a = -int(x[i])    
    if a < colums and b < rows:
        #print a,b,i
        img1[b][a]=[97,6,255]
    else:
        continue
cv2.imshow('img1',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
