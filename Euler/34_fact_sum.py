f = []

def fact():
	for n in xrange(0,10):
		fa = 1
		while n > 0:
			fa *= n
			n -= 1
		f.append(fa)

def get_fact_sum(n):
	l = [int(i) for i in str(n)]
	l = [f[i] for i in l]
	sum = 0
	for a in l:
		sum += a
	return sum

fact()
sum = 0
for i in xrange(3, 1000000):
	if i == get_fact_sum(i):
		sum += i

print "sum = ",sum