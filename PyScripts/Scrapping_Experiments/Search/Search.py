__author__ = 'T90'
__version__ = '1.0.0'

import GoogleSearch as goog
import YahooSearch as yahoo
import BingSearch as bing
from

if __name__ == '__main__':
	keyword = raw_input("Enter the search key : ")
	num = input("How many pages should I search? ")
	goog.display_results(keyword, num)
	bing.display_results(keyword, num)
	yahoo.display_results(keyword, num)