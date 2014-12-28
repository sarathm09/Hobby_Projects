__author__ = 'T90'
__version__ = '1.0.0'

import time
import os
from multiprocessing import Process
from sys import argv

import pafy


p = ['' for i in range(0, 5)]
filename = 'files/temp.txt'
parallel, num_files, links = 5, 0, []


class Downloader():
	def __init__(self, pnum, path):
		self.pnum = pnum
		self.path = path
		self.title = ""
		self.dirname = ""

	def getSafeFilename(self, name):
		path = list(name)
		path[0] = path[0].upper()
		for i in xrange(len(name) - 1):
			if not name[i].isalnum():
				path[i + 1] = name[i + 1].upper()
			else:
				path[i + 1] = name[i + 1].lower()
		return "".join(x for x in path if x.isalnum())

	def downloadvideo(self, url):
		try:
			video = pafy.new(url)
			best = video.getbest(preftype='mp4')
			self.title = video.title
			dstat = str(self.pnum + 1) + ", start: " + url + ", " + video.title
			self.logger(down=False, data=dstat)
			best.download(quiet=True, filepath=self.path + "/videos/", callback=self.logger)
			dstat = str(self.pnum + 1) + ", finish: " + url + ", " + video.title
			self.logger(down=False, data=dstat)
			killProcess(self.pnum)
		except:
			links.append(url)
			dstat = str(self.pnum + 1) + ", Error: " + url + ", " + video.title + ", " + video.getbest().url
			self.logger(down=False, data=dstat)

	def downloadplaylist(self, url):
		plist = pafy.get_playlist(url)
		dstat = str(self.pnum + 1) + ", start: " + url + ", " + plist['title']
		self.logger(down=False, data=dstat)
		try:
			self.dirname = self.getSafeFilename(plist['title'] if len(plist['title']) > 2 else "no_title")
			os.mkdir(self.path + "/playlists/" + self.dirname)
		except:
			pass
		for vid in plist['items']:
			try:
				self.title = vid['pafy'].title
				dstat = str(self.pnum + 1) + ", start: " + url + ", " + self.title
				self.logger(down=False, data=dstat)
				vid['pafy'].getbest().download(callback=self.logger, filepath=self.path + "/playlists/" + self.dirname,
											   quiet=True)
				killProcess(self.pnum)
			except:
				links.append(url)
				dstat = str(self.pnum + 1) + ", Error: " + url + ", " + vid['pafy'].title \
						+ ", " + vid['pafy'].getbest().url
				self.logger(down=False, data=dstat)


	def logger(self, total=0.0, recvd=0.0, ratio=0.0, rate=0.0, eta=0.0, down=True, data=""):
		if down:
			"""
			Vid Name^tot^rat^eta^speed
			"""
			self.pstat = open("files/pstatus").read().split("\n")
			self.pstat[self.pnum] = str(self.title) + "^" + str(float(total) / 1024) + "^" + \
									str(ratio) + "^" + str(str(eta)) + "^" + str(rate)
			open("files/pstatus", "w").write("\n".join(self.pstat))
		else:
			self.dstat = open("files/dstatus").read().split("\n")
			self.dstat[self.pnum] = data
			open("files/dstatus", "w").write("\n".join(self.dstat))


def update_new_files():
	global links, num_files, filename
	# get file contents
	nlist = filter(lambda x: x != '' and x[0] != '#', open(filename, 'r').read().split('\n'))
	# check and update if there are new contents
	if len(nlist) > num_files:
		for i in xrange(num_files, len(nlist)):
			links.append(nlist[i])
			num_files += 1


def killProcess(pnum):
	p[pnum].terminate()


def downloader(path):
	"""
	Program to get download links from a file 'filename' and dowmload them in separate windows (to disable
	separate windows, run this program as 'python start.py silent', with 'parallel' number of windows at a
	time. The file 'filename' can be updated any time with new links for files, videos or playlists, they'll
	be automatically added to the queue.
	"""
	update_new_files()
	dobj = [Downloader(x, path) for x in xrange(0, 5)]
	# file for maintaining number of active downloads
	open('active.txt', 'w').write('False,False,False,False,False')
	# make the downloads folder
	if not os.path.exists(path):
		os.mkdir(path)
	try:
		os.mkdir(path + "/videos/")
		os.mkdir(path + "/playlists/")
	except:
		pass
	# Start the auto file mover program
	# the main loop
	while len(links) > 0:
		active = open('active.txt', 'r').read().split(",").count('True')
		while active < parallel:
			if len(links) == 0:
				break
			active = open('active.txt', 'r').read().split(",")
			if 'False' in active:
				url = str(links[0])
				links.remove(url)
				pnum = active.index('False')
				active[pnum] = 'True'
				print 'alloted : ' + url + ', remaining : ' + str(len(links))
				open('active.txt', 'w').write(str(','.join(active)))
				if len(url) > 0:
					if 'watch?v' in url:
						# dobj[pnum].downloadvideo(url)
						p[pnum] = Process(target=dobj[pnum].downloadvideo, args=(url,))
						# p[pnum].daemon = True
						p[pnum].start()
					elif 'playlist?list' in url:
						# dobj[pnum].downloadplaylist(url)
						p[pnum] = Process(target=dobj[pnum].downloadplaylist, args=(url,))
						# p[pnum].daemon = True
						p[pnum].start()
		update_new_files()
		time.sleep(0.5)
	print 'over'


if __name__ == '__main__':
	downloader(argv[1])