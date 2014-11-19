__author__ = 'T90'
__version__ = '1.0.0'

import re
import zipfile


l = []

def next(p):
	global z
	fname = 'channel/' + p + '.txt'
	text = open(fname, "r").read()
	m = re.findall('Next nothing is ([0-9]+)', text)
	l.append(z.getinfo(p + '.txt').comment)
	if len(m) == 0:
		print text
	else:
		next(m[0])

if __name__ == '__main__':
	z = zipfile.ZipFile('channel.zip')
	next('90052')
	print ''.join(l)
