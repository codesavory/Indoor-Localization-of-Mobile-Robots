import tty, sys, termios
from bstem.platform import AdCord

ad1=AdCord()
class ReadChar():
    def __enter__(self):
        self.fd = sys.stdin.fileno()
        self.old_settings = termios.tcgetattr(self.fd)
        tty.setraw(sys.stdin.fileno())
        return sys.stdin.read(1)
    def __exit__(self, type, value, traceback):
        termios.tcsetattr(self.fd, termios.TCSADRAIN, self.old_settings)

f=open('encoders.txt','w')
def erun():
    stscalar=0.3
    scalar=0.5
    newscalar=0.1
    while True:
        with ReadChar() as rc:
            char = rc
	#print(ord(char))
	print("Leftwheel:",-ad1.encoder[2].position*3.38)#left motor
	print("Rightwheel:",ad1.encoder[0].position*3.38)#right motor
	f.write('M '+str(-ad1.encoder[2].position*3.38)+" "+str(ad1.encoder[0].position*3.38)+"\n")
	if (char) =='w' or ord(char)==56:#forward
		#print((char))
		ad1.motor[0].speed=stscalar #right motor 
		ad1.motor[2].speed=-stscalar #left motor
	elif (char)=='a' or ord(char)==52:#left
		ad1.motor[0].speed=scalar
		ad1.motor[2].speed=-newscalar
	elif (char)=='d' or ord(char)==54:#right
		ad1.motor[0].speed=newscalar
		ad1.motor[2].speed=-scalar
	elif (char)=='s' or ord(char)==53:#back
		ad1.motor[0].speed=-stscalar
		ad1.motor[2].speed=stscalar
	elif ord(char)==32:#stop
		ad1.motor[0].speed=0
		ad1.motor[2].speed=0
	if ord(char)==43:#increase speed
		scalar+=0.10
	elif ord(char)==45:#decrease speed
		scalar-=0.10		
	if char in "x" or ord(char)==27:#exit
            sys.exit()

if __name__ == "__main__":
    erun()
