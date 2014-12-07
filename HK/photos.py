__author__ = 'T90'
__version__ = '1.0.0'

from operator import methodcaller
import urllib

def download():
	f = open('fin.csv', 'r').read().split("\n")
	ids = map(methodcaller('split',', '), f)
	url = "http://www.rajagiritech.ac.in/stud/Photo/"
	for i in ids:
		urllib.urlretrieve(url + i[0] + ".jpg", "files/" + i[0] + ".jpg")
		print "Completed : " + i[0]
	print 'Success!!!'

if __name__ == "__main__":
	download()