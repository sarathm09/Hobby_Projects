__author__ = 'T90'
__version__ = '1.0.0'

import sys
from PySide import QtGui


class Example(QtGui.QMainWindow):
	def __init__(self):
		super(Example, self).__init__()

		self.initUI()

	def initUI(self):
		self.statusBar().showMessage('Ready')

		exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip('Exit application')
		exitAction.triggered.connect(self.close)

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(exitAction)

		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('Statusbar')
		self.show()


def main():
	app = QtGui.QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()