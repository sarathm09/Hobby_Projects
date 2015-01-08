from threading import Thread
from PySide.QtCore import *
from PySide.QtGui import *
from sys import argv
import socket


class MyApp(QWidget):
	def __init__(self):
		super(MyApp, self).__init__()
		self.host = 'localhost'
		self.port = 8000
		self.initUi()
		self.initNetwork()
		self.show()

	def initUi(self):
		lay = QVBoxLayout()
		self.setLayout(lay)
		self.cbox = QTextBrowser()
		lay.addWidget(self.cbox)
		self.ip = QLineEdit()
		lay.addWidget(self.ip)
		self.ip.returnPressed.connect(self.sendMsg)

	def initNetwork(self):
		self.s = socket.socket()
		self.s.connect((self.host, self.port))
		for i in range(5):
			Thread(target=self.getMsg).start()


	def getMsg(self):
		self.s.send("Connected")
		while True:
			msg = self.s.recv(1024)
			self.cbox.append("server: " + msg)


	def sendMsg(self):
		msg = self.ip.text()
		if len(msg) > 1 and msg != "\n":
			self.s.send(msg)


app = QApplication(argv)
mp = MyApp()
app.exec_()