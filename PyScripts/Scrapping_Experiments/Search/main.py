__author__ = 'T90'
__version__ = '1.0.0'

from threading import Thread
import GoogleSearch as goog
import YahooSearch as yahoo
import BingSearch as bing

if __name__ == '__main__':

	keyword = raw_input("Enter the search key : ")
	num = input("How many pages should I search? ")
	gTH = Thread(target=goog.display_results, args=(keyword, num))
	bTH = Thread(target=bing.display_results, args=(keyword, num))
	yTH = Thread(target=yahoo.display_results, args=(keyword, num))

	Th = [gTH, bTH, yTH]

	for t in Th:
		t.run()

	for t in Th:
		t.join()
