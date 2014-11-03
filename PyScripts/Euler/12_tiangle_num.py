__author__ = 'T90'
__version__ = '1.0.0'


def triangle(n):
	sum = 0
	for i in xrange(1, n+1):
		sum += i
	return sum


def factor_count(n):
	count = 0
	for i in xrange(2, n+1):
		if n % i == 0:
			count += 1
	if count > 500:
		return True
	else:
		return False

for i in xrange(5000, 7000):
	t = triangle(i)
	if factor_count(t):
		print i, t
		break
