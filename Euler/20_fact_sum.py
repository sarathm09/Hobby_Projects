__author__ = 'T90'
__version__ = '1.0.0'


def fact(n):
	if n == 1:
		return 1
	else:
		return n * fact(n-1)


def main():
	print sum([int(i) for i in list(str(fact(100)))])


main()