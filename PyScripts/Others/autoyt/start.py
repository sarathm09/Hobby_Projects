__author__ = 'T90'
__version__ = '1.0.0'

import os, sys, time

def update_new_files():
    global links, num_files, filename
    # get file contents
    nlist = filter(lambda x: x != '', open(filename, 'r').read().split('\n'))
    # check and update if there are new contents
    if len(nlist) > num_files:
        for i in xrange(num_files, len(nlist) + 1):
            links.append(nlist[i])
            num_files += 1

def start(type, url, playlist=''):
    global silentword
    if type == 'youtube':
        os.system(silentword + 'python yt.py ' + playlist + url)
    elif type == 'file':
        os.system(silentword + 'python fd.py ' + url)

if __name__ == '__main__':
    """
    Program to get download links from a file 'filename' and dowmload them in separate windows (to disable
    separate windows, run this program as 'python start.py silent', with 'parallel' number of windows at a
    time. The file 'filename' can be updated any time with new links for files, videos or playlists, they'll
    be automatically added to the queue.
    """
    filename = 'list.txt'
    # read file and ignore empty lines
    links = filter(lambda x: x != '', open(filename, 'r').read().split('\n'))
    parallel, num_files, silentword = 5, len(links), ''
    # if there is any extra argument, make the download silent
    if len(sys.argv) == 2:
        silentword = ''
    else:
        silentword  = 'start '
    # file for maintaining number of active downloads
    if os.path.exists('active.txt'):
        active = int(open('active.txt', 'r').read())
    else:
        open('active.txt', 'w').write('0')
        active = 0
    # make the downloads folder
    if not os.path.exists('downloads/'):
        os.mkdir('downloads')
    # the main loop
    while len(links) > 0:
        active = int(open('active.txt', 'r').read())
        while active < parallel:
            update_new_files()
            if len(links) == 0:
                break
            active = int(open('active.txt', 'r').read())
            url = str(links[0])
            links.remove(url)
            print 'alloted : ' + url + ', remaining : ' + str(len(links)-1)
            active += 1
            open('active.txt','w').write(str(active))
            if 'youtube.com/' in url:
                if len(url) > 0:
                    if 'watch?v' in url:
                        start('youtube', url)
                    elif 'playlist?list' in url:
                        start('youtube', url, '-p ')
            else:
                start('file', url)
        time.sleep(10)