from time import sleep
import serial
import Queue
from gyro_calib import *
#import gyro_calib as m
from bstem.platform import AdCord

ser = serial.Serial('/dev/ttyACM1',9600)
ad1=AdCord()
scalar=0.35
#q=Queue.Queue()
re=0
turn_angle=0
new_turn_angle=0
'''turn_angle_a=0
new_turn_angle_a=0
turn_angle_d=0
new_turn_angle_d=0'''
while True:
	rc = ser.read()
	print rc #read the newest output from the arduino
	#print("Leftwheel:",-ad1.encoder[2].position*3.38)#left motor
	#print("Rightwheel:",ad1.encoder[0].position*3.38)#right motor
	#f.write(str(-ad1.encoder[2].position*3.38)+" "+str(ad1.encoder[0].position*3.38)+"\n")
	if rc =='w':#forward
		#print(rc)
		ad1.motor[0].speed=scalar #right motor 
		ad1.motor[2].speed=-scalar #left motor
		print("Going Straight")
	elif rc=='a':#left
		ad1.motor[0].speed=scalar
		ad1.motor[2].speed=scalar
		'''gyro()
		re=q.get()
		#print(re)
		turn_angle=re
		new_turn_angle=new_turn_angle + turn_angle
		print("Going left")
		print("The angle turned by the bot in left is",new_turn_angle)'''

		'''turn_angle_a=re
		new_turn_angle_a=new_turn_angle_a + turn_angle_a
		print("Going left")
		print("The angle turned by the bot in left is",new_turn_angle_a)
		turn_angle_d=0
		new_turn_angle_d=0'''
	elif rc=='d':#right
		ad1.motor[0].speed=-scalar
		ad1.motor[2].speed=-scalar
		'''gyro()
		re=q.get()
		turn_angle=re
		new_turn_angle=new_turn_angle + turn_angle
		print("Going right")
		print("The angle turned by the bot in right is",new_turn_angle)'''
		
		'''turn_angle_d=re
		new_turn_angle_d=new_turn_angle_d + turn_angle_d
		print("Going right")
		print("The angle turned by the bot in right is",new_turn_angle_d)
		turn_angle_a=0
		new_turn_angle_a=0'''
	elif rc=='s':#back
		ad1.motor[0].speed=-scalar
		ad1.motor[2].speed=scalar
