__author__ = 'T90'
__version__ = '1.0.0'
prime = []


def genprime():
	for n in range(2, 800000):
		pr = True
		for i in xrange(2, n / 2 + 1):
			if n % i == 0:
				pr = False
				break
		if pr:
			prime.append(n)



def check(n):
	l = len(str(n))
	i = 1
	while i < l:
		if int(str(n)[i:]) not in prime or int(str(n)[:-1*i]) not in prime:
			return False
		i += 1
	return True

sum = 0
genprime()
print prime
for i in prime:
	if check(i) and i > 10:
		print i
		sum += i

print sum, "*"