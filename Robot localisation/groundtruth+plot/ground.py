f= open("eight_ground.txt",'r')
w= open("grnd.txt",'w',0)
c=0
x = []
y=[]
i=0
for val in f:
	reading = val.split(",")
	x.append(int(reading[0]))
	y.append(int(reading[1]))
	c=c+1
w.write(str(x[0])+","+str(y[0])+"\n")

while(i<c-1):#for i in range (c):																
	if(x[i] < x[i+1] and y[i]==y[i+1]):
		j = x[i+1] - x[i]
		sum1 = x[i]
		for q in range (j):
			sum1 = sum1 + 1	
			w.write(str(sum1) +","+ str(y[i])+ "\n")
	elif(x[i] > x[i+1] and y[i]==y[i+1]):
		j = x[i] - x[i+1]
		sum1 = x[i]
		for q1 in range (j):
			sum1 = sum1 -1
			w.write(str(sum1) + "," + str(y[i]) + "\n")
	elif(y[i] < y[i+1] and x[i]==x[i+1]):
		j = y[i+1] - y[i]
		sum1 = y[i]
		for q in range (j):
			sum1 = sum1 + 1	
			w.write(str(x[i]) + "," + str(sum1) + "\n")
	elif(y[i] > y[i+1] and x[i]==x[i+1]):
		j = y[i] - y[i+1]
		sum1 = x[i]
		for q1 in range (j):
			sum1 = sum1 -1
			w.write(str(x[i])+ "," + str(sum1)+ "\n")
	
	elif(x[i] < x[i+1] and y[i] < y[i+1]):
		j = abs(x[i+1] - x[i])
		k = abs(y[i+1] - y[i])
		sum1 = x[i]
		sum2 = y[i]
		maxi = max(j,k)
		for q in range (maxi):
			if(q<j and q>k):
				sum1 = sum1 +1	
				w.write(str(sum1) +","+ str(sum2)+ "\n")
			elif(q<k and q>j):
				sum2 = sum2 + 1
				w.write(str(sum1) +","+ str(sum2)+ "\n")
			else:
				sum1 = sum1 + 1
				sum2 = sum2 + 1
				w.write(str(sum1) +","+ str(sum2)+ "\n")

	elif(x[i] > x[i+1] and y[i] > y[i+1]):
		j = abs(x[i+1] - x[i])
		k = abs(y[i+1] - y[i])
		sum1 = x[i]
		sum2 = y[i]
		maxi = max(j,k)
		for q in range (maxi):
			if(q<j and q>k):
				sum1 = sum1 -1	
				w.write(str(sum1) +","+ str(sum2)+ "\n")
			elif(q<k and q>j):
				sum2 = sum2 - 1
				w.write(str(sum1) +","+ str(sum2)+ "\n")
			else:
				sum1 = sum1 - 1
				sum2 = sum2 - 1
				w.write(str(sum1) +","+ str(sum2)+ "\n")
				
	
	elif(x[i] < x[i+1] and y[i] > y[i+1]):
		j = abs(x[i+1] - x[i])
		k = abs(y[i+1] - y[i])
		sum1 = x[i]
		sum2 = y[i]
		maxi = max(j,k)
		for q in range (maxi):
			if(q<j and q>k):
				sum1 = sum1 +1	
				w.write(str(sum1) +","+ str(sum2)+ "\n")
			elif(q<k and q>j):
				sum2 = sum2 - 1
				w.write(str(sum1) +","+ str(sum2)+ "\n")
			else:
				sum1 = sum1 + 1
				sum2 = sum2 - 1
				w.write(str(sum1) +","+ str(sum2)+ "\n")

	elif(x[i] > x[i+1] and y[i] < y[i+1]):
		j = abs(x[i+1] - x[i])
		k = abs(y[i+1] - y[i])
		sum1 = x[i]
		sum2 = y[i]
		maxi = max(j,k)
		for q in range (maxi):
			if(q<j and q>k):
				sum1 = sum1 -1	
				w.write(str(sum1) +","+ str(sum2)+ "\n")
			elif(q<k and q>j):
				sum2 = sum2 + 1
				w.write(str(sum1) +","+ str(sum2)+ "\n")
			else:
				sum1 = sum1 - 1
				sum2 = sum2 + 1
				w.write(str(sum1) +","+ str(sum2)+ "\n")
	i=i+1

											
	
	

		
		 
		
		
		
	
