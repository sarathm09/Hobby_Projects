__author__ = 'T90'
__version__ = '1.0.0'


def fibo():
	c = 0
	a, b = 1, 1
	n = 2
	while len(str(c)) < 1000:
		c = a + b
		a, b = b, c
		n += 1
	return n

print fibo()