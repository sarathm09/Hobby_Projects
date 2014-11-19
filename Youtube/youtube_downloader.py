#!/usr/bin/env python
"""
Youtube downloader. Download separate videos, entire playlist, audio etc
"""
__author__ = "T90"
__credits__ = "Jayarajan J N"
__version__ = "1.1.0"
__status__ = "Beta"

import argparse
import os
import pafy


def logger(data):
	f = open("errors.txt", "a")
	f.write(data)
	f.write("\n")
	f.close()


def downloadvideo(url, ptype='mp4', audio=False, silent=False):
	video = pafy.new(url)
	if audio:
		best = video.getbestaudio()
	else:
		best = video.getbest(preftype=ptype)
	print "\nDownloading : " + video.title
	best.download(quiet=silent, filepath="videos")
	msg = "Completed : " + video.title + "\n"
	print msg


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
			best.download(quiet=silent, filepath="playlists/")
			msg = "Completed : " + video.title + "\n"
			print msg
		except:
			msg = "Error, skipping : " + video.title
			print msg
			logger(msg)


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-p', action='store_true', help='given url is a playlist')
	parser.add_argument('--s', type=int, help='download from given index in playlist')
	parser.add_argument('--e', type=int, help='download till given index in playlist')
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
				playlist(arguments.u, arguments.start, arguments.end, audio=arguments.a)
			else:
				downloadvideo(arguments.u, audio=arguments.a)
		else:
			pass
		f.close()
	elif arguments.p:
		playlist(arguments.u, arguments.start, arguments.end, audio=arguments.a)
	else:
		downloadvideo(arguments.u, audio=arguments.a)


if __name__ == '__main__':
	main()