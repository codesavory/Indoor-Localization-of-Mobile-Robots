# Implement the first move model for the Lego robot.
# 02_a_filter_motor
# Claus Brenner, 31 OCT 2012
from math import * 
from pylab import *
from lego_robot import *
import numpy as np
from PIL import Image
import matplotlib.image as mpimg
import sys

# Measured width of the robot (wheel gauge), in cm.
robot_width = 54
# Empirically derived conversion from ticks to mm.
ticks_to_cm_l = 3.3536
ticks_to_cm_r = 3.2263#3.2070
#5.558772438
#Setting initial points
ix= 0#input('Enter X:')
iy= 0#input('Enter Y:')

# This function takes the old (x, y, heading) pose and the motor ticks
# (ticks_left, ticks_right) and returns the new (x, y, heading).
def filter_step(old_pose, motor_ticks):
	#img = mpimg.imread('map.png')
	#imgplot = plt.imshow(img)

	stlne =((motor_ticks[0]*ticks_to_cm_l - motor_ticks[1]*ticks_to_cm_r) )
   	#l= motor_ticks[0]
	#r= motor_ticks[1]
	#print "--------"
	#print stlne,motor_ticks

	#print (l,r)
    	# Find out if there is a turn at all.
	if  stlne==0:
		#print ((motor_ticks[0]* ticks_to_mm)*cos(old_pose[2])+old_pose[0],(motor_ticks[1]* ticks_to_mm)*sin(old_pose[2])+old_pose[1],old_pose[2])
		#print("straight")
	 	return((motor_ticks[0]* ticks_to_cm_l)*cos(old_pose[2])+old_pose[0],(motor_ticks[1]* ticks_to_cm_r)*sin(old_pose[2])+old_pose[1],old_pose[2])
 
        # --->>> Implement your code to compute x, y, theta here.
        #return (x, y, theta)

    	elif stlne < 0:#left turn
		#print("strlne :"+str(stlne))
		
		alpha=-((stlne)/robot_width)
		#print (ang)
		theta=old_pose[2]
		turn_rad = (motor_ticks[0]* ticks_to_cm_l) / (alpha) + robot_width/2
		#con=R+75
		#print (old_pose[2])
		cx=old_pose[0]-((turn_rad) * sin(theta))
		cy=old_pose[1]-(turn_rad * (-cos(theta)))
		#print motor_ticks[1]

		x=(cx+(turn_rad * sin(theta + alpha)))
		y=(cy+(turn_rad * -cos(theta + alpha)))
		#print(x, y, theta+alpha)
        # --->>> Implement your code to compute x, y, theta here.
		#print "left"
        	return (x, y, theta+alpha)
		
	else:#right turn
		#print("strlne :"+str(stlne))
		#print (l-r)
		alpha=-((stlne)/robot_width)
		#print (ang)
		theta=old_pose[2]
		#con=R+75
		#print (old_pose[2])
		turn_rad = (motor_ticks[1]* ticks_to_cm_r) / (-alpha) + robot_width/2
		cx=old_pose[0]-(turn_rad * (-sin(theta)))
		cy=old_pose[1]-(turn_rad * (cos(theta)))

		x=(cx+(turn_rad * (-sin(theta + alpha))))
		y=(cy+(turn_rad * (cos(theta + alpha))))
		
		#print(x, y, theta+alpha)
        # --->>> Implement your code to compute x, y, theta here.
		#print "right"
        	return (x, y, theta+alpha)

if __name__ == '__main__':

    '''readFile = open('newencoder.txt','r')
    sepFile = readFile.read().split('\n')
    readFile.close()'''

    # Read data.
    logfile = LegoLogfile()
    logfile.read("encoders.txt")

    print "Enter the initial position of the robot:"	

    f=open("newdata.txt","w",0)
    f.write(str(ix) + "," +str(iy) + "\n")

    # Start at origin (0,0), looking along x axis (alpha = 0).
    pose = (ix,iy, 0)#3.14159 = 180 degrees
    #f=open("newdata.txt","w",0)

    # Loop over all motor tick records generate filtered position list.
    filtered = []
    for ticks in logfile.motor_ticks:
        pose = filter_step(pose, ticks)
	#sys.stdin.read(1)
        f.write(str(pose[0])+","+str(pose[1])+","+str(pose[2]*57.2957795)+"\n")
        filtered.append(pose)
    f.close()
 	
    '''# Draw result.
    for pose in filtered:
        print pose
        plot([p[0] for p in filtered], [p[1] for p in filtered], 'bo')
    show()'''
