__author__ = 'T90'
__version__ = '1.0.0'

from PySide.QtGui import *
from PySide.QtCore import *
import sys


class MyApp(QWidget):
	def __init__(self):
		super(MyApp, self).__init__()
		self.initui()

	def initui(self):
		self.tabs = QTabWidget()
		self.tabs.addTab(DownloaderTab, "Main")
		self.tabs.addTab(OptionsTab, "Options")
		self.show()

class DownloaderTab(QWidget):
	def __init__(self):
		super(DownloaderTab, self).__init__()
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
		self.urlbox.setText("# Enter urls here. \n# Each url should be in a separate line.\n# Lines with '#' as beginning will be ignored.\n ")
		self.logbox.setToolTip("The logs will appear here")
		self.logbox.setReadOnly(True)

		self.downcounter = QLabel("0/0 Downloaded")
		self.dfailcounter = QLabel("0 Failed")
		self.movecounter = QLabel("0/0 Moved")
		self.mfailcounter = QLabel("0 Failed")


		self.startbtn = QPushButton("Start")
		self.movebtn = QPushButton("Move")

		self.textlayout.addWidget(self.urlbox)
		self.textlayout.addWidget(self.logbox)

		self.counterlayout.addWidget(self.downcounter)
		self.counterlayout.addWidget(self.dfailcounter)
		self.counterlayout.addWidget(self.movecounter)
		self.counterlayout.addWidget(self.mfailcounter)

		self.buttonlayoutmain.addWidget(self.startbtn)
		self.buttonlayoutmain.addWidget(self.movebtn)

		self.show()


class OptionsTab(QWidget):
	def __init__(self):
		super(OptionsTab, self).__init__()
		self.initgui()

	def initgui(self):
		self.label = QLabel("tab2")
		self.mainlayout = QVBoxLayout()
		self.setLayout(self.mainlayout)
		self.mainlayout.addWidget(self.label)
		self.show()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	tooltip = MyApp()
	app.exec_()