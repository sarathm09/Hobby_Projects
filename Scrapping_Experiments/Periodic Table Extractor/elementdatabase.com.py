import requests, re
from BeautifulSoup import BeautifulSoup

url = "http://www.elementsdatabase.com"
r = requests.get(url)
links = []
bs1 = BeautifulSoup(r.content)

for l in bs1.findAll('a'):
	if 'element' in l['href'] and 'database' not in l['href']:
		links.append(url + str(l['href']))

for a in links:
	data = requests.get(a).content
	sym = re.findall("Symbol:</b> ([A-Za-z]*)", data)[0]
	name = re.findall("<h1>([A-Za-z]*)</h1>", data)[0]
	z = re.findall("Atomic Number:</b> ([0-9]*)", data)[0]
	wt = re.findall("Atomic Weight:</b> [\(]*([0-9.]*)", data)[0]
	name = re.findall("<h1>([A-Za-z]*)</h1>", data)[0]
	content = re.findall("\?</b>(.*)You can", data, flags=re.MULTILINE | re.DOTALL)[0]
	s = z + "," + name + "," + sym + "," + wt + ",\"" + name + " " + \
		re.sub("<.*>", "", content)[3:].replace("\n", "").replace("\"", "'") + "\"\n"
	open("elementdatabase_table.csv", "a").write(s)
	print name
