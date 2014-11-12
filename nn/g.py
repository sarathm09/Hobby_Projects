def gcd(a, b):
	sm, lg = a, b
	if b < a:
		sm, lg = b, a
	for i in xrange(lg, 0, -1):
		if a%i == 0 and b%i == 0:
			break
	return i


def process(l):
	if len(l) == 1:
		return l[0]
	elif len(l) == 2:
		return gcd(l[0], l[1])
	else:
		while len(l)>2:
			l[0:2] = [gcd(l[0], l[1])]
        return gcd(l[0], l[1])

def main():
	n = input()
	for i in xrange(0, n):
		m = input()
		l = [int(h) for h in raw_input().split(' ')]
		if process(l) == 1:
			print 'YES'
		else:
			print 'NO'

main()