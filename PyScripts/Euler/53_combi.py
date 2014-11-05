result = 0;
limit = 1000000;
rows = 100;
 
pTriangle = [[1 for i in xrange(0, rows+2)] for a in range(0, rows+2)]


for n in xrange(2, rows+1):
	for r in xrange(2, n+1):
		pTriangle[n][r] = pTriangle[n-1][r] +  pTriangle[n-1][r-1]
		if pTriangle[n][r] > limit:
			pTriangle[n][r] = limit
			result += 1

print result