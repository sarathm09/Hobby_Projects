__author__ = 'T90'
__version__ = '1.0.0'

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from math import *

class form(QDialog):
	def __init__(self, parent=None):
		super(form, self).__init__(parent)

		self.browser = QTextBrowser()
		self.linedit = QLineEdit()
		self.linedit.textChanged.connect(self.updateUi)
		self.linedit.selectAll()
		layout = QVBoxLayout()
		layout.addWidget(self.browser)
		layout.addWidget(self.linedit)
		self.setLayout(layout)
		self.linedit.setFocus()
		#self.connect(self.linedit, SIGNAL("textChanged()"), self.updateUi)
		self.setWindowTitle("Calculator")

	def updateUi(self):
		text = str(self.linedit.text())
		ops = ['+', '-', '*', '/', '%', '**', '//', '(', ')']
		if not text[-1] in ops and len(text) > 1:
			try:
				self.browser.append("%s = <b>%s</b>" % (text, eval(text)))
			except:
				self.browser.append("<font color=red>INVALID</font>")



app = QApplication(sys.argv)
f = form()
f.show()
app.exec_()
