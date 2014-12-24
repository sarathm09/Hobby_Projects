import shutil
import os
import time

src = 'downloads/'
yttype = ['videos/', 'playlists/']
dest = 'J:/'

logger = open('moveerror.txt', 'a')
while(True):
	for directory in yttype:
		l = os.listdir(src + yttype)
		for f in l:
			try:
				type = f.split('.')[-1]
				if  type == 'mp4' or type == 'flv':
					print 'moving : ' + yttype + f
					shutil.move(src+yttype+f, dest)
					print 'moved : ' + yttype + f
			except:
				print 'ERROR: ' + f
				logger.write("error: " + yttype + f)
	time.sleep(60*3)