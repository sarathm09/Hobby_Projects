import requests, re
from BeautifulSoup import BeautifulSoup

url = "http://periodictable.com/Elements/"
imgurls = []

for i in range(1, 119):
	# temp = url + str(i).rjust(3, '0') + "/index.html"
	# data = requests.get(temp).content
	# bs = BeautifulSoup(data)
	# for l in bs.findAll('img'):
	# 	if 's9s.JPG' in l['src']:
	# 		imgurls.append(url + l['src'])

	temp = url + str(i).rjust(3, '0') + "/data.html"
	data = requests.get(temp).content
	bs = BeautifulSoup(data)
	# print bs.prettify()
	print "A"
	if i == 1:
		open("table.csv", "w").write(",")
		b = bs.findAll('table')[7]
		for td in b.findAll('td')[2:]:
			if '#AAAAAA' in str(td):
				open("table.csv", "a").write("\"" + td.text.replace("\"", "\\\"") + "\",")
		b = bs.findAll('table')[9]
		for td in b.findAll('td'):
			if '#AAAAAA' in str(td):
				open("table.csv", "a").write("\"" + td.text.replace("\"", "\\\"") + "\",")
		open("table.csv", "a").write("\n")
	b = bs.findAll('table')[7]
	for td in b.findAll('td')[2:]:
		if '#AAAAAA' not in str(td) and '<b>' not in str(td):
			open("table.csv", "a").write("\"" + td.text.replace("\"", "\\\"") + "\",")
	b = bs.findAll('table')[9]
	for td in b.findAll('td'):
		if '#AAAAAA' not in str(td) and '<b>' not in str(td):
			open("table.csv", "a").write("\"" + td.text.replace("\"", "\\\"") + "\",")

	open("table.csv", "a").write("\n")