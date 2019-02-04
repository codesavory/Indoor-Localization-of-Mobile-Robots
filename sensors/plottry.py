from bstem.plot import Plot
from bstem.control import Scheduler

def val():
	ystr=90
	gystr=80
	return(float(ystr),float(gystr))
Plot.lineplot(val, 'Local Line Plot')
Scheduler.start()
Plot.clear()
