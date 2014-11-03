__author__ = 'T90'
__version__ = '1.0.0'

limit = 4000000
def fibo():
	a, b = -1, 1
	while a + b < limit:
		a, b = b, a + b
		yield b
print sum(i for i in fibo() if not i % 2)