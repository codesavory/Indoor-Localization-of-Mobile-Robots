import numpy as np
import matplotlib.pyplot as plt
x=[]
y=[]
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

major_ticks = np.arange(-850,850,30)
minor_ticks = np.arange(-480,480,30)

ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor =True)
ax.set_yticks(major_ticks)
ax.set_yticks(minor_ticks, minor =True)

ax.grid(which='both')
readFile = open('newdata2.txt','r')
sepFile = readFile.read().split('\n')
readFile.close()

for plotpair in sepFile:
	XANDY = plotpair.split(',')
	if len(XANDY) > 1:
		x.append(int(float(XANDY[0])))
		#x.set_rotation(45)
		y.append(int(float(XANDY[1])))
plt.plot([x],[y],'o',color='green')
plt.plot([x[0]],[y[0]],'o',color='red')
plt.show()
