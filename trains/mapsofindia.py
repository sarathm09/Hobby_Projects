import urllib
from BeautifulSoup import BeautifulSoup

tlist = open('trains.txt').read().split("\n")
for t in tlist:
	data = urllib.urlopen(
		"http://www.mapsofindia.com/railway-timetable/train/check.php?value=" + t.replace(" ", "+")).read()
	temp = urllib.urlopen("http://www.mapsofindia.com/railway-timetable/" + data.strip() + ".html").read()
	num = t.split("-")[0]
	name = t.split("-")[1]
	tr = "\nTrain," + num + "," + name + ",,,,,,,\n"
	bs = BeautifulSoup(temp)
	n = 0
	d = bs.find("div", "image")
	for i in d.findAll("td"):
		n += 1
		tr += (i.text + ",")
		if n % 9 == 0:
			tr += "\n"
	open('trains.csv', 'a').write(tr + "\n")
	print 'completed ' + str(tlist.index(t))