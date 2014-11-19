__author__ = 'T90'
__version__ = '1.0.0'

from itertools import permutations


def permu():
	num = "012"
	p = permutations(range(10))
	n = 0
	for i in p:
		n += 1
		if n == 1000000:
			print str(i).replace(', ','')


permu()