r=open("agereadings.txt","r")
f=open("encoders.txt",'w')
sepFile = r.read().split('\n')
for ag in sepFile:
	reading=ag.split(',')
	encoder=reading[3].split(" ")
	f.write("M "+encoder[0]+" "+encoder[1]+"\n")
