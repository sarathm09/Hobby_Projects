__author__ = 'T90'
__version__ = '1.0.0'

nums = [i for i in xrange(1, 101)]


def sum_of_square():
	return sum([i * i for i in nums])


def square_sums():
	return sum(nums) ** 2

print square_sums()-sum_of_square()