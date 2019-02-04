ticks_to_cm_l = 3.3536
ticks_to_cm_r = 3.2263#3.2070

r = open("raw_encoders.txt",'r')
#w = open("encoder_ticks.txt",'w',0)
for f in r:
	encoder = f.split(" ")
	print (str(float(encoder[0])*ticks_to_cm_l) +" "+str(float(encoder[1])*ticks_to_cm_r))
