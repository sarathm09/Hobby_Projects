__author__ = 'T90'
__version__ = '1.0.0'

import mechanize
from BeautifulSoup import BeautifulSoup
import re


def searchhtml(keyword):
	chrome = mechanize.Browser()
	chrome.set_handle_robots(False)
	chrome.addheaders = [('User-agent',
						  'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; InfoPath.3) ')]

	base_url = 'http://www.bing.com/search?q='
	search_url = base_url + keyword.replace(' ', '+')

	return chrome.open(search_url)


def getlinks(keyword):
	results = []
	html = searchhtml(keyword)
	bs = BeautifulSoup(html).findAll('li', attrs={'class': 'b_algo'})
	linkre = re.compile('<a.*href="([^"]*)".*>.*</a>')
	h2re = re.compile('<a[^<>]*>(.*)</a>')
	for a in bs:
		item = str(BeautifulSoup(str(a)).find('h2'))
		results.append([re.findall(h2re, item)[0].replace('<strong>', '').replace('</strong>', ''), re.findall(linkre, item)[0]])
	return results


if __name__ == '__main__':
	results = getlinks("Google")
	for result in results:
		print result[0] + ", " + result[1]