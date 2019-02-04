import sys
import pygame
import pygame as pg
import tty, sys, termios
import pygame.gfxdraw
from PIL import Image
from bstem.platform import AdCord
from gyro_calib import *
from run1 import *
import threading
import math

adz=AdCord()
def map(k,l):
	for event in pygame.event.get():
		#screen.blit(background, backgroundRect)
		pygame.gfxdraw.filled_circle(screen,int(k),int(l),2, BLUE)
		pygame.display.flip()

if __name__ == "__main__":
	background= pygame.image.load("/home/ubuntu/Desktop/jarvis exclusive/integration/dada.png")
	im = Image.open("/home/ubuntu/Desktop/jarvis exclusive/integration/dada.png")
	pix = im.load()
	#print im.size
	backgroundRect = background.get_rect()
	h=pygame.Surface.get_height(background)
	print ("height=",h)
	w=pygame.Surface.get_width(background)
	print("width=",w)
	print "Enter the initial position of the robot:"
	x= input('Enter X:')
	y= input('Enter Y:')
	GREEN = (0,255,0)
	RED = (255,0,0)
	BLUE = (0,0,153)
	size = (width, height) = background.get_size()
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption('CSE BLOCK MAP')
	for i in range (1):
		for event in pygame.event.get():
			screen.blit(background, backgroundRect)
			#background.blit(marker,(x,y))
			pygame.gfxdraw.filled_circle(screen,x,y,2, RED)
			pygame.display.flip()

	g=threading.Thread(target=gyro) #gyro thread
	g.daemon=True
	g.start()

	e=threading.Thread(target=test) #erun thread
	e.daemon=True
	e.start()
	
	p_dist=0
	p_ang=0
	#flag=0	
	while True:
		gz=q.get()
		dist=(((-adz.encoder[2].position*3.38)+(adz.encoder[1].position*3.38))/2)-p_dist
		#print("Left:"+str(-ad1.encoder[2].position*3.38))
		#print("Right:"+str(ad1.encoder[1].position*3.38))
		#print(dist)
		ang=(math.radians(gz))-p_ang
		k=((-dist*(math.sin(ang))/10)+x)
		l=(((dist*(math.cos(ang)))/10)+y)
		map(k,l)#send in pixels
		p_dist=dist
		p_ang=ang	
