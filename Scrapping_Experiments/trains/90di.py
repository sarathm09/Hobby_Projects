import urllib2, re, os
from BeautifulSoup import BeautifulSoup

ip = raw_input("Enter search query: ")
url = "http://www.90di.com/travel/m/doSearch?req=ftsearch&search_bar=" + ip.replace(" ", "+")
data = urllib2.urlopen(url).read()
bs = BeautifulSoup(data)
if not os.path.isfile('data.csv'):
	open('data.csv', 'w').write(
		"Train num, Train name, Source, Destination, Start time, End Time, Running days, 1A, 2A, 3A, FC, SL, 2S, CC\n")
for div in bs.findAll('div', "resultRow"):
	t = div.text.replace("&nbsp;", " ")
	print t
	num = re.findall('([0-9]*)', t)[0]
	name = re.findall('[0-9]* - ([a-zA-Z ]*)', t)[0]
	start = re.findall('([a-zA-Z ]*)', t)[11].strip()
	e1 = re.findall('([a-zA-Z ]*)', t)[24].strip()
	e2 = re.findall('([a-zA-Z ]*)', t)[25].strip()
	end = e1 if e1 != '' else e2
	starttym = re.findall('([0-9]*:[0-9][^\(\)]*)', t)[0]
	endtym = re.findall('([0-9]*:[0-9][^\(\)]*)', t)[1]
	operates = re.findall('Operates on ([a-zA-Z ,0-9]*)', t)[0].replace(",", ";")
	rates = re.findall('Rs.[0-9\.\(\)ASLFC]*', t)
	cls = ['1A', '2A', '3A', 'FC', 'SL', '2S', 'CC']
	train = num + ", " + name + ", " + start + ", " + end + ", " + starttym + ", " + endtym + ", " + operates
	for c in cls:
		f = False
		for r in rates:
			# print c, r
			if str(c) in str(r):
				train += ", " + r.replace("(" + c + ")", "")
				f = True
		if not f:
			train += ","

	open('data.csv', 'a').write(train + "\n")