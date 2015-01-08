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
		self.label.setAutoFillBackground(True)
		p = self.label.palette()
		p.setColor(self.label.backgroundRole(), Qt.blue)
		self.label.setPalette(p)
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
		if len(text) > 0:
			if text[-1] not in ops and len(text) > 1:
				if text.count('(') == text.count(')'):
					try:
						self.browser.append("%s = <b>%s</b>" % (text, eval(text)))
						htm = '<h1 style="color:#fff;" ><font size="6000">' + str(eval(text)) + '</font></h1>'
						self.label.setText(unicode(htm))
					except:
						self.browser.append("<font color=red>INVALID</font>")



app = QApplication(sys.argv)
f = form()
f.show()
app.exec_()
