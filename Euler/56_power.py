max = 0
for a in xrange(1, 100):
	for b in xrange(1, 100):
		temp = sum([int(i) for i in list(str(a ** b))])
		if temp > max:
			max = temp
print max
