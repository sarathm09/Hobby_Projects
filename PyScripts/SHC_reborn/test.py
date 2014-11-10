__author__ = 'T90'
__version__ = '1.0.0'

import json
import re

fp = open("data/dict.json", "r")
j = json.load(fp)
# for a in j:
# 	print "\n Module " + a + " : "
# 	for b in str(j[a]).split(','):
# 		print b,", ",

word = raw_input("\nWord : ")
while word != "exit":
	for a in j:
		if word in j[a]:
			temp = open("data/" + a + ".txt").read()
			word = word.replace(" ", "").replace("\n", "")
			reg = "##" + word + "##\n" + "(.*)" + "\n##" + word + "##"
			code = re.findall(reg, temp, re.MULTILINE | re.DOTALL)
			print code[0]
			break
	word = raw_input("\nWord : ")
