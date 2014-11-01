#!/usr/bin/env python
"""
Youtube downloader. download entire playlist. and do more!
"""
__author__ = "T90"
__credits__ = ["Jayarajan J N", "T90"]
__version__ = "1.0.0"
__status__ = "BETA"

import pafy
import argparse
import os
import sys


def logger(data):
    f = open("errors.txt", "a")
    f.write(data)
    f.write("\n")
    f.close()


def downloadVideo(url, ptype='mp4', audio=False, silent=False):
    video = pafy.new(url)
    if audio:
        best = video.getbestaudio()
    else:
        best = video.getbest(preftype=ptype)
    print "\nDownloading : " + video.title
    best.download(quiet=silent, filepath="videos")
    print "Completed : " + video.title + "\n"


def downloadPlaylist(url, start, end, ptype='mp4', silent=False, audio=False):
    plist = pafy.get_playlist(url)
    videos = [item['pafy'] for item in plist['items']]
    if start is None:
        start = 0
    else:
        start = start - 1
    if end is None:
        end = len(videos)

    for video in videos[start:end]:
        try:
            if audio:
                best = video.getbestaudio()
            else:
                best = video.getbest(preftype=ptype)
            print "Downloading : ", video.title
            best.download(quiet=silent, filepath="playlists/")
            print "Completed : ", video.title
        except:
            msg = "Error, skipping : " + video.title
            print msg
            logger(msg)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', action='store_true', help='given url is a playlist')
    parser.add_argument('--s', type=int, help='download from given index in playlist')
    parser.add_argument('--e', type=int, help='download upto given index in playlist')
    parser.add_argument('-a', action='store_true', help="download audio only")
    parser.add_argument("-u", help='url of the playlist')
    parser.add_argument("-f", help='url of the file')
    arguments = parser.parse_args()
    if not os.path.exists("videos"):
        os.mkdir("videos")
    if not os.path.exists("playlists"):
        os.mkdir("playlists")
    if arguments.f:
        f = open(arguments.f)
        for line in f:
            if line[0] == '#':
                continue
            if 'youtube.com/playlist' in list:
                downloadPlaylist(arguments.u, arguments.start, arguments.end, audio=arguments.a)
            else:
                downloadVideo(arguments.u, audio=arguments.a)
        else:
            pass
        f.close()
    elif arguments.p:
        downloadPlaylist(arguments.u, arguments.start, arguments.end, audio=arguments.a)
    else:
        downloadVideo(arguments.u, audio=arguments.a)