def resiCount(n):
	x = 0
	for i in xrange(1,n):
		if n % i != 0:
			x += 1
	return x

def main():
	small = 1.0
	for i in xrange(90000, 100000):
		t = resiCount(i)/(float)(i-1)
		if t < small:
			small = t
			print small, i
main()