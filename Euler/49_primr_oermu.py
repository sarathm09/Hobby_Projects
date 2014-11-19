__author__ = 'T90'
__version__ = '1.0.0'

from itertools import permutations
prime = []


def genprime():
	for n in range(1000, 10000):
		pr = True
		for i in xrange(2, n / 2 + 1):
			if n % i == 0:
				pr = False
				break
		if pr:
			prime.append(n)

genprime()
sum2 = []
for a in prime:
	l = permutations(str(a))
	h = 0
	sum = 0
	for t in l:
		q = 0
		for el in t:
			q = q*10 + int(el)
		if q in prime:
			h += 1
			sum += q
		if h == 3:
			sum2.append(sum)
sum2.sort()
print set(sum2)