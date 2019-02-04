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
arrz=[]
arrz.append(0)
for i in f:
	print(i)
	arr=(i.split())
	arrz[0]=float(arr[2])
	ax.plot(xs=float(arr[0]), ys=float(arr[1]), zs=arrz, label='Accelerometer')
	ax.legend()
	plt.draw()
plt.show()
