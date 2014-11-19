__author__ = 'T90'
__version__ = '1.0.0'


def gcd(a, b):
	while a != b:
		while a > b:
			a -= b
		while b > a:
			b -= a
	return a


def rad(val):
	pr = []
	i = 2
	p = 1
	while val != 1:
		while val % i == 0:
			val /= i
			pr.append(i)
		i += 1
	p = 1
	for n in set(pr):
		p *= n
	return p


def checks(a, b, c):
	abc = False
	if a < b:
		if a + b == c:
			if gcd(a, b) == 1 and gcd(c, b) == 1 and gcd(a, c) == 1:
				if rad(a * b * c) < c:
					abc = True
	return abc


def main():
	n = 120001
	k = 0
	for i in xrange(1, n):
		for j in xrange(i+1, n - i + 1):
			if checks(i, j, i+j):
				k += 1
	print k

main()