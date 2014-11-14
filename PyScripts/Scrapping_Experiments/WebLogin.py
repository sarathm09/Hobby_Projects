__author__ = 'T90'
__version__ = '1.0.0'

import mechanize
import HTMLParser
from BeautifulSoup import BeautifulSoup


def getdata(id, passw):
	cols = [2, 3, 4, 8, 9, 12]
	browser = mechanize.Browser(factory=mechanize.RobustFactory())
	browser.set_handle_robots(False)
	r = browser.open("http://rajagiritech.ac.in/stud/parent/")
	browser.select_form(nr=0)
	browser.form["user"] = id
	browser.form["pass"] = passw
	print 'Submitting Auth'
	browser.submit()
	if 'Parent.asp' in str(browser.geturl()):
		print 'Auth Success'
		marklistpage = browser.open('http://rajagiritech.ac.in/stud/parent/Stud_View.asp?Sem=S7')
		html = str(marklistpage.read()).lower()
		bs = BeautifulSoup(html)
		print 'Marklist loaded'
		name = str(BeautifulSoup(html).findAll('font', attrs={'color': '#ff6600'})[0].text).replace('academic details of', '').replace('on  s7', '').replace('.', '').upper()
		print '\n Marklist of ' + name
		table = bs.findAll('table', attrs={"class": "ibox"})[0]
		rownum = 1
		for row in table.findAll('tr'):
			if rownum > 2:
				td = row.findAll('td')
				colnum = 1
				print '\n'
				for data in td:
					if colnum in cols:
						text = HTMLParser.HTMLParser().unescape(data.text).upper()
						if len(text) < 5:
							pass
						else:
							temp = ""
							for i in xrange(0, 15 - len(text)):
								temp += " "
							text = text + temp if len(text) < 16 else text[:15] + "..."
						print text, "\t",
					colnum += 1
			rownum += 1
		print ''


if __name__ == '__main__':
	idnum = input("last 4 digits : ")
	passw = (3774 + (idnum - 3107))
	getdata("U110" + str(idnum), str(passw))