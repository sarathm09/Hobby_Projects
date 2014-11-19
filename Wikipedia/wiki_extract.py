import re

__author__ = 'T90'
__version__ = '1.0.0'

import urllib2
from BeautifulSoup import BeautifulSoup
import re


def cleanhtml(raw_html):
	cleanr = re.compile('<.*?>')
	cleantext = re.sub(cleanr, '', raw_html)
	return cleantext


def main():
	while True:
		search = raw_input("Enter the keyword : ")
		url = 'http://en.wikipedia.org/w/index.php?search=' +search.replace(' ','+') + '&title=Special%3ASearch&go=Go';
		brks = '\[\d*\]'
		br = re.compile(brks)
		b = BeautifulSoup(urllib2.urlopen(url).read().replace('<.?table.?>{.*}</table>',''))
		p = b.findAll("p")
		if len(p) < 2 or "may refer to" in p[0]:
			print "Oops, exact match not found, please try again.. "
			continue
		data = ""
		for item in p:
			text2 = cleanhtml(str(item))
			text2 = re.sub(br, '', text2)
			data += text2 + "\n\t"
			if len(data) > 1500:
				break
		print "\n\t" + data

		q = raw_input("Enter q to quit : ")
		if q == 'q':
			break


if __name__ == "__main__":
	main()