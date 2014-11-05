__author__ = 'T90'
__version__ = '1.0.0'


orig = (1, 2, 3, 4, 5)


def diff(a):
	c = 0
	for i in range(0, len(a)):
		if a[i] != orig[i]:
			c += 1
	if c == 0:
		c = 1
	return c


def rotate(strg, n):
	return strg[n:] + strg[:n]

def permute(a):
	print a
	t = ''
	if len(a) == 3:
		t = a[0]
		a[0] = t
		print a
	# 	t, a[0], a[2] = a[0], a[2], t
	# 	print a
	# 	t, a[1], a[2] = a[1], a[2], t
	# 	print a
	# 	rotate(a,1)
	# 	print a
	# 	rotate(a,-1)
	# 	print a
	else:
		permute(a[1:])



def main():
	permute('123')


if __name__ == '__main__':
    main()