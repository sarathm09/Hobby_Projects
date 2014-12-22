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
		self.tabs.addTab(DownloaderTab(), "Main")
		self.tabs.addTab(OptionsTab(), "Options")
		self.tabs.addTab(AboutTab(), "About")

		self.tabs.currentChanged.connect(self.refreshtabs)

		self.mainlayout = QVBoxLayout()
		self.setLayout(self.mainlayout)
		self.mainlayout.addWidget(self.tabs)
		self.show()

	def refreshtabs(self):
		if self.tabs.currentIndex() == 0:
			DownloaderTab().updateui()
		elif self.tabs.currentIndex() == 1:
			OptionsTab().updateui()


class DownloaderTab(QWidget):

	def __init__(self):
		super(DownloaderTab, self).__init__()
		self.initUi()

	def initUi(self):
		self.mainlayout = QVBoxLayout()
		self.textlayout = QHBoxLayout()
		self.counterlayout = QHBoxLayout()
		self.buttonlayoutmain = QHBoxLayout()
		self.buttonlayoutsec = QHBoxLayout()
		self.progresslayout = QHBoxLayout()
		self.setLayout(self.mainlayout)

		self.mainlayout.addLayout(self.counterlayout)
		self.mainlayout.addLayout(self.textlayout)
		self.mainlayout.addLayout(self.buttonlayoutmain)
		self.mainlayout.addLayout(self.buttonlayoutsec)
		self.mainlayout.addLayout(self.progresslayout)

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

		self.p1 = QProgressBar()
		self.p2 = QProgressBar()
		self.p3 = QProgressBar()
		self.p4 = QProgressBar()
		self.p5 = QProgressBar()
		self.p1.setValue(10)

		self.counterlayout.addWidget(self.downcounter)
		self.counterlayout.addWidget(self.dfailcounter)
		self.counterlayout.addWidget(self.movecounter)
		self.counterlayout.addWidget(self.mfailcounter)

		self.buttonlayoutmain.addWidget(self.startbtn)
		self.buttonlayoutmain.addWidget(self.movebtn)

		self.progresslayout.addWidget(self.p1)
		self.progresslayout.addWidget(self.p2)
		self.progresslayout.addWidget(self.p3)
		self.progresslayout.addWidget(self.p4)
		self.progresslayout.addWidget(self.p5)


		self.show()

	def updateui(self):
		pass

class OptionsTab(QWidget):
	def __init__(self):
		super(OptionsTab, self).__init__()
		self.initgui()

	def initgui(self):
		self.mainlayout = QVBoxLayout()
		self.setLayout(self.mainlayout)
		self.movelayout = QHBoxLayout()
		self.videolayout = QHBoxLayout()

		self.movesrc = QPushButton("Source not set")
		self.movedest = QPushButton("Destination not set")
		self.movesrc.clicked.connect(self.srcClicked)
		self.movedest.clicked.connect(self.destClicked)

		self.dloc = QPushButton("Download Location")
		self.q1 = QPushButton("Best Quality")
		self.q2 = QPushButton("Second Quality")

		self.movelayout.addWidget(self.movesrc)
		self.movelayout.addWidget(self.movedest)
		self.videolayout.addWidget(self.dloc)
		self.videolayout.addWidget(self.q1)
		self.videolayout.addWidget(self.q2)

		self.mainlayout.addLayout(self.videolayout)
		self.mainlayout.addLayout(self.movelayout)
		self.show()

	def updateui(self):
		pass

	def srcClicked(self):
		self.dir = self.getFolder()
		self.movesrc.setText(self.dir)

	def destClicked(self):
		self.dir = self.getFolder()
		self.movedest.setText(self.dir)

	def getFolder(self):
		flags = QFileDialog.DontResolveSymlinks | QFileDialog.ShowDirsOnly
		return QFileDialog.getExistingDirectory(self, "Select Directory", ".", flags)

class AboutTab(QWidget):
	def __init__(self):
		super(AboutTab, self).__init__()
		self.initui()

	def initui(self):
		self.mainlayout = QVBoxLayout()
		self.setLayout(self.mainlayout)
		self.title = QLabel("Youtube Downloader v2 by T90")
		self.mainlayout.addWidget(self.title)
		self.show()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	tooltip = MyApp()
	app.exec_()