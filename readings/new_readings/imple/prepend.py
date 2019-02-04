f = open("encoders.txt")
lines = f.readlines()
lines = ['M ' + line for line in lines] 
w = open("newencoder.txt" , 'w' )
w.writelines(lines)  
