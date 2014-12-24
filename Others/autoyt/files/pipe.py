import subprocess
import time

p = subprocess.Popen("python yt.py https://www.youtube.com/watch?v=YxyX4u9KN8Q", stdout=subprocess.PIPE)
# q = subprocess.Popen("python yt.py https://www.youtube.com/watch?v=aSoHman19XY", stdout=subprocess.PIPE)
while True:
	p.communicate()
# p.communicate()
	# print  "1. " + p.stdout.readline(), "2. "+q.stdout.readline(),
	# time.sleep(3)
	# p.terminate()