from time import sleep
from PySide.QtCore import QThread

__author__ = 'T90'
__version__ = '1.0.0'

from PySide.QtGui import QDialog, QApplication, QFileDialog, QMessageBox
from gui import Ui_DownloaderGUI
from threading import Thread
from sys import argv
from subprocess import Popen

class MyApp(QDialog, Ui_DownloaderGUI):

	def __init__(self):
		super(MyApp, self).__init__()
		self.setupUi(self)
		self.setupfiles()
		self.initui()
		self.UpdateThread = Thread(target=self.updateUi)
		self.UpdateThread.start()

	def updateUi(self):
		while True:
			self.mcom.setText(open("files/mstatus", "r").read())
			self.mfail.setText(str(len(open("files/mfail", "r").read().split("\n"))))
			p1d = open("files/p0").read().split("^")
			p2d = open("files/p1").read().split("^")
			p3d = open("files/p2").read().split("^")
			p4d = open("files/p3").read().split("^")
			p5d = open("files/p4").read().split("^")
			# self.p1.setValue(int(p1d[1]))
			# self.p2.setValue(int(p2d[1]))
			# self.p3.setValue(int(p3d[1]))
			# self.p4.setValue(int(p4d[1]))
			# self.p5.setValue(int(p5d[1]))
			self.p1l.setText(str(p1d[0]))
			self.p2l.setText(str(p2d[0]))
			self.p3l.setText(str(p3d[0]))
			self.p4l.setText(str(p4d[0]))
			self.p5l.setText(str(p5d[0]))

			self.p1d.setText(str(p1d[1]))
			self.p2d.setText(str(p2d[1]))
			self.p3d.setText(str(p3d[1]))
			self.p4d.setText(str(p4d[1]))
			self.p5d.setText(str(p5d[1]))

			tot = int(p1d[1]) + int(p2d[1]) + int(p3d[1]) + int(p4d[1]) + int(p5d[1])
			self.speed.display(tot)
			sleep(1)


	def setupfiles(self):
		open("files/mstatus", "w").write("0/0")
		open("files/mfail", "w")
		open("active.txt", "w").write("0")
		open("files/p0", "w").write("0^0")
		open("files/p1", "w").write("0^0")
		open("files/p2", "w").write("0^0")
		open("files/p3", "w").write("0^0")
		open("files/p4", "w").write("0^0")


	def initui(self):
		#buttons in main page
		self.downbtn.clicked.connect(self.dwn)
		self.movebtn.clicked.connect(self.movefile)
		self.session.clicked.connect(self.savesession)

		#buttons in option page
		self.dloc.clicked.connect(self.dlocclicked)
		self.msrc.clicked.connect(self.msrcclicked)
		self.mdest.clicked.connect(self.mdestclicked)

	def dwn(self):
		if self.downbtn.isChecked():
			self.downbtn.setText("Stop Download")
			self.isDownloading = True
			open("files/bkp", "a").write(open("files/temp.txt").read())
			open("files/temp.txt","w").write(self.urlbox.toPlainText())
			Popen("python DownloadLoop.py " + self.dloc.text())

		else:
			self.downbtn.setText("Download")
			self.isDownloading = False

	def movefile(self):
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
	app = QApplication(argv)
	mainclass = MyApp()
	mainclass.show()
	app.exec_()
