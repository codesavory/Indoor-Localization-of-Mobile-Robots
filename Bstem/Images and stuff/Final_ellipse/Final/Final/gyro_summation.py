import gyro_calib as gc
import threading

e=threading.Thread(target=gc.gyro) #gyro thread
e.daemon=True
e.start()

def gyros():
	while True:
		gzs = gc.q.get()
