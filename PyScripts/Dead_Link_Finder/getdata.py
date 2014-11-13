__author__ = 'T90'
__version__ = '1.0.0'

import mechanize
import urlparse


def fetch_data(url):
	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.addheaders = [("User-agent", "Mozilla/5.0")]
	return br.open(url).read()


def fetch_urls(url):
	links = []
	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.addheaders = [("User-agent", "Mozilla/5.0")]
	br.open(url)
	for link in br.links():
		new_url = urlparse.urljoin(link.base_url, link.url)
		if new_url not in links:
			links.append(new_url)
	return links


