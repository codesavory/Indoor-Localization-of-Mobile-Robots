                # Implement the first move model for the Lego robot.
# 02_a_filter_motor
# Claus Brenner, 31 OCT 2012
from math import * 
from pylab import *
from lego_robot import *
import numpy as np
import matplotlib.image as mpimg

array = []
i=0

# This function takes the old (x, y, heading) pose and the motor ticks
# (ticks_left, ticks_right) and returns the new (x, y, heading).
def filter_step(old_pose, motor_ticks, ticks_to_cm_l,ticks_to_cm_r, robot_width):
        #img = mpimg.imread('map.png')
        #imgplot = plt.imshow(img)

        stlne =(motor_ticks[0]*ticks_to_cm_l -motor_ticks[1]*ticks_to_cm_r)
        l= motor_ticks[0]
        r= motor_ticks[1] 
        
        #print (l,r)
    # Find out if there is a turn at all.
        if  stlne == 0:
                #print ((motor_ticks[0]* ticks_to_mm)*cos(old_pose[2])+old_pose[0],(motor_ticks[1]* ticks_to_mm)*sin(old_pose[2])+old_pose[1],old_pose[2])
                global i
                i=i+1
                #print i
                return((motor_ticks[0]* ticks_to_cm_l)*cos(old_pose[2])+old_pose[0],(motor_ticks[1]* ticks_to_cm_r)*sin(old_pose[2])+old_pose[1],array[i])
 
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
                global i
                i=i+1
                #print i
                return (x, y, array[i])
                
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

                x=(cx+(turn_rad * (-sin(theta))))
                y=(cy+(turn_rad * (cos(theta))))
                
                #print(x, y, theta+alpha)
        # --->>> Implement your code to compute x, y, theta here.
                global i
                i=i+1
                #print i
                return (x, y,array[i])

if __name__ == '__main__':
    # Empirically derived conversion from ticks to mm.

    '''readFile = open('newencoder.txt','r')
    sepFile = readFile.read().split('\n')
    readFile.close()'''

    # Measured width of the robot (wheel gauge), in mm.
    ticks_to_cm_l = 3.3536
    ticks_to_cm_r = 3.2263
    robot_width=54	

    # Read data.
    logfile = LegoLogfile()
    logfile.read("encoders.txt")

    print "Enter the initial position of the robot:"    
    #Setting initial points
    ix= input('Enter X:')
    iy= input('Enter Y:')
    f=open("new.txt","w",0)
    f.write(str(ix) + "," +str(iy) + "\n")
    b=0
    with open("kalmanangle.txt", "r") as ins:
            global array
            for line in ins:
                array.append(float(line))
                b=b+1

    # Start at origin (0,0), looking along x axis (alpha = 0).
    global i
    global array
    #print b
    #print array[i]+1.0
    pose = (ix,iy, array[i])
    #f=open("newdata.txt","w",0)

    # Loop over all motor tick records generate filtered position list.
    filtered = []
    for ticks in logfile.motor_ticks:
        pose = filter_step(pose, ticks, ticks_to_cm_l,ticks_to_cm_r, robot_width)
        f.write(str(pose[0])+","+str(pose[1])+ "\n")
        filtered.append(pose)
        if i == 6700:
                break
    f.close()
        
    '''# Draw result.
    for pose in filtered:
        #print pose
        plot([p[0] for p in filtered], [p[1] for p in filtered], 'bo')
    show()'''
