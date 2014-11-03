from fractions import gcd

__author__ = 'T90'
__version__ = '1.0.0'

l = [i for i in xrange(1, 25)]


def gcd(a, b):
	sm, lg = a, b
	if b < a:
		sm, lg = b, a
	for i in xrange(lg, 0, -1):
		if a%i == 0 and b%i == 0:
			break
	return i


def lcm(a, b):
	return (a*b)/gcd(a,b)


while len(l) > 1:
	a, b = l[0], l[1]
	l.remove(a)
	l.remove(b)
	l.append(lcm(a, b))

print l[0]