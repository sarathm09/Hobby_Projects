__author__ = 'T90'
__version__ = '1.0.0'

import urllib2 as ulib
from BeautifulSoup import BeautifulSoup


def problem(n):
	url = "https://projecteuler.net/problem=" + str(n)
	u = ulib.urlopen(url)
	data = u.read()
	soup = BeautifulSoup(data)
	h2 = soup.find('h2')
	div = soup.find('div', attrs={'class': 'problem_content'})
	file = open("questions.html", "a")
	content = "<hr/><br/><h1> Problem : " + str(n) + "</h1>" + str(h2) + str(div)
	file.write(content)
	file.close()

for i in xrange(1, 480):
	problem(i)