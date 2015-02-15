from PySide import QtGui, QtCore
import sys, os


class MyClassItem(QtGui.QListWidgetItem):
    def __init__(self, parent=None):
        super(QtGui.QListWidgetItem, self).__init__(parent)


class ThumbListWidget(QtGui.QListWidget):
    def __init__(self, type, parent=None):
        super(ThumbListWidget, self).__init__(parent)
        self.setIconSize(QtCore.QSize(124, 124))
        self.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            super(ThumbListWidget, self).dragEnterEvent(event)

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
        else:
            super(ThumbListWidget, self).dragMoveEvent(event)

    def dropEvent(self, event):
        print 'dropEvent', event
        if event.mimeData().hasUrls():
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
            links = []
            for url in event.mimeData().urls():
                links.append(str(url.toLocalFile()))
            self.emit(QtCore.SIGNAL("dropped"), links)
        else:
            event.setDropAction(QtCore.Qt.MoveAction)
            super(ThumbListWidget, self).dropEvent(event)


class Dialog_01(QtGui.QMainWindow, MyClassItem):
    def __init__(self):
        super(Dialog_01, self).__init__()
        self.listItems={}

        myQWidget = QtGui.QWidget()
        myBoxLayout = QtGui.QVBoxLayout()
        myQWidget.setLayout(myBoxLayout)
        self.setCentralWidget(myQWidget)

        self.listWidgetA = ThumbListWidget(self)
        self.listWidgetB = ThumbListWidget(self)

        for i in range(7):
            listItemAInstance=MyClassItem()
            listItemAInstance.setText('A'+'%04d'%i)
            listItemAInstance.setBackgroundColor(QtCore.Qt.darkGray)
            if i%2: listItemAInstance.setBackgroundColor(QtCore.Qt.gray)
            self.listWidgetA.addItem(listItemAInstance)

            listItemBInstance=MyClassItem()
            listItemBInstance.setText('B'+'%04d'%i)

            if i%2: listItemBInstance.setBackgroundColor(QtCore.Qt.lightGray)
            self.listWidgetB.addItem(listItemBInstance)

        myBoxLayout.addWidget(self.listWidgetA)

        myBoxLayout.addWidget(self.listWidgetB)
        self.connect(self.listWidgetA, QtCore.SIGNAL("dropped"), self.droppedOnA)
        self.connect(self.listWidgetB, QtCore.SIGNAL("dropped"), self.droppedOnB)


    def droppedOnA(self, arg):
        print '\n\t droppedOnA', arg.text

    def droppedOnB(self, arg):
        print '\n\t droppedOnB', arg.text


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    dialog_1 = Dialog_01()
    dialog_1.show()
    dialog_1.resize(480,320)
    sys.exit(app.exec_())