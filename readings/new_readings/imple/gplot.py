import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image

x=[]
y=[]

'''plt.title('Bstem Project')											#Setting the title
plt.xlabel('x label')
plt.ylabel('y label')

readFile = open('accelerometerz.txt','r')
sepFile = readFile.read().split('\n')
readFile.close()

for plotpair in sepFile:
	print (plotpair)
	y.append(int(float(plotpair)))'''

readFile = open('accelerometerzz.txt','r')
sepFile = readFile.read().split('\n')
readFile.close()

for plotpair in sepFile:
	XANDY = plotpair.split(',')
	if len(XANDY) > 1:
		x.append((float(XANDY[0])))
		y.append((float(XANDY[1])))

'''for i in range (8976):
	x.append(i)'''

#plt.clf()
plt.plot([x],[y],'o',color='blue')
plt.show()

