__author__ = 'T90'
__version__ = '1.0.0'


def is_triplet(i, j, k):
	if i**2 == j**2 + k**2 or j ** 2 == i ** 2 + k ** 2 or k ** 2 == j ** 2 + i ** 2:
		return True
	else:
		return False


for i in xrange(1, 1000):
	for j in xrange(i, 500):
		for k in xrange(j, 500):
			if i + j + k == 1000:
				if is_triplet(i, j, k):
					print i,j,k,i*j*k