#!/usr/bin/env python
"""
Youtube downloader. Download separate videos, entire playlist, audio etc
"""
__author__ = "T90"
__credits__ = "Jayarajan J N"
__version__ = "1.1.0"
__status__ = "Beta"

from datetime import datetime as dt
import argparse
import os
import pafy


def logger(data):
    f = open("log.txt", "a")
    f.write(str(dt.now()) + " : " + data)
    f.write("\n")
    f.close()


def downloadvideo(url, ptype='mp4', audio=False, silent=False):
    video = pafy.new(url)
    if audio:
        best = video.getbestaudio()
    else:
        best = video.getbest(preftype=ptype)
    print "\nDownloading : " + video.title
    try:
        best.download(quiet=silent, filepath="downloads/videos/")
        msg = "v@ Completed : " + video.title + url
    except:
        msg = "v@ Failed : " + video.title +  url
    logger(msg)
    active = int(open('active.txt', 'r').read())
    open('active.txt', 'w').write(str(active - 1))


def playlist(url, start, end, ptype='mp4', silent=False, audio=False):
    plist = pafy.get_playlist(url)
    videos = [item['pafy'] for item in plist['items']]
    if start is None:
        start = 0
    else:
        start -= 1
    if end is None:
        end = len(videos)
    for video in videos[start:end]:
        try:
            if audio:
                best = video.getbestaudio()
            else:
                best = video.getbest(preftype=ptype)
            print "\nDownloading : " + video.title
            best.download(quiet=silent, filepath="downloads/playlists/")
            msg = "p@ Completed : " + video.title + url
        except:
            msg = "p@ Error, skipping : " + video.title + url
    print msg
    logger(msg)
    active = int(open('active.txt', 'r').read())
    open('active.txt', 'w').write(str(active - 1))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', action='store_true', help='given url is a playlist')
    parser.add_argument('--start', type=int, help='download from given index in playlist')
    parser.add_argument('--end', type=int, help='download upto given index in playlist')
    parser.add_argument('-a', action='store_true', help="download audio only")
    parser.add_argument("url", help='url of the playlist')
    arguments = parser.parse_args()
    if not os.path.exists("downloads"):
        os.mkdir('downloads')
        os.mkdir("downloads/videos")
        os.mkdir("downloads/playlists")
    if arguments.p:
        playlist(arguments.url, arguments.start, arguments.end, audio=arguments.a)
    else:
        downloadvideo(arguments.url, audio=arguments.a)


if __name__ == '__main__':
    main()