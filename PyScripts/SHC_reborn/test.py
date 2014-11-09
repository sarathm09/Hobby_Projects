__author__ = 'T90'
__version__ = '1.0.0'

import json

fp = open("dict.json", "r")
j = json.load(fp)
for a in j:
	print "\n Module " + a + " : "
	for b in str(j[a]).split(','):
		print b,", "