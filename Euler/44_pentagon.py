__author__ = 'T90'
__version__ = '1.0.0'


def func(n):
	return n * (3*n - 1)/2

penta = []

for i in xrange(1, 5000):
	penta.append(func(i))

for i in xrange(1, len(penta)+1):
	for j in xrange(i, len(penta)+1):
		if abs(i - j) in penta and abs(i + j) in penta:
			print i, j, i-j