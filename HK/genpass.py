__author__ = 'T90'
__version__ = '1.0.0'

from itertools import permutations
import string
chars = list(string.ascii_lowercase + string.digits)


def perm(n):
	pas = []
	l = permutations(chars, n)
	for p in l:
		pas.append(''.join(str(p)))
	print len(pas)

if __name__ == '__main__':
    perm(7)