from BeautifulSoup import BeautifulSoup
import requests

r = requests.get(raw_input("Enter url: "))
b = BeautifulSoup(r.text)
for i in b.findAll("div", attrs={"class": "yt-lockup-dismissable"}):
	a = i.find('a')
	num = i.find('span', attrs={"class": "formatted-video-count-label"}).find('b').text
	h3 = i.find('h3').text
	print h3[:48] + ''.join([' ' for i in range((50-len(h3[:48])))]) + "http://youtube.com"+a['href'] + "\t\t\t" + num