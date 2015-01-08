__author__ = 'T90'
__version__ = '1.0.0'

from PySide.QtCore import *
from PySide.QtGui import *
from sys import argv

class App(QWidget):
	def __init__(self):
		super(App, self).__init__()
		self.initUi()

	def initUi(self):
		self.l = QVBoxLayout()
		self.setLayout(self.l)
		self.b1 = QPushButton()
		self.tb = QTextBrowser()
		self.l.addWidget(self.b1)
		self.l.addWidget(self.tb)

		machine = QStateMachine(self)
		s1 = QState()
		s2 = QState()
		s3 = QState()

		s1.assignProperty(self.b1, "text", "@ state 1")
		s1.assignProperty(self.tb, "rotation", 60.0)

		s2.assignProperty(self.b1, "text", "@ state 2")
		s2.assignProperty(self.tb, "rotation", 120.0)

		s3.assignProperty(self.b1, "text", "@ state 3")
		s3.assignProperty(self.tb, "rotation", 180.0)

		s1.addTransition(self.b1.clicked, s2)
		s2.addTransition(self.b1.clicked, s3)
		s3.addTransition(self.b1.clicked, s1)

		machine.addState(s1)
		machine.addState(s2)
		machine.addState(s3)
		machine.setInitialState(s1)

		machine.start()
		self.show()


app = QApplication(argv)
a = App()
app.exec_()
