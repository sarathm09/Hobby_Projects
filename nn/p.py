
def process(A, B, C, M, N):
	for i in xrange(1, M):
	    for j in xrange(1, N):
	        if j % B[i] == 0:
	            A[j] = A[j] * C[i]%(10**9+7)
	for i in A:
		print i,


a = raw_input().split(' ')
N, M = int(a[0]), int(a[1])
A = [int(i) for i in raw_input().split(' ')]
B = [int(i) for i in raw_input().split(' ')]
C = [int(i) for i in raw_input().split(' ')]


process(A, B, C, M, N)