from bstem.platform import AdCord

ad=AdCord()
ad.gpio[0].direction = 'in'   # set gpio to read in a signal
while True:
	val = ad.gpio[0].value
	print(val)
