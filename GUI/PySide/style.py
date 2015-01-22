from PySide.QtCore import *
from PySide.QtGui import *
from sys import argv
import qdarkstyle


class MyApp(QWidget):
	def __init__(self):
		super(MyApp, self).__init__()
		self.setStyleSheet(qdarkstyle.load_stylesheet())
		self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)
		self.initUi()

	def initUi(self):
		btn = QPushButton()


app = QApplication(argv)
mp = MyApp()
mp.show()
app.exec_()