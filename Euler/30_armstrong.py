__author__ = 'T90'
__version__ = '1.0.0'


def check(n):
	sum, val = 0, n
	while n > 0:
		t = n % 10
		t **= 5
		sum += t
		n /= 10
	if sum == val:
		return True
	else:
		return False


def main():
	tot = 0
	for i in xrange(0, 1000000):
		if check(i):
			print i
			tot += i

	print tot


main()
