__author__ = 'T90'
__version__ = '1.0.0'

import urllib
import re

nothing = '82682'

nothin = re.compile('nothing is ([0-9]*)')


while nothing.isdigit():
	txt = urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + nothing).read()
	n = nothin.findall(txt)
	nothing = n[0]
	print txt
	if nothing == '16044':
		nothing = str(int(nothing)/2)