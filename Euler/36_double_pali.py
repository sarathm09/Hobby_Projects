
def check_pali(n):
	return str(n) == str(n)[::-1]

def convert(n):
	bin = []
	while n > 0:
		bin.append(n % 2)
		n /= 2
	return bin[::-1]

n = 0
for i in xrange(1, 1000000):
	if check_pali(i):
		if i % 10 == 0:
			print i
		ch = ''.join([str(c) for c in convert(i)])
		if check_pali(int(ch)):
			n += i
print n
