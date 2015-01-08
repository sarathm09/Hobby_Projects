__author__ = 'T90'
__version__ = '1.0.0'

import sys, time
from PySide.QtCore import *
from PySide.QtGui import *

app = QApplication(sys.argv)
try:
	due = QTime.currentTime()
	msg = "Alert!!!"
	if len(sys.argv) < 2:
		raise ValueError
	hr, min = sys.argv[1].split(":")
	due = QTime(int(hr), int(min))
	if not due.isValid():
		raise ValueError
	if len(sys.argv) > 2:
		msg = " ".join(sys.argv[2:])
except ValueError:
	msg = "Error"
while QTime.currentTime() < due:
	time.sleep(10)
label = QLabel(text="<font color=red size=72><b>" + msg + "</b></font>")
label.setWindowFlags(Qt.SplashScreen)
label.show()
QTimer.singleShot(20000, app.quit)
app.exec_()

