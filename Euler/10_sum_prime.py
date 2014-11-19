__author__ = 'T90'
__version__ = '1.0.0'

l = [i for i in xrange(2, 2000001)]
j = 1
for a in l:
	j = 1 - j
	if j == 0:
		if a != 2:
			l.remove(a)

print len(l)

for i in xrange(2, 100000):
	for n in l:
		if i < n/2 and n % i == 0:
			l.remove(n)
			break
	print len(l)
print sum(l)