def isfibo(n):
	a, b = 0, 1
	while True: 
		if n == a:
			return True
		if a > n:
			return False
		a, b = b, a+b


n = input()
for i in xrange(0, n):
	if isfibo(input()):
		print 'IsFibo'
	else:
		print 'IsNotFibo'