from threading import Thread
from PySide.QtCore import *
from PySide.QtGui import *
from sys import argv
import socket


class MyApp(QWidget):
	def __init__(self):
		super(MyApp, self).__init__()
		self.host = ''
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
		self.s.bind((self.host, self.port))
		self.s.listen(1)
		Thread(target=self.getMsg).start()


	def getMsg(self):
		self.conn, self.addr = self.s.accept()
		self.cbox.append("Connected from " + str(self.addr))
		while True:
			msg = self.conn.recv(1024)
			self.cbox.append(str(self.addr) + ": " + msg)

	def sendMsg(self):
		msg = self.ip.text()
		if len(msg) > 1 and msg != "\n":
			self.conn.sendall(msg)


app = QApplication(argv)
mp = MyApp()
app.exec_()