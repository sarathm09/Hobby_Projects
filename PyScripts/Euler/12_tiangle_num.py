__author__ = 'T90'
__version__ = '1.0.0'

# from itertools import count
#
# def triangle(_):
# 	return _*(_+1)/2
#
#
# def factor_count(n):
# 	c = 0
# 	for i in count(1, 1):
# 		if i > n:
# 			break
# 		if n % i == 0:
# 			c += 1
# 	print n, c
# 	if c > 500:
# 		return True
# 	else:
# 		return False
#
# def t1():
# 	i = 1000000
# 	while True:
# 		if factor_count(triangle(i)):
# 			print i, triangle(i)
# 			break
# 		i -= 1
#
#
# def t2():
# 	for i in xrange(9000, 10000):
# 		if factor_count(triangle(i)):
# 			print i, triangle(i)
# 			break
#
# t1()
# # tt1 = Thread(target=t1)
# # tt2 = Thread(target=t2)
# #
# # tt1.start()
# # #tt2.start()

import math
import operator


def find_sum(n):
	return n * (n + 1) / 2


def find_num_divisor(num, primes):
	next_prime = primes[0]
	num_divisor = 1
	prime_count = 1
	while next_prime <= num:
		exponent = 0
		while num % next_prime == 0:
			num /= next_prime
			exponent += 1
		exponent += 1
		num_divisor *= exponent
		next_prime = primes[prime_count]
		prime_count += 1
	return num_divisor


def return_n_primes(n, primes=None):
	'''
	Merge the set of n prime numbers or extend the given primes' set

	Input:
		n - number of prime numbers
		primes - list of prime numbers that are already curated. If it is
		None start from scratch

	Output:
		primes - set of n prime numbers
	'''

	if primes == None:
		counter = 0
		cur_val = 2
		primes = []
	else:
		cur_val = primes[-1]
		counter = len(primes)
	while counter < n:
		if check_prime(cur_val):
			primes.append(cur_val)
			counter += 1
		cur_val += 1
	return primes


def check_prime(num):
	'''
	Check whether the given number is prime or not

	Iterate over all the values in the interval [2, sqrt(num)], if no
	exact divisor is found then raise the number as prime.
	'''
	if num == 1:
		return False
	check_val = int(math.floor(math.sqrt(num)))
	for i in range(check_val, 1, -1):
		if num % i == 0:
			return False
	return True


if __name__ == '__main__':
	LIM = 500
	num_divisors = 0
	primes = return_n_primes(500)
	next_tri_val = 1
	while num_divisors < LIM:
		# find the next triangle number
		tri_val = find_sum(next_tri_val)
		try:
			# find number of divisors, if primes' set is short than extend it
			num_divisors = find_num_divisor(tri_val, primes)
			next_tri_val += 1
		except:
			# if primes list is not enough extend it
			return_n_primes(len(primes) + 100, primes)
		print 'num divisors ', num_divisors
	print tri_val