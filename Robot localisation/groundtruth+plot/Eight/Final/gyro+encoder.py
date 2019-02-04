import plot_klaus_brenner as pkb
import math

#gyroscope
ang=0
theta = 0
p_dist=0
#p_ang =0
ticks_to_cm = (pkb.ticks_to_cm_l + pkb.ticks_to_cm_r)/2
#encoders
pose = (pkb.ix,pkb.iy,0)
last_ticks = None
first_motor_ticks = True
x=0
y=0
def calculate_ticks(l,r):
	ticks = ((l),(r))
	global first_motor_ticks,last_ticks
        if first_motor_ticks:
       		first_motor_ticks = False
       		last_ticks = ticks
        motor_ticks = ( tuple([(int(float(ticks[i])))-(int(float(last_ticks[i]))) for i in range(2)]))
        last_ticks = ticks
	return motor_ticks

w = open("newdata3.txt",'w')
r = open("(g+e)readings.txt",'r')

for val in r:
	reading = val.split(",")
	rc = reading[0]
	encoder=reading[1].split(" ")
	l=float(encoder[0])
	r=float(encoder[1])
	#global pose
	#global motor_ticks
	#global x
	#global y
	if rc =='w':#front
		motor_ticks = calculate_ticks(l,r)
		pose = pkb.filter_step(pose, motor_ticks)
		ang = pose[2] 
		#p_ang = ang
		#print ang
		#for gyroscope
		p_dist = (l+r)/2
		#print p_dist
		x = pose[0]
		y = pose[1]   
		#print(l,r)
		#print (x,y,ang*57.2957795)
		last_ticks = ((l),(r))
		#print (last_ticks)
		w.write(str(pose[0])+","+str(pose[1])+","+ str(ang*57.2957795)+"\n")#+","+'w'+","+str(l)+" "+str(r)+","+str(ang)+"\n")

	elif rc=='s':#back
		motor_ticks = calculate_ticks(l,r)
		pose = pkb.filter_step(pose, motor_ticks)
		ang = pose[2]
		#p_ang = ang
		print ang
		#for gyroscope
		p_dist = (l+r)/2
		#print p_dist
		x = pose[0]
		y = pose[1]
		w.write(str(pose[0])+","+str(pose[1])+","+ str(ang*57.2957795)+"\n")#+","+'s'+","+str(l)+" "+str(r)+","+str(ang)+"\n")

	elif rc=='a':#left
		#print reading[2]
		ang = ang + math.radians(float(reading[2]))
		
		dist=(l+r)/2
		r_dist = (dist-p_dist)*ticks_to_cm
		#print (dist,p_dist,r)
		p_dist=dist
		#print r_dist
		theta=ang#57.2957795
		#print ang*57.294
		x+= (r_dist*(math.cos(theta)))
		y+= (r_dist*(math.sin(theta)))
		#print(l,r)
		#for encoders
		#print(l,r)
		#print (x,y,ang*57.2957795)	
		last_ticks = ((l),(r))
		#print (last_ticks)
		#print ang
		pose = (x,y,ang)
		#print (x,y,ang)
		last_ticks = ((l),(r))
		#print (last_ticks)
		w.write(str(pose[0])+","+str(pose[1])+","+ str(ang*57.2957795)+"\n")#+","+'a'+","+str(l)+" "+str(r)+","+str(ang)+"\n")
	

	elif rc=='d':#right
		print reading[2]
		ang = ang + math.radians(float(reading[2]))
		dist=(l+r)/2
		r_dist = (dist-p_dist)*ticks_to_cm
		#print (dist,p_dist,r)
		p_dist=dist
		#print r_dist
		theta=ang#57.2957795
		#print(ang)
		#print ang
		x+= (r_dist*(math.cos(theta)))
		y+= (r_dist*(math.sin(theta)))
		#print(l,r)
		#for encoders
		pose = (x,y,ang)
		#print (x,y,ang*57.2957795)
		last_ticks = ((l),(r))
		#print (last_ticks)
		w.write(str(pose[0])+","+str(pose[1])+","+ str(ang*57.2957795)+"\n")#+","+'d'+","+str(l)+" "+str(r)+","+str(ang)+"\n")


	

