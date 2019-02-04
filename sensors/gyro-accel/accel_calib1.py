from bstem.platform import AdCord

ad=AdCord()
min_accel = 0.05
def accelo():#calibrating accel in x and y
	accel= ad.accelerometer
	if (accel.x >= min_accel or accel.x <= -min_accel):#returning only those values that are above a minimum threshold, treating below this threshold as noise
		if (accel.y >= min_accel or accel.y <= -min_accel):
			return (accel.x,accel.y,accel.z)
		else:
			return (accel.x,0,accel.z)
	elif (accel.y >= min_accel or accel.y <= -min_accel):#returning only those values that are above a minimum threshold, treating below this threshold as noise
		if (accel.x >= min_accel or accel.x <= -min_accel):
			return (accel.x,accel.y,accel.z)
		else:
			return (0,accel.y,accel.z)
	else:
		return (0,0,accel.z)

if __name__ == "__main__":
	while(True):
		acl = accelo()
		print(acl)
