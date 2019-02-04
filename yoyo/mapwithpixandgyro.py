import sys
import pygame
import pygame as pg
import tty, sys, termios
import pygame.gfxdraw
from PIL import Image
from bstem.platform import AdCord
from gyro_calib import *
import threading

ad=AdCord()

pygame.init()

class ReadChar():
    def __enter__(self):
        self.fd = sys.stdin.fileno()
        self.old_settings = termios.tcgetattr(self.fd)
        tty.setraw(sys.stdin.fileno())
        return sys.stdin.read(1)
    def __exit__(self, type, value, traceback):
        termios.tcsetattr(self.fd, termios.TCSADRAIN, self.old_settings)


t=threading.Thread(target=kiran)
t.daemon=True
t.start()
                
def move(self):
	if (char) =='w' or ord(char)==56:
		print "Hooo"
				#pygame.draw.line(screen, (140, 140, 150), (300, 300), (50, 50))
				#a=a+1
				#c=c+1
				#print a
		e=e+1
		if (e%10 == 0):
			pygame.gfxdraw.filled_circle(screen,a+1,b,3, BLUE)
			pygame.display.flip()
			a=a+1
			r =r+10
			print ("You have moved (cm):", r)
	if (char) == "a":
		print "leftu"
		e=e+1
		if (e%10 == 0):
			
			pygame.gfxdraw.filled_circle(screen,a,b-1,3, BLUE)
			pygame.display.flip()
			b=b-1
			r =r+10
			print ("You have moved (cm):", r)
	if (char) =="d":
		print "Rightu"
		e=e+1
		if (e%10 == 0):
			pygame.gfxdraw.filled_circle(screen,a,b+1,3, BLUE)
			pygame.display.flip()
			b=b+1
			r =r+10
			print ("You have moved (cm):", r)
 
background= pygame.image.load("/home/ubuntu/Desktop/jarvis exclusive/yoyo/dada.png")
im = Image.open("/home/ubuntu/Desktop/jarvis exclusive/yoyo/dada.png")

pix = im.load()
#print im.size

backgroundRect = background.get_rect()

h=pygame.Surface.get_height(background)
print ("height=",h)

w=pygame.Surface.get_width(background)
print("width=",w)

#marker=pygame.image.load("/home/ragul/Bstem/marker.png")

print "Enter the initial position of the robot:"
x= input('Enter X:')
y= input('Enter Y:')

GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,153)

scalar=0.5
slow=0.3

a=x
b=y

e = 0
r = 0
k = 50
z = 5

g=12800/1287

size = (width, height) = background.get_size()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('CSE BLOCK MAP')
for i in range (1):
	for event in pygame.event.get():
		screen.blit(background, backgroundRect)
		#background.blit(marker,(x,y))
		pygame.gfxdraw.filled_circle(screen,x,y,2, RED)
		pygame.display.flip() 

while True:
	for event in pygame.event.get():
		screen.blit(background, backgroundRect)
		pygame.gfxdraw.filled_circle(screen,x,y,2, RED)
		#background.blit(marker,(x,y))
		for i in range (999999):
			with ReadChar() as rc:
				char = rc            	
			print(ord(char))
			gz=queue.get()
			if (char) =='w' or ord(char)==56:
				print "Hooo"
				ad.motor[0].speed=scalar
				ad.motor[2].speed=-scalar
				#pygame.draw.line(screen, (140, 140, 150), (300, 300), (50, 50))
				#a=a+1
				#c=c+1
				#print a
				e=e+1
				if (pix[a+z,b] != (255,255,255)):
					print ("U have an obstacle",k,"cm ahead of u")
					k = k-1
					if (k%10 == 0):
						z = z-1

					if (k == 0 or (pix[a,b] != (255,255,255))):
						print ("U have hit an obstacle :P")

				if(pix[a,b] != (255,255,255)):
						print ("U have hit an obstacle :P")

				if (e%2 == 0):
					
					pygame.gfxdraw.filled_circle(screen,a+1,b,2, BLUE,gz)
					pygame.display.flip()
					a=a+1
					r =r+10
					print ("You have moved (cm):", r)
					#if(pix[a,b] != (255,255,255)):
						#print ("U have hit an obstacle :P")

			if (char) == "a":
				print "leftu"
				e=e+1
				if(pix[a,b] != (255,255,255)):
						print ("U have hit an obstacle :P")
				if (e%2 == 0):
					ad.motor[0].speed=scalar
					ad.motor[2].speed=scalar
					pygame.gfxdraw.filled_circle(screen,a,b-1,2, BLUE,gz)
					pygame.display.flip()
					b=b-1
					r =r+10
					print ("You have moved (cm):", r)

			if (char) =="d":
				print "Rightu"
				e=e+1
				if(pix[a,b] != (255,255,255)):
						print ("U have hit an obstacle :P")
				if (e%2 == 0):
					ad.motor[0].speed=-scalar
					ad.motor[2].speed=-scalar
					pygame.gfxdraw.filled_circle(screen,a,b+1,2, BLUE,gz)
					pygame.display.flip()
					b=b+1
					r =r+10
					print ("You have moved (cm):", r)
			
			if (char) =="p":
				print "U are at (",a,b,") and u hav moved :",r ,"cm"
				#print "In the real time u ar at (",a*g,b*g,")"

			if (char) =='q':
				sys.exit()

		


    	if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


	pygame.display.flip() 

 

 #pygame.draw.line(screen, (140, 140, 150), (300, 300), (50, 50))
