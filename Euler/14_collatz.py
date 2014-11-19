__author__ = 'T90'
__version__ = '1.0.0'

maxval = 0
maxnum = 0
n = []

def travel(j):
	global maxval, maxnum
	tmp = j
	count = 1
	while j != 1:
		count += 1
		if j % 2 == 0:
			j /= 2
		else:
			j = 3 * j + 1
	if count > maxval:
		maxval = count
		maxnum = tmp
		print maxval, maxnum

for i in xrange(1000000, 50000, -1):
	travel(i)

print maxval, maxnum
