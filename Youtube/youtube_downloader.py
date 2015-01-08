#!/usr/bin/env python
"""
Youtube downloader. Download separate videos, entire playlist, audio etc
"""

import pafy, os


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


def main():
	print "Simple Youtube Downloader | by T90\n"
	url = raw_input("Enter url of the file : ")
	start, end = 0, 0
	if 'youtube.com/playlist' in url:
		if 'n' in raw_input("It seems the url is a playlist. Enter y to download full playlist and n if you want specific indices : "):
			start = input("Enter starting index : ")
			end = input("Enter ending index : ")

	if not os.path.exists("videos"):
		os.mkdir("videos")
	if not os.path.exists("playlists"):
		os.mkdir("playlists")
	if 'youtube.com/playlist' in url:
		if start == 0 and end == 0:
			playlist(url, start=None, end=None, audio=False)
		else:
			playlist(url, start, end, audio=False)
	else:
		downloadvideo(url, audio=False)

if __name__ == '__main__':
	main()