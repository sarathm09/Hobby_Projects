from PySide.QtGui import *
import sys
import mechanize


class GUI(QWidget):
	def __init__(self, parent=None):
		super(GUI, self).__init__(parent)
		self.res = QTextBrowser()
		self.inp = QLineEdit()
		self.showUI()

	def showUI(self):
		self.setWindowTitle('GetWiki')
		self.inp.setPlaceholderText("Enter your search here")
		self.layout = QVBoxLayout()
		self.layout.addWidget(self.res)
		self.layout.addWidget(self.inp)
		self.setLayout(self.layout)
		self.inp.returnPressed.connect(self.getData)
		self.setGeometry(100,100,1200,600)

	def getData(self):
		self.keyword = self.inp.text()
		chrome = mechanize.Browser()
		chrome.set_handle_robots(False)
		chrome.addheaders = [('User-agent',
							  'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36')]
		self.result = ""
		if len(self.keyword) >= 0:
			base_url = 'http://en.wikipedia.org/w/index.php?go=Go&search='
			search_url = base_url + self.keyword.replace(' ', '+')
			self.res.setText(str(chrome.open(search_url).read()))



searcher = QApplication(sys.argv)
app = GUI()
app.show()
searcher.exec_()
