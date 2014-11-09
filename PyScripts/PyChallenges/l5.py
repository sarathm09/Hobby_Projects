__author__ = 'T90'
__version__ = '1.0.0'

import pickle

txt = pickle.load(open('banner.p', 'rb'))

for i in range(len(txt)):
	for j in range(len(txt[i])):
		for k in range(txt[i][j][1]):
			print txt[i][j][0],
