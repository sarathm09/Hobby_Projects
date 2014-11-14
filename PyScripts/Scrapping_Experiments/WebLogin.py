__author__ = 'T90'
__version__ = '1.0.0'

import mechanize
from BeautifulSoup import BeautifulSoup
import re

def getdata():
	cols = [2, 3, 4, 8, 9, 12]
	datare = re.compile('>([A-Za-z0-9]*<)')
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
		bs = BeautifulSoup(browser.open('http://rajagiritech.ac.in/stud/parent/Stud_View.asp?Sem=S7'))
		print 'Marklist loaded'
		table = bs.findAll('table', attrs={"class": "ibox"})[0]
		for row in table.findAll('tr'):
			td = row.findAll('td')
			colnum = 1
			for data in td:
				#if colnum in cols:
				print data
				print data.text
				print re.findall(datare, str(data))[0]
				colnum += 1

getdata()