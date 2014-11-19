from Others.autoyt import fileDownloader

__author__ = 'T90'
__version__ = '1.0.0'

from datetime import datetime as dt
import argparse, os

def logger(data):
    f = open("log.txt", "a")
    f.write(str(dt.now()) + " : " + data)
    f.write("\n")
    f.close()

def downloadfile(url, resume = '', uname = '', passw = '', path = "downloads/files/"):
    path += url.split('/')[-1]
    if uname == '':
        downloader = fileDownloader.DownloadFile(url, path)
    else:
        downloader = fileDownloader.DownloadFile(url, path,  (uname, passw))
    try:
        downloader.download()
        logger("Completed : " + url)
    except:
        print 'Error Downloading ' + url
        logger("Failed : " + url)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='URL of the file')
    parser.add_argument('-r', help='Resume download')
    parser.add_argument('-u', help='Username, if required')
    parser.add_argument('-p', help='Password, if required')
    parser.add_argument('-path', help='Path to which file is to be downloaded')
    args = parser.parse_args()
    if not os.path.exists('downloads/files'):
        os.mkdir('downloads/files')
    if args.r:
        res = "resume"
    else:
        res = ""
    if args.u:
        downloadfile(args.url, resume=res, uname=args.u, passw=args.p)
    else:
        downloadfile(args.url, resume=res)

if __name__ == '__main__':
    main()