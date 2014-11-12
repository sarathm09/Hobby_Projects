from itertools import *
def arrange(n):
    i = 0
    l = []
    count = 0
    while 4*i < n:
        for i in xrange(0,i):
            l.append(4)
        for i in xrange(0,n-(4*i)):
            l.append(1)
        count += len(list(combinations(l,0)))
    print count, list(combinations(l,0)),l

arrange(0)
arrange(7)
            
