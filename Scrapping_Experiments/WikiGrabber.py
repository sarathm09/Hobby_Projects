from PySide.QtCore import *
from PySide.QtGui import *
from threading import Thread
import sys

class GUI(QWidget):
	def __init__(self, parent=None):
		super(GUI, self).__init__(parent)
		self.res = QTextBrowser()
		self.inp = QLineEdit()
		self.th = Wiki()
		self.showUI()

	def showUI(self):
		self.setWindowTitle('GetWiki')
		self.inp.setPlaceholderText("Enter your search here")
		self.layout = QVBoxLayout()
		self.layout.addWidget(self.res)
		self.layout.addWidget(self.inp)
		self.setLayout(self.layout)
		self.inp.textChanged.connect(self.getData)
		self.inp.returnPressed.connect(self.getData)
		self.connect(self.th, SIGNAL("data(QString)"), self.updateUI,
													Qt.DirectConnection)
	def getData(self):
		txt = self.inp.text()
		if len(txt) > 0:
			self.th.setKeyword(txt)
			self.th.start()
		else:
			self.res.setText(txt)

	def updateUI(self, d):
		self.res.setText(d)

class Wiki(QThread):
	def __init__(self, parent=None):
		super(Wiki, self).__init__(parent)
		self.result = ""

	def setKeyword(self, str):
		self.keyword = str

	def run(self):
		self.result = ""
		if len(self.keyword) >= 0:
			base_url = 'http://en.wikipedia.org/w/index.php?go=Go&search='
			search_url = base_url + self.keyword.replace(' ', '+')
			result = str(chrome.open(search_url).read())
		self.emit(SIGNAL("data(QString)"), self.result)



searcher = QApplication(sys.argv)
app = GUI()
app.show()
searcher.exec_()
