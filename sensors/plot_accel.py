import pylab
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

x,y = np.random.randn(2,100)
mpl.rcParams['legend.fontsize'] = 10
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

pylab.xlim([0,1])
ax.set_autoscalex_on(False)
pylab.ylim([0,1])
ax.set_autoscaley_on(False)
#pylab.zlim([0,1])
#ax.set_autoscalez_on(False)
#ax.acorr(x, usevlines=True, normed=True, maxlags=50, lw=2)
#ax.xcorr(x, y, usevlines=True, maxlags=50, normed=True, lw=2)
f=open("accel.txt",'r')
arr=[]
for i in f:
	arr.append(i.split())

arrx=[]
arry=[]
arrz=[]
for i in range(len(arr)):
	print(arr[i])
	arrx.append(float(arr[i][0]))
	arry.append(float(arr[i][1]))
	arrz.append(float(arr[i][2]))

ax.xscale=50
ax.plot(xs=arrx, ys=arry, zs=arrz, label='Accelerometer')
ax.legend()
plt.show()
