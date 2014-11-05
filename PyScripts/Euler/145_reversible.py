__author__ = 'T90'
__version__ = '1.0.0'


def revsum(n):
	return n + int(str(n)[::-1])


def check(n):
	for i in str(n):
		if int(i) % 2 == 0:
			return False
	return True


def main():
	n = 0
	i = 0
	while i < 1000000000:
		i += 1
		if str(i)[len(str(i)) - 1] != '0':
			if check(revsum(i)):
				n += 1
	print n


main()