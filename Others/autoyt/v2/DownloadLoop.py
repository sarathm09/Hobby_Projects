__author__ = 'T90'
__version__ = '1.0.0'

import sys, time, os
from multiprocessing import Process
import pafy

p  = ['' for i in range(0,5)]

class Downloader():
	def __init__(self, pnum):
		self.pnum = pnum
		self.path = sys.argv[1]
		self.title = ""

	def downloadvideo(self, url):
		try:
			video = pafy.new(url)
			best = video.getbest(preftype='mp4')
			self.title = video.title
			dstat = str(self.pnum + 1) + ", start: " + url + ", " + video.title
			self.logger(down=False, data=dstat)
			best.download(quiet=True, filepath=self.path + "/videos", callback=self.logger)
			dstat = str(self.pnum + 1) + ", finish: " + url + ", " + video.title
			self.logger(down=False, data=dstat)
			killProcess(self.pnum)
		except:
			pass

	def logger(self, total=0.0, recvd=0.0, ratio=0.0, rate=0.0, eta=0.0, down = True, data = ""):
		if down:
			"""
			Vid Name^tot^rat^eta^speed
			"""
			self.pstat = open("files/pstatus").read().split("\n")
			self.pstat[self.pnum] = str(self.title) + "^" + str(float(total)/1024) + "^" + \
						 str(ratio) + "^" + str(str(eta) + " sec") + "^" + str(rate)
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

if __name__ == '__main__':
	"""
	Program to get download links from a file 'filename' and dowmload them in separate windows (to disable
	separate windows, run this program as 'python start.py silent', with 'parallel' number of windows at a
	time. The file 'filename' can be updated any time with new links for files, videos or playlists, they'll
	be automatically added to the queue.
	"""
	filename = 'files/temp.txt'
	parallel, num_files, links = 5, 0, []
	update_new_files()
	dobj = [Downloader(x) for x in xrange(0,5)]
	# if there is any extra argument, make the download silent
	path = sys.argv[1]
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
						p[pnum] = Process(target=dobj[pnum].downloadvideo, args=(url,))
						p[pnum].daemon = True
						p[pnum].start()
						pass
					elif 'playlist?list' in url:
						#Popen('python dLink.py -p ' + url + ' -d ' + path)
						pass
		update_new_files()
		time.sleep(0.5)
	print 'over'