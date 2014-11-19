__author__ = 'T90'
__version__ = '1.0.0'


def ispali(n):
	return str(n) == str(n)[::-1]

l = []
for i in xrange(999, 100, -1):
	for j in xrange(999, 100, -1):
		pr = i*j
		if ispali(pr):
			l.append(pr)

l.sort()
print l
