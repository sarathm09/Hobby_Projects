# source: Internet
def r(a):
  i = a.find('0')
  ~i or exit(a)
  [m in[(i-j)%9*(i/9^j/9)*(i/27^j/27|i%9/3^j%9/3)or a[j]for j in range(81)] or r(a[:i]+m+a[i+1:])for m in'%d'%5**18]
from sys import *
r(argv[1])


# inp: 530070000600195000098000060800060003400803001700020006060000280000419005000080079