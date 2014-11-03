__author__ = 'T90'
__version__ = '1.0.0'

from itertools import count


def is_prime(n):
	prime = True
	for i in count(2, 1):
		if i > n/2:
			break
		if n % i == 0:
			prime = False
	return prime


def main():
	num = 2
	j = 4
	while num != 10001:
		j += 1
		if is_prime(j):
			num += 1
	print j

main()