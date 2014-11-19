__author__ = 'T90'
__version__ = '1.0.0'

sum = 0
for i in xrange(1, 1001):
	print i
	sum += i**i

a = str(sum)
print a[-10:]
