__author__ = 'T90'
__version__ = '1.0.0'

from PySide.QtGui import *
import sys

class MyApp(QWidget):
	def __init__(self):
		super(MyApp, self).__init__()

		self.setGeometry(300,300,250, 150)
		self.setWindowTitle("Hello!!! My second app")
		self.setWindowIcon(QIcon('web.png'))

		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	a = MyApp()
	app.exec_()