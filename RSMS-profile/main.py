__author__ = 'T90'
__version__ = '1.0.0'

import mechanize
from BeautifulSoup import BeautifulSoup

database = []


def getdata(id, passw):
	global database
	te = []
	cols = [2, 3, 4, 8, 9, 12]
	browser = mechanize.Browser()
	browser.set_handle_robots(False)
	browser.open("http://rajagiritech.ac.in/stud/parent/")
	browser.select_form(nr=0)
	browser.form["user"] = id
	browser.form["pass"] = passw
	browser.submit()
	if 'Parent.asp' in str(browser.geturl()):
		#print 'Auth Success'
		marklistpage = browser.open('http://rajagiritech.ac.in/stud/parent/stud_verify.asp')
		html = str(marklistpage.read()).encode('utf-8')
		bs = BeautifulSoup(html)
		for inp in bs.findAll('input', attrs={"disabled": "disabled"}):
			te.append(str(inp['value']))
		print "Completed : ", te[1].replace('.', '')
		database.append(te)


def tocsv(student):
	f = open('details.csv', 'a')
	for details in student:
		f.write(details + ", ")
	f.write("\n")
	f.close()


if __name__ == '__main__':
	data = open('p.txt', 'r').read().split('\n')
	n = 0
	for temp in data:
		stud = temp.split(',')
		idnum = stud[0]
		passw = stud[1]
		getdata(idnum, passw)
		tocsv(database[n])
		n += 1
