__author__ = 'T90'
__version__ = '1.0.0'

for i in xrange(1, 10000):
	for j in xrange(1, 500):
		for k in xrange(1, 500):
			pan = True
			pan2 = False
			s = str(i) + str(j) + str(k)
			if len(s) == 9:
				for t in xrange(1, 10):
					if str(t) not in s:
						pan = False
				if pan:
					if i * j == k or k * j == i or i * k == j:
						pan2 = True
			if pan and pan2:
				print i, j, k