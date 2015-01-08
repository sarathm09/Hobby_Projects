from PySide.QtCore import *
from PySide.QtGui import *
from sys import argv
import time
from threading import Thread

class MyPainter(QWidget):

	def __init__(self):
		super(MyPainter, self).__init__()
		self.initui()

	def mousePressEvent(self, event):
		self.startx = event.pos().x()
		self.starty = event.pos().y()

	def mouseMoveEvent(self, event):
		self.looper(event.pos())

	def mouseReleaseEvent(self, event):
		self.points.append([[self.startx, self.starty],[event.pos().x(), event.pos().y()], [self.pen, self.brush]])
		print self.points

	def initui(self):
		self.points = []
		self.qp = ''
		self.ml = QVBoxLayout()
		self.setLayout(self.ml)
		self.w = QWidget()
		self.ml.addWidget(self.w)
		self.show()


	def looper(self, qp):
		self.qp = qp
		self.update()


	def paintEvent(self, event=None):
		self.p = QPainter(self)
		self.paintPrev()
		self.pen = Qt.blue
		self.brush = Qt.darkBlue
		self.p.setPen(Qt.blue)
		self.p.setBrush(Qt.darkBlue)
		if self.qp != '':
			self.p.drawRect(self.startx, self.starty, self.qp.x()-self.startx, self.qp.y()-self.starty)
		else:
			self.p.drawRect(10, 10, 100, 100)
		self.p.end()

	def paintPrev(self):
		for box in self.points:
			self.p.setPen(box[2][0])
			self.p.setBrush(box[2][1])
			self.p.drawRect(box[0][0], box[0][1], box[1][0] - box[0][0], box[1][1] - box[0][1])


app = QApplication(argv)
mp = MyPainter()
app.exec_()