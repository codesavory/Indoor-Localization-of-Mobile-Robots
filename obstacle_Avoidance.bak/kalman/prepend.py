f = open("encoders.txt")
lines = f.readlines()
lines = ['M ' + line for line in lines] 
w = open("newkalmanangle.txt" , 'w' )
w.writelines(lines)  
