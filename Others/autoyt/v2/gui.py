# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Wed Dec 24 13:53:37 2014
# by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class Ui_DownloaderGUI(object):
	def setupUi(self, DownloaderGUI):
		DownloaderGUI.setObjectName("DownloaderGUI")
		DownloaderGUI.resize(586, 537)
		DownloaderGUI.setAutoFillBackground(False)
		DownloaderGUI.setStyleSheet("")
		self.horizontalLayout_8 = QtGui.QHBoxLayout(DownloaderGUI)
		self.horizontalLayout_8.setSpacing(0)
		self.horizontalLayout_8.setContentsMargins(3, 3, 3, 3)
		self.horizontalLayout_8.setObjectName("horizontalLayout_8")
		self.tabs = QtGui.QTabWidget(DownloaderGUI)
		self.tabs.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.tabs.setAutoFillBackground(True)
		self.tabs.setTabPosition(QtGui.QTabWidget.West)
		self.tabs.setTabShape(QtGui.QTabWidget.Rounded)
		self.tabs.setElideMode(QtCore.Qt.ElideLeft)
		self.tabs.setDocumentMode(False)
		self.tabs.setTabsClosable(False)
		self.tabs.setObjectName("tabs")
		self.dtab = QtGui.QWidget()
		self.dtab.setObjectName("dtab")
		self.verticalLayout_2 = QtGui.QVBoxLayout(self.dtab)
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.statusbox = QtGui.QGroupBox(self.dtab)
		self.statusbox.setMinimumSize(QtCore.QSize(0, 30))
		self.statusbox.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
		self.statusbox.setFlat(False)
		self.statusbox.setObjectName("statusbox")
		self.horizontalLayout_5 = QtGui.QHBoxLayout(self.statusbox)
		self.horizontalLayout_5.setObjectName("horizontalLayout_5")
		self.widget = QtGui.QWidget(self.statusbox)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(1)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
		self.widget.setSizePolicy(sizePolicy)
		self.widget.setCursor(QtCore.Qt.ForbiddenCursor)
		self.widget.setObjectName("widget")
		self.verticalLayout = QtGui.QVBoxLayout(self.widget)
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout.setObjectName("verticalLayout")
		self.label_11 = QtGui.QLabel(self.widget)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(1)
		sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
		self.label_11.setSizePolicy(sizePolicy)
		self.label_11.setObjectName("label_11")
		self.verticalLayout.addWidget(self.label_11)
		self.speed = QtGui.QLCDNumber(self.widget)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(3)
		sizePolicy.setHeightForWidth(self.speed.sizePolicy().hasHeightForWidth())
		self.speed.setSizePolicy(sizePolicy)
		self.speed.setFrameShape(QtGui.QFrame.StyledPanel)
		self.speed.setFrameShadow(QtGui.QFrame.Sunken)
		self.speed.setSmallDecimalPoint(False)
		self.speed.setDigitCount(7)
		self.speed.setSegmentStyle(QtGui.QLCDNumber.Filled)
		self.speed.setProperty("value", 0.0)
		self.speed.setProperty("intValue", 0)
		self.speed.setObjectName("speed")
		self.verticalLayout.addWidget(self.speed)
		self.horizontalLayout_5.addWidget(self.widget)
		self.widget_2 = QtGui.QWidget(self.statusbox)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(2)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
		self.widget_2.setSizePolicy(sizePolicy)
		self.widget_2.setObjectName("widget_2")
		self.gridLayout_3 = QtGui.QGridLayout(self.widget_2)
		self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
		self.gridLayout_3.setObjectName("gridLayout_3")
		self.label_7 = QtGui.QLabel(self.widget_2)
		self.label_7.setAlignment(QtCore.Qt.AlignCenter)
		self.label_7.setWordWrap(True)
		self.label_7.setObjectName("label_7")
		self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)
		self.label_8 = QtGui.QLabel(self.widget_2)
		self.label_8.setAlignment(QtCore.Qt.AlignCenter)
		self.label_8.setWordWrap(True)
		self.label_8.setObjectName("label_8")
		self.gridLayout_3.addWidget(self.label_8, 0, 1, 1, 1)
		self.label_9 = QtGui.QLabel(self.widget_2)
		self.label_9.setAlignment(QtCore.Qt.AlignCenter)
		self.label_9.setWordWrap(True)
		self.label_9.setObjectName("label_9")
		self.gridLayout_3.addWidget(self.label_9, 0, 2, 1, 1)
		self.label_10 = QtGui.QLabel(self.widget_2)
		self.label_10.setAlignment(QtCore.Qt.AlignCenter)
		self.label_10.setWordWrap(True)
		self.label_10.setObjectName("label_10")
		self.gridLayout_3.addWidget(self.label_10, 0, 3, 1, 1)
		self.dcom = QtGui.QLabel(self.widget_2)
		self.dcom.setAlignment(QtCore.Qt.AlignCenter)
		self.dcom.setObjectName("dcom")
		self.gridLayout_3.addWidget(self.dcom, 1, 0, 1, 1)
		self.dfail = QtGui.QLabel(self.widget_2)
		self.dfail.setAlignment(QtCore.Qt.AlignCenter)
		self.dfail.setObjectName("dfail")
		self.gridLayout_3.addWidget(self.dfail, 1, 1, 1, 1)
		self.mcom = QtGui.QLabel(self.widget_2)
		self.mcom.setAlignment(QtCore.Qt.AlignCenter)
		self.mcom.setObjectName("mcom")
		self.gridLayout_3.addWidget(self.mcom, 1, 2, 1, 1)
		self.mfail = QtGui.QLabel(self.widget_2)
		self.mfail.setAlignment(QtCore.Qt.AlignCenter)
		self.mfail.setObjectName("mfail")
		self.gridLayout_3.addWidget(self.mfail, 1, 3, 1, 1)
		self.horizontalLayout_5.addWidget(self.widget_2)
		self.verticalLayout_2.addWidget(self.statusbox)
		self.io = QtGui.QGroupBox(self.dtab)
		self.io.setFlat(False)
		self.io.setObjectName("io")
		self.verticalLayout_4 = QtGui.QVBoxLayout(self.io)
		self.verticalLayout_4.setObjectName("verticalLayout_4")
		self.horizontalLayout = QtGui.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.label_6 = QtGui.QLabel(self.io)
		self.label_6.setObjectName("label_6")
		self.horizontalLayout.addWidget(self.label_6)
		self.label_5 = QtGui.QLabel(self.io)
		self.label_5.setObjectName("label_5")
		self.horizontalLayout.addWidget(self.label_5)
		self.verticalLayout_4.addLayout(self.horizontalLayout)
		self.horizontalLayout_3 = QtGui.QHBoxLayout()
		self.horizontalLayout_3.setObjectName("horizontalLayout_3")
		self.urlbox = QtGui.QTextEdit(self.io)
		self.urlbox.setProperty("cursor", QtCore.Qt.IBeamCursor)
		self.urlbox.setFrameShape(QtGui.QFrame.WinPanel)
		self.urlbox.setFrameShadow(QtGui.QFrame.Sunken)
		self.urlbox.setTabChangesFocus(True)
		self.urlbox.setTextInteractionFlags(
			QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
		self.urlbox.setObjectName("urlbox")
		self.horizontalLayout_3.addWidget(self.urlbox)
		self.logbox = QtGui.QTextEdit(self.io)
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(8)
		font.setItalic(True)
		self.logbox.setFont(font)
		self.logbox.setProperty("cursor", QtCore.Qt.BusyCursor)
		self.logbox.setFrameShape(QtGui.QFrame.WinPanel)
		self.logbox.setFrameShadow(QtGui.QFrame.Sunken)
		self.logbox.setReadOnly(True)
		self.logbox.setObjectName("logbox")
		self.horizontalLayout_3.addWidget(self.logbox)
		self.verticalLayout_4.addLayout(self.horizontalLayout_3)
		self.verticalLayout_2.addWidget(self.io)
		self.buttons = QtGui.QGroupBox(self.dtab)
		self.buttons.setMinimumSize(QtCore.QSize(0, 30))
		self.buttons.setFlat(False)
		self.buttons.setObjectName("buttons")
		self.horizontalLayout_6 = QtGui.QHBoxLayout(self.buttons)
		self.horizontalLayout_6.setObjectName("horizontalLayout_6")
		self.downbtn = QtGui.QPushButton(self.buttons)
		self.downbtn.setCursor(QtCore.Qt.PointingHandCursor)
		self.downbtn.setCheckable(True)
		self.downbtn.setDefault(False)
		self.downbtn.setFlat(False)
		self.downbtn.setObjectName("downbtn")
		self.horizontalLayout_6.addWidget(self.downbtn)
		self.movebtn = QtGui.QPushButton(self.buttons)
		self.movebtn.setCursor(QtCore.Qt.PointingHandCursor)
		self.movebtn.setCheckable(True)
		self.movebtn.setDefault(False)
		self.movebtn.setFlat(False)
		self.movebtn.setObjectName("movebtn")
		self.horizontalLayout_6.addWidget(self.movebtn)
		self.session = QtGui.QPushButton(self.buttons)
		self.session.setCursor(QtCore.Qt.PointingHandCursor)
		self.session.setDefault(False)
		self.session.setFlat(False)
		self.session.setObjectName("session")
		self.horizontalLayout_6.addWidget(self.session)
		self.verticalLayout_2.addWidget(self.buttons)
		self.progress = QtGui.QGroupBox(self.dtab)
		self.progress.setObjectName("progress")
		self.gridLayout = QtGui.QGridLayout(self.progress)
		self.gridLayout.setObjectName("gridLayout")
		self.p2 = QtGui.QProgressBar(self.progress)
		self.p2.setProperty("value", 0)
		self.p2.setAlignment(QtCore.Qt.AlignCenter)
		self.p2.setOrientation(QtCore.Qt.Horizontal)
		self.p2.setInvertedAppearance(False)
		self.p2.setTextDirection(QtGui.QProgressBar.TopToBottom)
		self.p2.setObjectName("p2")
		self.gridLayout.addWidget(self.p2, 2, 1, 1, 1)
		self.p4 = QtGui.QProgressBar(self.progress)
		self.p4.setProperty("value", 0)
		self.p4.setAlignment(QtCore.Qt.AlignCenter)
		self.p4.setOrientation(QtCore.Qt.Horizontal)
		self.p4.setInvertedAppearance(False)
		self.p4.setTextDirection(QtGui.QProgressBar.TopToBottom)
		self.p4.setObjectName("p4")
		self.gridLayout.addWidget(self.p4, 2, 3, 1, 1)
		self.p5 = QtGui.QProgressBar(self.progress)
		self.p5.setProperty("value", 0)
		self.p5.setAlignment(QtCore.Qt.AlignCenter)
		self.p5.setOrientation(QtCore.Qt.Horizontal)
		self.p5.setInvertedAppearance(False)
		self.p5.setTextDirection(QtGui.QProgressBar.TopToBottom)
		self.p5.setObjectName("p5")
		self.gridLayout.addWidget(self.p5, 2, 4, 1, 1)
		self.p1 = QtGui.QProgressBar(self.progress)
		self.p1.setProperty("value", 0)
		self.p1.setAlignment(QtCore.Qt.AlignCenter)
		self.p1.setOrientation(QtCore.Qt.Horizontal)
		self.p1.setInvertedAppearance(False)
		self.p1.setTextDirection(QtGui.QProgressBar.TopToBottom)
		self.p1.setObjectName("p1")
		self.gridLayout.addWidget(self.p1, 2, 0, 1, 1)
		self.p3 = QtGui.QProgressBar(self.progress)
		self.p3.setProperty("value", 0)
		self.p3.setAlignment(QtCore.Qt.AlignCenter)
		self.p3.setOrientation(QtCore.Qt.Horizontal)
		self.p3.setInvertedAppearance(False)
		self.p3.setTextDirection(QtGui.QProgressBar.TopToBottom)
		self.p3.setObjectName("p3")
		self.gridLayout.addWidget(self.p3, 2, 2, 1, 1)
		self.p1l = QtGui.QLabel(self.progress)
		self.p1l.setObjectName("p1l")
		self.gridLayout.addWidget(self.p1l, 0, 0, 1, 1)
		self.p2l = QtGui.QLabel(self.progress)
		self.p2l.setObjectName("p2l")
		self.gridLayout.addWidget(self.p2l, 0, 1, 1, 1)
		self.p3l = QtGui.QLabel(self.progress)
		self.p3l.setObjectName("p3l")
		self.gridLayout.addWidget(self.p3l, 0, 2, 1, 1)
		self.p4l = QtGui.QLabel(self.progress)
		self.p4l.setObjectName("p4l")
		self.gridLayout.addWidget(self.p4l, 0, 3, 1, 1)
		self.p5l = QtGui.QLabel(self.progress)
		self.p5l.setObjectName("p5l")
		self.gridLayout.addWidget(self.p5l, 0, 4, 1, 1)
		self.p1d = QtGui.QLabel(self.progress)
		self.p1d.setObjectName("p1d")
		self.gridLayout.addWidget(self.p1d, 1, 0, 1, 1)
		self.p2d = QtGui.QLabel(self.progress)
		self.p2d.setObjectName("p2d")
		self.gridLayout.addWidget(self.p2d, 1, 1, 1, 1)
		self.p3d = QtGui.QLabel(self.progress)
		self.p3d.setObjectName("p3d")
		self.gridLayout.addWidget(self.p3d, 1, 2, 1, 1)
		self.p4d = QtGui.QLabel(self.progress)
		self.p4d.setObjectName("p4d")
		self.gridLayout.addWidget(self.p4d, 1, 3, 1, 1)
		self.p5d = QtGui.QLabel(self.progress)
		self.p5d.setObjectName("p5d")
		self.gridLayout.addWidget(self.p5d, 1, 4, 1, 1)
		self.verticalLayout_2.addWidget(self.progress)
		self.tabs.addTab(self.dtab, "")
		self.otab = QtGui.QWidget()
		self.otab.setObjectName("otab")
		self.verticalLayout_5 = QtGui.QVBoxLayout(self.otab)
		self.verticalLayout_5.setObjectName("verticalLayout_5")
		self.groupBox = QtGui.QGroupBox(self.otab)
		self.groupBox.setObjectName("groupBox")
		self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox)
		self.verticalLayout_6.setObjectName("verticalLayout_6")
		self.dloc = QtGui.QPushButton(self.groupBox)
		self.dloc.setFlat(False)
		self.dloc.setObjectName("dloc")
		self.verticalLayout_6.addWidget(self.dloc)
		self.msrc = QtGui.QPushButton(self.groupBox)
		self.msrc.setObjectName("msrc")
		self.verticalLayout_6.addWidget(self.msrc)
		self.mdest = QtGui.QPushButton(self.groupBox)
		self.mdest.setObjectName("mdest")
		self.verticalLayout_6.addWidget(self.mdest)
		self.verticalLayout_5.addWidget(self.groupBox)
		self.groupBox_2 = QtGui.QGroupBox(self.otab)
		self.groupBox_2.setObjectName("groupBox_2")
		self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_2)
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.verticalLayout_7 = QtGui.QVBoxLayout()
		self.verticalLayout_7.setObjectName("verticalLayout_7")
		self.pushButton_3 = QtGui.QPushButton(self.groupBox_2)
		self.pushButton_3.setObjectName("pushButton_3")
		self.verticalLayout_7.addWidget(self.pushButton_3)
		self.horizontalLayout_2.addLayout(self.verticalLayout_7)
		self.verticalLayout_8 = QtGui.QVBoxLayout()
		self.verticalLayout_8.setObjectName("verticalLayout_8")
		self.horizontalLayout_2.addLayout(self.verticalLayout_8)
		self.verticalLayout_5.addWidget(self.groupBox_2)
		self.groupBox_3 = QtGui.QGroupBox(self.otab)
		self.groupBox_3.setObjectName("groupBox_3")
		self.horizontalLayout_4 = QtGui.QHBoxLayout(self.groupBox_3)
		self.horizontalLayout_4.setObjectName("horizontalLayout_4")
		self.label = QtGui.QLabel(self.groupBox_3)
		self.label.setObjectName("label")
		self.horizontalLayout_4.addWidget(self.label)
		self.lineEdit = QtGui.QLineEdit(self.groupBox_3)
		self.lineEdit.setObjectName("lineEdit")
		self.horizontalLayout_4.addWidget(self.lineEdit)
		self.pushButton = QtGui.QPushButton(self.groupBox_3)
		self.pushButton.setObjectName("pushButton")
		self.horizontalLayout_4.addWidget(self.pushButton)
		self.verticalLayout_5.addWidget(self.groupBox_3)
		self.groupBox_5 = QtGui.QGroupBox(self.otab)
		self.groupBox_5.setObjectName("groupBox_5")
		self.verticalLayout_5.addWidget(self.groupBox_5)
		self.groupBox_4 = QtGui.QGroupBox(self.otab)
		self.groupBox_4.setObjectName("groupBox_4")
		self.verticalLayout_5.addWidget(self.groupBox_4)
		self.tabs.addTab(self.otab, "")
		self.atab = QtGui.QWidget()
		self.atab.setObjectName("atab")
		self.tabs.addTab(self.atab, "")
		self.horizontalLayout_8.addWidget(self.tabs)

		self.retranslateUi(DownloaderGUI)
		self.tabs.setCurrentIndex(0)
		QtCore.QMetaObject.connectSlotsByName(DownloaderGUI)

	def retranslateUi(self, DownloaderGUI):
		DownloaderGUI.setWindowTitle(QtGui.QApplication.translate("DownloaderGUI", "Youtube Downloader | by T90", None,
																  QtGui.QApplication.UnicodeUTF8))
		self.statusbox.setTitle(
			QtGui.QApplication.translate("DownloaderGUI", "Status", None, QtGui.QApplication.UnicodeUTF8))
		self.label_11.setText(
			QtGui.QApplication.translate("DownloaderGUI", "Total Speed (kbps)", None, QtGui.QApplication.UnicodeUTF8))
		self.label_7.setText(
			QtGui.QApplication.translate("DownloaderGUI", "Completed", None, QtGui.QApplication.UnicodeUTF8))
		self.label_8.setText(
			QtGui.QApplication.translate("DownloaderGUI", "Failed", None, QtGui.QApplication.UnicodeUTF8))
		self.label_9.setText(
			QtGui.QApplication.translate("DownloaderGUI", "Moved", None, QtGui.QApplication.UnicodeUTF8))
		self.label_10.setText(
			QtGui.QApplication.translate("DownloaderGUI", "MFailed", None, QtGui.QApplication.UnicodeUTF8))
		self.dcom.setText(QtGui.QApplication.translate("DownloaderGUI", "0/0", None, QtGui.QApplication.UnicodeUTF8))
		self.dfail.setText(QtGui.QApplication.translate("DownloaderGUI", "0", None, QtGui.QApplication.UnicodeUTF8))
		self.mcom.setText(QtGui.QApplication.translate("DownloaderGUI", "0/0", None, QtGui.QApplication.UnicodeUTF8))
		self.mfail.setText(QtGui.QApplication.translate("DownloaderGUI", "0", None, QtGui.QApplication.UnicodeUTF8))
		self.io.setTitle(
			QtGui.QApplication.translate("DownloaderGUI", "Download", None, QtGui.QApplication.UnicodeUTF8))
		self.label_6.setText(
			QtGui.QApplication.translate("DownloaderGUI", "URL Input", None, QtGui.QApplication.UnicodeUTF8))
		self.label_5.setText(QtGui.QApplication.translate("DownloaderGUI", "Log", None, QtGui.QApplication.UnicodeUTF8))
		self.urlbox.setHtml(QtGui.QApplication.translate("DownloaderGUI",
														 "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
														 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
														 "p, li { white-space: pre-wrap; }\n"
														 "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
														 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\"># Enter urls here. </span></p>\n"
														 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\"># Each url should be in a separate line.</span></p>\n"
														 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\"># Lines with \'#\' as beginning will be ignored.</span></p>\n"
														 "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
														 "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>",
														 None, QtGui.QApplication.UnicodeUTF8))
		self.logbox.setHtml(QtGui.QApplication.translate("DownloaderGUI",
														 "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
														 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
														 "p, li { white-space: pre-wrap; }\n"
														 "</style></head><body style=\" font-family:\'Arial\'; font-size:8pt; font-weight:400; font-style:italic;\">\n"
														 "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:normal;\">No Logs Yet</span></p></body></html>",
														 None, QtGui.QApplication.UnicodeUTF8))
		self.buttons.setTitle(
			QtGui.QApplication.translate("DownloaderGUI", "Controls", None, QtGui.QApplication.UnicodeUTF8))
		self.downbtn.setText(
			QtGui.QApplication.translate("DownloaderGUI", "Download", None, QtGui.QApplication.UnicodeUTF8))
		self.movebtn.setText(
			QtGui.QApplication.translate("DownloaderGUI", "Move", None, QtGui.QApplication.UnicodeUTF8))
		self.session.setText(
			QtGui.QApplication.translate("DownloaderGUI", "Save Session", None, QtGui.QApplication.UnicodeUTF8))
		self.progress.setTitle(
			QtGui.QApplication.translate("DownloaderGUI", "Progess", None, QtGui.QApplication.UnicodeUTF8))
		self.p2.setFormat(QtGui.QApplication.translate("DownloaderGUI", "%p%", None, QtGui.QApplication.UnicodeUTF8))
		self.p4.setFormat(QtGui.QApplication.translate("DownloaderGUI", "%p%", None, QtGui.QApplication.UnicodeUTF8))
		self.p5.setFormat(QtGui.QApplication.translate("DownloaderGUI", "%p%", None, QtGui.QApplication.UnicodeUTF8))
		self.p1.setFormat(QtGui.QApplication.translate("DownloaderGUI", "%p%", None, QtGui.QApplication.UnicodeUTF8))
		self.p3.setFormat(QtGui.QApplication.translate("DownloaderGUI", "%p%", None, QtGui.QApplication.UnicodeUTF8))
		self.p1l.setText(
			QtGui.QApplication.translate("DownloaderGUI", "Unallocated", None, QtGui.QApplication.UnicodeUTF8))
		self.p2l.setText(
			QtGui.QApplication.translate("DownloaderGUI", "Unallocated", None, QtGui.QApplication.UnicodeUTF8))
		self.p3l.setText(
			QtGui.QApplication.translate("DownloaderGUI", "Unallocated", None, QtGui.QApplication.UnicodeUTF8))
		self.p4l.setText(
			QtGui.QApplication.translate("DownloaderGUI", "Unallocated", None, QtGui.QApplication.UnicodeUTF8))
		self.p5l.setText(
			QtGui.QApplication.translate("DownloaderGUI", "Unallocated", None, QtGui.QApplication.UnicodeUTF8))
		self.p1d.setText(
			QtGui.QApplication.translate("DownloaderGUI", "No Details", None, QtGui.QApplication.UnicodeUTF8))
		self.p2d.setText(
			QtGui.QApplication.translate("DownloaderGUI", "No Details", None, QtGui.QApplication.UnicodeUTF8))
		self.p3d.setText(
			QtGui.QApplication.translate("DownloaderGUI", "No Details", None, QtGui.QApplication.UnicodeUTF8))
		self.p4d.setText(
			QtGui.QApplication.translate("DownloaderGUI", "No Details", None, QtGui.QApplication.UnicodeUTF8))
		self.p5d.setText(
			QtGui.QApplication.translate("DownloaderGUI", "No Details", None, QtGui.QApplication.UnicodeUTF8))
		self.tabs.setTabText(self.tabs.indexOf(self.dtab), QtGui.QApplication.translate("DownloaderGUI", "Main", None,
																						QtGui.QApplication.UnicodeUTF8))
		self.tabs.setTabToolTip(self.tabs.indexOf(self.dtab),
								QtGui.QApplication.translate("DownloaderGUI", "Main Downloader", None,
															 QtGui.QApplication.UnicodeUTF8))
		self.groupBox.setTitle(
			QtGui.QApplication.translate("DownloaderGUI", "Locations", None, QtGui.QApplication.UnicodeUTF8))
		self.dloc.setToolTip(
			QtGui.QApplication.translate("DownloaderGUI", "Download Location", None, QtGui.QApplication.UnicodeUTF8))
		self.dloc.setText(
			QtGui.QApplication.translate("DownloaderGUI", "downloads", None, QtGui.QApplication.UnicodeUTF8))
		self.msrc.setToolTip(
			QtGui.QApplication.translate("DownloaderGUI", "Move SRC", None, QtGui.QApplication.UnicodeUTF8))
		self.msrc.setText(
			QtGui.QApplication.translate("DownloaderGUI", "downloads", None, QtGui.QApplication.UnicodeUTF8))
		self.mdest.setToolTip(
			QtGui.QApplication.translate("DownloaderGUI", "Move Dest", None, QtGui.QApplication.UnicodeUTF8))
		self.mdest.setText(QtGui.QApplication.translate("DownloaderGUI", "F:\\", None, QtGui.QApplication.UnicodeUTF8))
		self.groupBox_2.setTitle(
			QtGui.QApplication.translate("DownloaderGUI", "Download", None, QtGui.QApplication.UnicodeUTF8))
		self.pushButton_3.setText(
			QtGui.QApplication.translate("DownloaderGUI", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
		self.groupBox_3.setTitle(
			QtGui.QApplication.translate("DownloaderGUI", "SuperUser", None, QtGui.QApplication.UnicodeUTF8))
		self.label.setText(
			QtGui.QApplication.translate("DownloaderGUI", "SuperUser Password", None, QtGui.QApplication.UnicodeUTF8))
		self.pushButton.setText(
			QtGui.QApplication.translate("DownloaderGUI", "Activate SuperUser", None, QtGui.QApplication.UnicodeUTF8))
		self.groupBox_5.setTitle(
			QtGui.QApplication.translate("DownloaderGUI", "GroupBox", None, QtGui.QApplication.UnicodeUTF8))
		self.groupBox_4.setTitle(
			QtGui.QApplication.translate("DownloaderGUI", "GroupBox", None, QtGui.QApplication.UnicodeUTF8))
		self.tabs.setTabText(self.tabs.indexOf(self.otab),
							 QtGui.QApplication.translate("DownloaderGUI", "Options", None,
														  QtGui.QApplication.UnicodeUTF8))
		self.tabs.setTabToolTip(self.tabs.indexOf(self.otab),
								QtGui.QApplication.translate("DownloaderGUI", "Options for Downloading and Moving",
															 None, QtGui.QApplication.UnicodeUTF8))
		self.tabs.setTabText(self.tabs.indexOf(self.atab), QtGui.QApplication.translate("DownloaderGUI", "About", None,
																						QtGui.QApplication.UnicodeUTF8))
		self.tabs.setTabToolTip(self.tabs.indexOf(self.atab),
								QtGui.QApplication.translate("DownloaderGUI", "Help and About", None,
															 QtGui.QApplication.UnicodeUTF8))
