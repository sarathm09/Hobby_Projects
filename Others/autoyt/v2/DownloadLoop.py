__author__ = 'T90'
__version__ = '1.0.0'

import sys, time, os
from multiprocessing import Process
import random

def demo(abc):
	a =  random.randint(0, 30)
	b = a
	while a<100:
		#print str(a) + "from " + str(abc)
		a += 1
		open("files/p" + str(abc), "w").write(str(b) + "^" + str(a))
		# print str(a)
		time.sleep(random.randint(0, 10)/5)
	active = open('active.txt', 'r').read().split(",")
	active[abc] = 'False'
	open('active.txt', 'w').write(str(','.join(active)))


def update_new_files():
	global links, num_files, filename
	# get file contents
	nlist = filter(lambda x: x != '' and x[0] != '#', open(filename, 'r').read().split('\n'))
	# check and update if there are new contents
	if len(nlist) > num_files:
		for i in xrange(num_files, len(nlist)):
			links.append(nlist[i])
			num_files += 1


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
	# if there is any extra argument, make the download silent
	path = sys.argv[1]
	# file for maintaining number of active downloads
	open('active.txt', 'w').write('False,False,False,False,False')
	# make the downloads folder
	if not os.path.exists(path):
		os.mkdir(path)
	print path
	try:
		os.mkdir(path + "/videos/")
		os.mkdir(path + "/playlists/")
	except:
		pass
	# Start the auto file mover program
	# the main loop
	while len(links) > 0:
		active = open('active.txt', 'r').read().split(",").count('True')
		print active, open('active.txt', 'r').read().split(",")
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
						Process(target=demo, args=(pnum,)).start()
						pass
					elif 'playlist?list' in url:
						#Popen('python dLink.py -p ' + url + ' -d ' + path)
						pass
		update_new_files()
		time.sleep(0.5)
	print 'over'