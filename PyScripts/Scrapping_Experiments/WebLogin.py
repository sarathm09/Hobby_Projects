__author__ = 'T90'
__version__ = '1.0.0'

import mechanize
from BeautifulSoup import BeautifulSoup
import HTMLParser

def getdata():
	cols = [2, 3, 4, 8, 9, 12]
	browser = mechanize.Browser(factory=mechanize.RobustFactory())
	browser.set_handle_robots(False)
	r = browser.open("http://rajagiritech.ac.in/stud/parent/")
	browser.select_form(nr=0)
	browser.form["user"] = "U1103121"
	browser.form["pass"] = "3788"
	print 'Submitting Auth'
	browser.submit()
	if 'Parent.asp' in str(browser.geturl()):
		print 'Auth Success'
		marklistpage = HTMLParser.HTMLParser().unescape(browser.open('http://rajagiritech.ac.in/stud/parent/Stud_View.asp?Sem=S7'))
		bs = BeautifulSoup(marklistpage)
		print 'Marklist loaded'
		table = bs.findAll('table', attrs={"class": "ibox"})[0]
		rownum = 1
		for row in table.findAll('tr'):
			if rownum > 2:
				td = row.findAll('td')
				colnum = 1
				for data in td:
					if colnum in cols:
						print data.text
					colnum += 1
			rownum += 1

getdata()