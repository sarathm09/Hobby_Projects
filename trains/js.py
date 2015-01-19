import json, string, urllib

st = [c for c in string.ascii_uppercase]
for c in st:
	d = urllib.urlopen("http://www.mapsofindia.com/railway-timetable/train/routesearch.php?term=" + c).read()
	da = json.loads(d)
	for i in da:
		open('trains.txt', 'a').write(i['value'] + "\n")