from PySide.QtCore import *
from PySide.QtGui import *
from threading import Thread
import mechanize
import re
import sys
import time


class GUI(QWidget):
	def __init__(self, parent=None):
		super(GUI, self).__init__(parent)
		self.res = QTextBrowser()
		self.inp = QLineEdit()
		self.th = Googler()
		self.showUI()


	def showUI(self):
		self.setWindowTitle('Google AutoComplete')
		self.layout = QVBoxLayout()
		self.layout.addWidget(self.res)
		self.layout.addWidget(self.inp)
		self.setLayout(self.layout)

		self.inp.textChanged.connect(self.getData)
		self.inp.returnPressed.connect(self.getData)
		self.inp.editingFinished.connect(self.getData)
		self.connect(self.th, SIGNAL("data(QString)"), self.updateUI)

	def getData(self):
		txt = self.inp.text()
		if len(txt) > 0:
			self.th.setKeyword(txt)
			self.th.start()
		else:
			self.res.setText(txt)

	def updateUI(self, d):
		self.res.setText(d)


class Googler(QThread):

	def __init__(self, parent=None):
		super(Googler, self).__init__(parent)
		self.result = ""

	def setKeyword(self, str):
		self.keyword = str

	def run(self):
		self.result = ""
		if len(self.keyword) >= 0:
			chrome = mechanize.Browser()
			chrome.set_handle_robots(False)
			chrome.addheaders = [('User-agent',
								  'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36')]
			base_url = 'https://www.google.co.in/s?gs_ri=psy-ab&q='
			search_url = base_url + self.keyword.replace(' ', '+')

			htmltxt = str(chrome.open(search_url).read()).decode('unicode_escape').replace('\\/', '/')
			suggestions = re.findall('"([a-z ]*)"', htmltxt.replace('<b>', '').replace('</b>', ''))[1:-4]
			for val in suggestions:
				self.result += val + "<br/>"
		self.emit(SIGNAL("data(QString)"), self.result)



searcher = QApplication(sys.argv)
app = GUI()
app.show()
searcher.exec_()
