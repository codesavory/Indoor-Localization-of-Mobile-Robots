from itertools import izip
with open('bothgyroandencoder.txt', 'w') as res, open('encodersang.txt') as f1, open('gyroangle.txt') as f2:
    for line1, line2 in zip(f1, f2):
        res.write("{} {}\n".format(line1.rstrip(), line2.rstrip()))
