__author__ = 'T90'
__version__ = '1.0.0'

from PySide.QtGui import *
from PySide.QtCore import *
import sys


class MyApp(QWidget):
	def __init__(self):
		super(MyApp, self).__init__()
		self.initUi()

	def initUi(self):
		QToolTip.setFont(QFont('SansSerif', 10))
		self.setToolTip('hello, this is a tooltip')

		btn = QPushButton('Click to close', self)
		btn.setToolTip('A Button ToolTip')
		btn.setGeometry(50, 50, 100, 100)
		btn.clicked.connect(QCoreApplication.instance().quit)

		self.setGeometry(300, 300, 250, 250)
		self.setWindowTitle('tooltip Test')
		self.center()

		self.statusBar().showMessage('Ready')

		self.show()

	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def closeEvent(self, event):
		reply = QMessageBox.question(self, 'Sure to Quit?', 'Are you sure u wanna quit?', QMessageBox.Yes |
									 QMessageBox.No, QMessageBox.No)
		if reply == QMessageBox.No:
			event.ignore()
		else:
			event.accept()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	tooltip = MyApp()
	app.exec_()