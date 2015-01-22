import json, urllib

st = [c for c in open("nums.txt").read().split("\n")]
co = 1
for c in st:
	d = urllib.urlopen("http://www.mapsofindia.com/railway-timetable/train/routesearch.php?term=" + c).read()
	da = json.loads(d)
	for i in da:
		open('southtrains.txt', 'a').write(i['value'] + "\n")
		print co, c, i['value']
		co += 1