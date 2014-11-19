__author__ = 'T90'
__version__ = '1.0.0'

l = []

for i in xrange(2,101):
	for j in xrange(2,101):
		l.append(i**j)
print len(set(l))