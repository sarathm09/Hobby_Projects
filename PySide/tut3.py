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
		self.label = QLabel()
		self.label.setMinimumWidth(300)
		self.label.setAlignment(Qt.AlignCenter)
		self.label.setMaximumHeight(self.browser.height())
		self.label.setFont('Helvetica')
		self.lablayout = QHBoxLayout()
		self.linedit.textChanged.connect(self.updateUi)
		self.linedit.selectAll()
		self.lablayout.addWidget(self.label)
		self.lablayout.addWidget(self.browser)
		layout = QVBoxLayout()
		layout.addLayout(self.lablayout)
		layout.addWidget(self.linedit)
		self.setLayout(layout)
		self.linedit.setFocus()
		#self.connect(self.linedit, SIGNAL("textChanged()"), self.updateUi)
		self.setWindowTitle("Calculator")

	def updateUi(self):
		text = str(self.linedit.text())
		ops = ['+', '-', '*', '/', '%', '**', '//']
		if text[-1] not in ops and len(text) > 1:
			if text.count('(') == text.count(')'):
				try:
					self.browser.append("%s = <b>%s</b>" % (text, eval(text)))
					htm = '<h1 style="width:100%; height:100%; background:#00f; color:#fff; font-size:700%">' + str(eval(text)) + '</h1>'
					self.label.setText(unicode(htm))
				except:
					self.browser.append("<font color=red>INVALID</font>")



app = QApplication(sys.argv)
f = form()
f.show()
app.exec_()
