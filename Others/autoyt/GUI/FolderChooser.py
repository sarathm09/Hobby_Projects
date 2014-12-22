__author__ = 'T90'
__version__ = '1.0.0'

from PySide.QtGui import *
from PySide.QtCore import *


class FolderChooser(QDialog):
	def __init__(self):
		super(FolderChooser, self).__init__()
		self.initui()

	def initui(self):
		self.layout = QVBoxLayout()
		self.setLayout(self.layout)
		self.text = QLabel
		self.dirchoose = QFileDialog()
		self.layout.addWidget(self.text)
		self.layout.addWidget(self.dirchoose)
		self.dirchoose.currentChanged.connect(self.text.setText)
		self.show()