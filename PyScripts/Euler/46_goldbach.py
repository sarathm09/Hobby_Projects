__author__ = 'T90'
__version__ = '1.0.0'

import math


odd_c = []
prime = []


def genprime():
	for n in range(2, 10000):
		pr = True
		for i in xrange(2, n/2):
			if n % i == 0:
				pr = False
				break
		if pr:
			prime.append(n)


def odd_composite():
	for n in xrange(5, 10000):
		for i in xrange(2, n / 2):
			if n % i == 0 and n % 2 == 1:
				odd_c.append(n)
				break


def is_sq(a):
	for i in xrange(1, a):
		if i**2 == a:
			return True
	print 'dsfg',a
	return False


def check(n):
	for i in prime:
		if is_sq((n-i)/2):
			return True
	return False

genprime()
odd_composite()
for n in odd_c:
	if not check(n):
		print n