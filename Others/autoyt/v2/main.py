from time import sleep

__author__ = 'T90'
__version__ = '1.0.0'

from PySide.QtGui import QDialog, QApplication, QFileDialog, QMessageBox
from gui import Ui_DownloaderGUI
from threading import Thread
import sys
from subprocess import Popen

class MyApp(QDialog, Ui_DownloaderGUI):

	def __init__(self):
		super(MyApp, self).__init__()
		self.setupUi(self)
		self.setupfiles()
		self.initui()
		self.t = Thread(target=self.looper)
		self.t.start()
		#self.t.join()


	def looper(self):
		while True:
			self.updateUi()

	def updateUi(self):
		i = 0
		while True:
			print i
			self.dfail.setText(str(i))
			i += 1
			sleep(3)

	def setupfiles(self):
		open("files/mstatus", "w").write("0/0")


	def initui(self):
		#buttons in main page
		self.downbtn.clicked.connect(self.dwn)
		self.movebtn.clicked.connect(self.move)
		self.session.clicked.connect(self.savesession)

		#buttons in option page
		self.dloc.clicked.connect(self.dlocclicked)
		self.msrc.clicked.connect(self.msrcclicked)
		self.mdest.clicked.connect(self.mdestclicked)

	def dwn(self):
		if self.downbtn.isChecked():
			self.downbtn.setText("Stop Download")
		else:
			self.downbtn.setText("Download")

	def move(self):
		if self.movebtn.isChecked():
			self.movebtn.setText("Moving")
			self.mproc = Popen("python movepy.py " + self.msrc.text() + " " +self.mdest.text())
		else:
			self.mproc.terminate()
		self.movebtn.setText("Move")
		self.movebtn.setChecked(False)


	def savesession(self):
		QMessageBox.information(self, "Success", "Session details has been saved.")

	def dlocclicked(self):
		newloc = self.getFolder(self.dloc.text())
		if newloc != "":
			self.dloc.setText(newloc)

	def msrcclicked(self):
		newloc = self.getFolder(self.msrc.text())
		if newloc != "":
			self.msrc.setText(newloc)

	def mdestclicked(self):
		newloc = self.getFolder(self.mdest.text())
		if newloc != "":
			self.mdest.setText(newloc)

	def getFolder(self, default):
		flags = QFileDialog.DontResolveSymlinks | QFileDialog.ShowDirsOnly
		return QFileDialog.getExistingDirectory(self, "Select Directory", default, flags)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	mainclass = MyApp()
	mainclass.show()
	app.exec_()
