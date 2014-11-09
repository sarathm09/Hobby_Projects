__author__ = 'T90'
__version__ = '1.0.0'

from subprocess import call
import os
import re

fileName = "a.c"


def compile():
	a = os.popen("bcc32 " + fileName).read()
	errors = ["Could not find file", "Statement missing", "errors in Compile"]
	for error in errors:
		if error in a:
			print 'Please Check your file; The reported Errors are : \n'
			er = re.findall('Error .* ' + fileName + ' ([0-9]+: .*)\n', a)
			for e in er:
				print e
			return False
	return True


def run():
	print 'Program Successfully compiled!!!. Here is the result : \n\n'
	os.system(fileName.replace(".c", ""))

if compile():
	run()

