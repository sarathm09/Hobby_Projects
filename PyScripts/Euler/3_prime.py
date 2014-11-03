__author__ = 'T90'
__version__ = '1.0.0'

def largest(n):
	for i in xrange(2, 6000):
		while n % i == 0:
			print n
			n //= i
			print n
		if n == i:
			break
	print n

largest(600851475143)
