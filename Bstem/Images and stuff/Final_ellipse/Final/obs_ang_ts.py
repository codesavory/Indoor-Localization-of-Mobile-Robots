from itertools import izip
with open('obs_ang_ts.txt', 'w') as res, open('sensor_angle.txt') as f1, open('tstamp.txt') as f2:
    for line1, line2 in zip(f1, f2):
        res.write("{} {}\n".format(line1.rstrip(), line2.rstrip()))
