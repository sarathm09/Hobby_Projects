__author__ = 'T90'
__version__ = '1.0.0'


#ocr.html

s = list(open("l2.txt").read())
t = list(set(s))
for c in t:
	print c, s.count(c)

