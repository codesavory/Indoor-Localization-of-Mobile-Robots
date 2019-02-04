import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image

x=[]
y=[]

img = mpimg.imread('indoor.png')
imgplot = plt.imshow(img)

readFile = open('data.txt','r')
sepFile = readFile.read().split('\n')
readFile.close()

for plotpair in sepFile:
	XANDY = plotpair.split(',')
	if len(XANDY) > 1:
		x.append(int(XANDY[0]))
		y.append(int(XANDY[1]))

plt.plot([x],[y],'o',color='blue')

def quit_figure(event):
	if event.key == 'q':
		plt.close(event.canvas.figure)
cid = plt.gcf().canvas.mpl_connect('key_press_event', quit_figure)

plt.show()
