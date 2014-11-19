__author__ = 'T90'
__version__ = '1.0.0'


import re

s = open("l3.txt").read()

ansReg = re.compile("[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]")

print ''.join(ansReg.findall(s))