import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image

x=[]
y=[]

plt.xlim(xmin=0,xmax=12778)											#setting the co-ordinate system for the map
plt.ylim(ymin=0,ymax=5549)

#img = mpimg.imread('scaledmap.png')
#imgplot = plt.imshow(img)
#im = plt.imshow(np.flipud(plt.imread('scaledmap.png')),origin='lower')

plt.title('Bstem Project')											#Setting the title
plt.xlabel('x label')
plt.ylabel('y label')

readFile = open('newdata1.txt','r')
sepFile = readFile.read().split('\n')
readFile.close()

for plotpair in sepFile:
	XANDY = plotpair.split(',')
	if len(XANDY) > 1:
		x.append(int(float(XANDY[0])))
		y.append(int(float(XANDY[1])))

#plt.clf()
plt.plot([x],[y],'o',color='cyan')
plt.plot([x[0]],[y[0]],'o',color='red')
#for i in range (82):
#	plt.plot(i,0,'o ',color='green')

def quit_figure(event):
	if event.key == 'q':
		plt.close(event.canvas.figure)
cid = plt.gcf().canvas.mpl_connect('key_press_event', quit_figure)
figure = plt.gcf()
figure.set_size_inches(16.80,4.57)
plt.savefig("g+e.png",dpi=100)
plt.show()
#plt.close(im)

