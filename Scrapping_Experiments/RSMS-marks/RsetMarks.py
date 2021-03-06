__author__ = 'T90'
__version__ = '1.0.0'

import mechanize
import HTMLParser
from BeautifulSoup import BeautifulSoup

database = []

def getdata(id, passw):
	global database
	stud = []
	cols = [2, 3, 4, 8, 9, 12]
	browser = mechanize.Browser()
	browser.set_handle_robots(False)
	browser.open("http://rajagiritech.ac.in/stud/parent/")
	browser.select_form(nr=0)
	browser.form["user"] = id
	browser.form["pass"] = passw
	#print 'Submitting Auth'
	browser.submit()
	if 'Parent.asp' in str(browser.geturl()):
		#print 'Auth Success'
		marklistpage = browser.open('http://rajagiritech.ac.in/stud/parent/Stud_View.asp?Sem=S7')
		html = str(marklistpage.read()).lower().encode('utf-8')
		bs = BeautifulSoup(html)
		#print 'Marklist loaded'
		name = str(BeautifulSoup(html).findAll('font', attrs={'color': '#ff6600'})[0].text).replace(
			'academic details of', '').replace('on  s7', '').replace('.', '').upper()
		stud.append(name)
		#print '\n Marklist of ' + name
		table = bs.findAll('table', attrs={"class": "ibox"})[0]
		rownum = 1
		for row in table.findAll('tr'):
			if rownum > 2:
				td = row.findAll('td')
				colnum = 1
				#print '\n'
				for data in td:
					if colnum in cols:
						text = HTMLParser.HTMLParser().unescape(data.text).upper().replace(u'\xa0', u' ')
						stud.append(str(text))
						if len(text) < 5:
							pass
						else:
							temp = ""
							for i in xrange(0, 15 - len(text)):
								temp += " "
							text = text + temp if len(text) < 16 else text[:15] + "..."
						#print text, "\t",
					colnum += 1
			rownum += 1
		#print ''
		database.append(stud)


def tocsv(database):
	f = open('temp.csv', 'a')
	for stud in database:
		n = 1
		for data in stud:
			if (n - 1) % 6 == 0:
				f.write(data + "\n")
			else:
				f.write(data + ", ")
			n += 1
		f.write("\n")
	f.close()


if __name__ == '__main__':
	idnum = input("last 4 digits : ")
	passw = (3774 + (idnum - 3107))
	getdata("U110" + str(idnum), str(passw))
	tocsv(database)