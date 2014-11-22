from PySide.QtCore import *
from PySide.QtGui import *
from threading import Thread
import mechanize
import re
import sys


class GUI(QWidget):

	def __init__(self):
		super(GUI, self).__init__()
		self.showUI()

	def getSuggestions(self):
		keyword = self.inp.text()
		if len(keyword)>= 0:
			chrome = mechanize.Browser()
			chrome.set_handle_robots(False)
			chrome.addheaders = [('User-agent',
								  'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36')]

			base_url = 'https://www.google.co.in/s?gs_ri=psy-ab&q='
			search_url = base_url + keyword.replace(' ', '+')

			htmltxt = str(chrome.open(search_url).read()).decode('unicode_escape').replace('\\/', '/')
			suggestions = re.findall('"([a-z ]*)"', htmltxt.replace('<b>', '').replace('</b>', ''))[1:-4]
			self.res.setText('Top Suggestions from Google:')
			for val in suggestions:
				self.res.append(val + "<br/>")
		else:
			self.res.setText('Type something to load results')

	def showUI(self):
		global keyword
		self.res = QTextBrowser()
		self.inp = QLineEdit()
		self.inp.setFocus()
		self.res.setText('Type something to load results')
		self.inp.textEdited.connect(self.getSuggestions)
		self.setWindowTitle('Search Suggestions')
		self.layout = QVBoxLayout()
		self.layout.addWidget(self.res)
		self.layout.addWidget(self.inp)
		self.setLayout(self.layout)

searcher = QApplication(sys.argv)
app = GUI()
app.show()
searcher.exec_()
