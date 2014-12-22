import subprocess

p = subprocess.Popen("python yt.py https://www.youtube.com/watch?v=YxyX4u9KN8Q", stdout=subprocess.PIPE)
while True:
	line = p.stdout.read()
	print line