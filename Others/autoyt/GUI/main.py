__author__ = 'T90'
__version__ = '1.0.0'

from PySide.QtGui import *
from PySide.QtCore import *
import sys


class MyApp(QWidget):
	def __init__(self):
		super(MyApp, self).__init__()
		self.initUi()

	def initUi(self):
		self.setWindowTitle('YTdwm by T90')
		self.mainlayout = QVBoxLayout()
		self.textlayout = QHBoxLayout()
		self.counterlayout = QHBoxLayout()
		self.buttonlayoutmain = QHBoxLayout()
		self.buttonlayoutsec = QHBoxLayout()
		self.setLayout(self.mainlayout)

		self.mainlayout.addLayout(self.counterlayout)
		self.mainlayout.addLayout(self.textlayout)
		self.mainlayout.addLayout(self.buttonlayoutmain)
		self.mainlayout.addLayout(self.buttonlayoutsec)

		self.urlbox = QTextEdit()
		self.logbox = QTextEdit()
		self.urlbox.setReadOnly(False)
		self.urlbox.setToolTip("Enter urls here")
		self.logbox.setToolTip("The logs will appear here")
		self.logbox.setReadOnly(True)

		self.downcounter = QLabel("Downloaded 0/0")
		self.movecounter = QLabel("Moved 0/0")

		self.startbtn = QPushButton("Start")
		self.movebtn = QPushButton("Move")

		self.textlayout.addWidget(self.urlbox)
		self.textlayout.addWidget(self.logbox)

		self.counterlayout.addWidget(self.downcounter)
		self.counterlayout.addWidget(self.movecounter)

		self.buttonlayoutmain.addWidget(self.startbtn)
		self.buttonlayoutmain.addWidget(self.movebtn)

		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	tooltip = MyApp()
	app.exec_()