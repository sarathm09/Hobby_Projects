from Scrapping_Experiments import getdata

__author__ = 'T90'
__version__ = '1.0.0'

if __name__ == '__main__':
	starturl = "http://csebeta.x10.mx"
	links = [starturl]
	visited = []
	dead = []
	while len(links) > 0:
		try:
			if starturl in links[0]:
				links += getdata.fetch_urls(links[0])
				for a in links:
					print a
				visited.append(links[0])
			links.pop(0)
		except:
			dead.append(links[0])
			links.pop(0)
	print 'Dead : ', dead