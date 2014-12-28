__author__ = 'T90'
__version__ = '1.0.0'

from shutil import move
from os import walk, path
from time import sleep
from sys import argv


def movefiles(src, dest):
	while True:
		flist = []
		for root, _, tfiles in walk(src):
			for f in tfiles:
				type = f.split('.')[-1]
				if type in ['mp4', 'flv', 'mp3', 'webm']:
					flist.append(path.join(root, f))
		fin1, tot = map(int, open("files/mstatus", "r").read().split("/"))
		open("files/mstatus", "w").write(str(fin1) + "/" + str(tot + len(flist)))
		for f in flist:
			try:
				print  "moving, " + f
				move(f, dest)
				fin, tot = map(int, open("files/mstatus", "r").read().split("/"))
				log = str(flist.index(f) + 1 + fin1) + "/" + str(tot)
				open("files/mstatus", "w").write(log)
				sleep(0.5)
			except:
				log = "failed, " + f
				open("files/mfail", "w").write(log)
		sleep(3)


if __name__ == '__main__':
	movefiles(argv[1], argv[2])