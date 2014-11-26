import shutil
import os
import time

src = '../'
dest = 'J:/'

logger = open('moveerror.txt', 'a')
while(True):
	l = os.listdir(src)
	for f in l:
		try:
			type = f.split('.')[-1]
			if  type == 'mp4' or type == 'flv':
				print 'moving : ' + f
				shutil.move(src+f, dest)
				print 'moved : ' + f
		except:
			print 'ERROR: ' + f
			logger.write("error: " + f)
	time.sleep(60*3)