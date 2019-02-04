import pygame.gfxdraw
from PIL import Image

black=(0,0,0,255)
white=(255,255,255,255)

m = open("coordinates.txt",'w',0)

im=Image.open("gyroscope.png")
pix = im.load()
w = im.size #width and height of image
a=w[0]
b=w[1]
print w
for i in range (a):
	for j in range (b):
		#if(pix[i,j]!=blue):
			#print pix[i,j]
		if(pix[i,j]!=black and pix[i,j]!=white and pix[i,j][1]<30):
			m.write(str(i)+","+ str(j) +"\n")
			#print (pix[i,j][1])
