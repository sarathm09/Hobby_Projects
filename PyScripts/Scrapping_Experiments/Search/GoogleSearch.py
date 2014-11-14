__author__ = 'T90'
__version__ = '1.0.0'

import mechanize
from BeautifulSoup import BeautifulSoup
import re


def searchhtml(keyword):
	chrome = mechanize.Browser()
	chrome.set_handle_robots(False)
	chrome.addheaders = [('User-agent',
						  'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36')]

	base_url = 'https://www.google.co.in/search?q='
	search_url = base_url + keyword.replace(' ', '+')

	return chrome.open(search_url)


def getlinks(keyword):
	results = []
	html = searchhtml(keyword)
	bs = BeautifulSoup(html).findAll('li', attrs={'class': 'g'})
	linkre = re.compile('<a.*href="([^"]*)".*>.*</a>')
	h3re = re.compile('<a.*>(.*)</a>')
	for a in bs:
		item = str(BeautifulSoup(str(a)).find('h3'))
		results.append([re.findall(h3re, item)[0], re.findall(linkre, item)[0]])
	return results


if __name__ == '__main__':
	results = getlinks("Google")
	for result in results:
		print result[0] + ", " + result[1]