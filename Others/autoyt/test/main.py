__author__ = 'T90'
__version__ = '1.0.0'

from PySide.QtCore import *
from PySide.QtGui import *
import gui
import sys

class MyApp(QDialog, gui.Ui_Form):
	def __init__(self):
		super(MyApp, self).__init__()
		self.setupUi(self)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	tooltip = MyApp()
	tooltip.show()
	app.exec_()