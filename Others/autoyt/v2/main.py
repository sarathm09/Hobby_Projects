__author__ = 'T90'
__version__ = '1.0.0'

from PySide.QtGui import QDialog, QApplication, QFileDialog, QMessageBox
from time import sleep
from PySide.QtCore import Signal
from gui import Ui_DownloaderGUI
from threading import Thread
from sys import argv
from subprocess import Popen

class MyApp(QDialog, Ui_DownloaderGUI):

	UpdateSig = Signal()

	def __init__(self):
		super(MyApp, self).__init__()
		self.setupUi(self)
		self.setupfiles()
		self.initui()

	def updateUi(self):
		try:
			self.mcom.setText(open("files/mstatus", "r").read())
			self.mfail.setText(str(len(open("files/mfail", "r").read().split("\n"))-1))
			#Vid Name^tot^rat^eta^speed
			pstatus = open("files/pstatus","r").read().split("\n")
			n = 0
			self.tot = 0.0
			for stat in pstatus:
				n += 1
				if n>5:
					break
				details = stat.split("^")
				if n==1 :
					self.p1.setValue(float(details[2]) * 100)
					self.p1l.setText(str(details[0]))
					self.p1l.setToolTip(str(details[0]))
					self.p1d.setText(str("size: " + str(float(details[1])/1024))[0:6] +
									 ", eta " + str(float(details[3]/60))[0:4])
				elif n == 2:
					self.p2.setValue(float(details[2]) * 100)
					self.p2l.setText(str(details[0]))
					self.p2l.setToolTip(str(details[0]))
					self.p2d.setText(str("size: " + str(float(details[1])/1024))[0:6] +
										 ", eta " + str(float(details[3]/60))[0:4])
				elif n == 3:
					self.p3.setValue(float(details[2]) * 100)
					self.p3l.setText(str(details[0]))
					self.p3l.setToolTip(str(details[0]))
					self.p3d.setText(str("size: " + str(float(details[1])/1024))[0:6] +
										 ", eta " + str(float(details[3]/60))[0:4])
				elif n == 4:
					self.p4.setValue(float(details[2]) * 100)
					self.p4l.setText(str(details[0]))
					self.p4l.setToolTip(str(details[0]))
					self.p4d.setText(str("size: " + str(float(details[1]) / 1024))[0:6] +
										 ", eta " + str(float(details[3] / 60))[0:4])
				elif n == 5:
					self.p5.setValue(float(details[2]) * 100)
					self.p5l.setText(str(details[0]))
					self.p5l.setToolTip(str(details[0]))
					self.p5d.setText(str("size: " + str(float(details[1])/1024))[0:6] +
										 ", eta " + str(float(details[3]/60))[0:4])

				self.tot += float(details[4])
			self.speed.display(self.tot)
			self.logbox.setText(open("files/dstatus").read())
		except:
			pass

	def looper(self):
		while True:
			self.UpdateSig.emit()
			sleep(1)

	def setupfiles(self):
		open("files/mstatus", "w").write("0/0")
		open("files/mfail", "w").write("")
		open("active.txt", "w").write("0")
		open("files/pstatus", "w").write("Not Allocated^0^0^0^0\n"*5)
		open("files/dstatus", "w").write("\n"*5)


	def initui(self):
		#buttons in main page
		self.downbtn.clicked.connect(self.dwn)
		self.movebtn.clicked.connect(self.movefile)
		self.session.clicked.connect(self.savesession)

		self.urlbox.textChanged.connect(self.dwn)

		#buttons in option page
		self.dloc.clicked.connect(self.dlocclicked)
		self.msrc.clicked.connect(self.msrcclicked)
		self.mdest.clicked.connect(self.mdestclicked)


		#GUI update Signal
		self.UpdateSig.connect(self.updateUi)

		#GUI update thread
		self.UpdateThread = Thread(target=self.looper)
		self.UpdateThread.setDaemon(True)
		self.UpdateThread.start()


	def dwn(self):
		open("files/bkp", "a").write(open("files/temp.txt").read())
		open("files/temp.txt", "w").write(self.urlbox.toPlainText())
		if not self.downbtn.isChecked():
			self.downbtn.setText("Update Links")
			Popen("python DownloadLoop.py " + self.dloc.text())


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
