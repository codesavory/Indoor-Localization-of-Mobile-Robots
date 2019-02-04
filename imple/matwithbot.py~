import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import pygame
from PIL import Image
from gyro_calib import *
#from encoders import *
import tty, sys, termios
import math
import threading

'''pygame.init()
im = Image.open("indoor.png")			#getting the pixel of the map
pix = im.load()'''


#fig = plt.figure()
plt.title('Bstem Project')											#Setting the title
plt.xlabel('x label')
plt.ylabel('y label')

plt.xlim(xmin=0,xmax=1287)											#setting the co-ordinate system for the map
plt.ylim(ymin=0,ymax=658)

img = mpimg.imread('indoor.png')		#Reading image for the map
imgplot = plt.imshow(img)

print "Enter the initial position of the robot:"	
#Setting initial points
ix= input('Enter X:')
iy= input('Enter Y:')


g=threading.Thread(target=gyro) 		#gyro thread
g.daemon=True
g.start()

plt.plot([ix],[iy],'o',color='r')

#fig=plt.gcf()
#fig.savefig('newmap.png')
#plt.ion()
#plt.show()
p_dist=0
p_ang=0
scalar=0.3
def quit_figure(event): #key press to close plot
		if event.key == 'q':
        		plt.close(event.canvas.figure)
		elif event.key == 'w':#forward
			ad.motor[1].speed=scalar #right motor 
			ad.motor[3].speed=-scalar #left motor
		elif event.key == 'a':#left
			ad.motor[1].speed=scalar #right motor 
			ad.motor[3].speed=scalar #left motor
		elif event.key == 'd':#right
			ad.motor[1].speed=-scalar #right motor 
			ad.motor[3].speed=-scalar #left motor
		elif event.key == 's':#backward
			ad.motor[1].speed=-scalar #right motor 
			ad.motor[3].speed=scalar #left motor
		elif event.key == ' ':#stop
			ad.motor[1].speed=0 #right motor 
			ad.motor[3].speed=0 #left motor
			plt.show()
	
while True:
	cid = plt.gcf().canvas.mpl_connect('key_press_event', quit_figure)
	gz=q.get()
	dist=(((-ad.encoder[2].position*3.38)+(ad.encoder[1].position*3.38))/2)-p_dist
	ang=math.radians(gz)-p_ang
	k=dist*math.sin(ang)+ix
	l=dist*math.cos(ang)+iy
	img = mpimg.imread('indoor.png')		#Reading image for the map
	imgplot = plt.imshow(img)
	plt.plot([k],[l],'o',color='blue')
	fig.savefig('newmap.png')
	p_dist=dist
	p_ang=ang
	#plt.draw()
	#time.sleep(0.05)
#plt.show()
'''x = []
y = []

readFile = open('/home/ragul/Bstem/matplotlib/sample.txt','r')		#opening file to read
sepFile = readFile.read().split('\n')
readFile.close()

for plotpair in sepFile:
	xAndy = plotpair.split(',')
	if len(xAndy) > 1:
		x.append(int(xAndy[0]))
		y.append(int(xAndy[1]))

print x
print(len(x))
u=len(x)
plt.plot([x],[y],'o',color='blue')

for i in range (u):													#pixel checking condition											
	if (pix [x[i],y[i]]) != (255,255,255):
		print ("U have hit an obstacle")

def quit_figure(event):												#key press to close plot
    if event.key == 'q':
        plt.close(event.canvas.figure)

cid = plt.gcf().canvas.mpl_connect('key_press_event', quit_figure)'''
