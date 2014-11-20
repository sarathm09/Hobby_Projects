__author__ = 'T90'
__version__ = '1.0.0'

from PySide.QtGui import *
import sys

qapp = QApplication(sys.argv)
qw = QWidget()
qw.setWindowTitle("My first app")
qw.resize(300,100)
qw.show()

qapp.exec_()