#!/usr/bin/env python
"""
Youtube downloader. download entire playlist. and do more!
"""
__author__ = "T90"
__credits__ = ["Jayarajan J N", "T90"]
__version__ = "1.0.0"
__status__ = "BETA"

import argparse
import sys

import pafy


def downloadVideo(url, ptype='mp4', audio=False, silent=False):
    video = pafy.new(url)
    if audio:
        best = video.getbestaudio()
    else:
        best = video.getbest(preftype=ptype)
    print "Downloading", video.title
    best.download(quiet=silent)
    print "Completed", video.title


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
            print "Downloading ", video.title
            best.download(quiet=silent)
            print "Completed", video.title
        except:
            print "Error:skipping"


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', action='store_true', help='given url is a playlist')
    parser.add_argument('--start', type=int, help='download from given index in playlist')
    parser.add_argument('--end', type=int, help='download upto given index in playlist')
    parser.add_argument('-a', action='store_true', help="download audio only")
    parser.add_argument("url", help='url of the playlist')
    arguments = parser.parse_args()
    if arguments.p:
        downloadPlaylist(arguments.url, arguments.start, arguments.end, audio=arguments.a)
    else:
        downloadVideo(arguments.url, audio=arguments.a)