__author__ = 'T90'
__version__ = '1.0.0'

def traverse(n, i, j):
	if i == n or j == n:
		return 1
	else:
		return traverse(n, i + 1, j) + traverse(n, i, j + 1)

print traverse(20, 0, 0)