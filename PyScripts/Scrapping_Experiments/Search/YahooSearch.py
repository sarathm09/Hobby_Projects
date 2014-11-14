__author__ = 'T90'
__version__ = '1.0.0'

__author__ = 'T90'
__version__ = '1.0.0'

import mechanize
from BeautifulSoup import BeautifulSoup
import re


def searchhtml(keyword):
	moz = mechanize.Browser()
	moz.set_handle_robots(False)
	moz.addheaders = [('User-agent',
						  'Mozilla/5.0 (Windows NT 6.2; rv:33.0) Gecko/20100101 Firefox/33.0')]

	base_url = "https://search.yahoo.com/search?p="
	search_url = base_url + keyword.replace(' ', '+')

	return moz.open(search_url).read() + moz.open(search_url + "&b=11").read() + \
			moz.open(search_url + "&b=21").read()


def getlinks(keyword):
	results = []
	html = searchhtml(keyword)
	bs = BeautifulSoup(html).findAll('div', attrs={'class': 'res'})
	linkre = re.compile('<a.*href="(.*)".*>.*</a>')
	h3re = re.compile('<a[^>]*>(.*)</a>')
	for a in bs:
		item = str(BeautifulSoup(str(a)).find('h3'))
		results.append([str(re.findall(h3re, item)[0]).replace('<b>', '').replace('</b>', ''), re.findall(linkre, item)[0]])
	return results


if __name__ == '__main__':
	results = getlinks("Google")
	print "Top " + str(len(results)) + " results from Yahoo\n"
	for result in results:
		print result[0] + ", " + result[1]
