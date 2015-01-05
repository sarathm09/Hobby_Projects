import pafy
from sys import argv

def convertlinks():
	for link in links:
		if "playlist?list" in link:
			temp = []
			plist = pafy.get_playlist(link)
			titles.append(plist['title'])

			for vid in [item['pafy'] for item in plist['items']]:
				best = vid.getbest(preftype="mp4")
				temp.append(best.url)
			urls.append(temp)

		else:
			vid = pafy.new(link)
			best = vid.getbest(preftype="mp4")
			titles.append(vid.title)
			urls.append([best.url])


def getdata(file):
	return filter(lambda x: x != "" and "youtube.com" in x and x[0] != "#",
				  open(file).read().split("\n"))

def savelinks():
	pass

if __name__ == '__main__':

	links, titles, urls = [[], [], []]

	filename = "list.txt"
	if len(argv)>1:
		filename = argv[1]

	links = getdata(filename)


	convertlinks()

	for i in urls:
		for j in i:
			print j

