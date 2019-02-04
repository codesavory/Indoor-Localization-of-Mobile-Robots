import sys
import pygame
import pygame as pg
import tty, sys, termios
import pygame.gfxdraw
from bstem.platform import AdCord
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
WHITE=(255,255,255)
scalar=0.5
slow=0.3
a=x
b=y

e = 0
r = 0

g=12800/1287

size = (width, height) = background.get_size()
screen = pygame.display.set_mode(size)

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
			if (char) =='w' or ord(char)==56:
				print "Hooo"
				ad.motor[0].speed=scalar
				ad.motor[2].speed=-scalar
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
					ad.motor[0].speed=scalar
					ad.motor[2].speed=scalar
					pygame.gfxdraw.filled_circle(screen,a,b-1,3, BLUE)
					pygame.display.flip()
					b=b-1
					r =r+10
					print ("You have moved (cm):", r)

			if (char) =="d":
				print "Rightu"
				e=e+1
				if (e%10 == 0):
					ad.motor[0].speed=-scalar
					ad.motor[2].speed=-scalar
					pygame.gfxdraw.filled_circle(screen,a,b+1,3, BLUE)
					pygame.display.flip()
					b=b+1
					r =r+10
					print ("You have moved (cm):", r)

			if (char) =="s":
				print "Baackuu"
				e=e+1
				if (e%10 == 0):
					ad.motor[0].speed=-scalar
					ad.motor[2].speed=scalar
					pygame.gfxdraw.filled_circle(screen,a-1,b,3, WHITE)
					pygame.display.flip()
					a=a+1
					r =r+10
					print ("You have moved (reverse -cm):", r)
			
			if (char) =="p":
				print "U are at (",a,b,") and u hav moved :",r ,"cm"
				#print "In the real time u ar at (",a*g,b*g,")"

			if (char) =='q':
				sys.exit()
			if (char) == 'null':
				ad.motor[0].speed=0
				ad.motor[2].speed=0

    	if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

	pygame.display.flip() 

 

 #pygame.draw.line(screen, (140, 140, 150), (300, 300), (50, 50))
