# Using a QWindow and QPainterPath (and QPropertyAnimation) to animate a todoitem
# http://doc.qt.io/qt-5/qtgui-index.html
# http://doc.qt.io/qt-5/qguiapplication.html
# http://doc.qt.io/qt-5/qwindow.html
# http://doc.qt.io/qt-5/paintsystem.html
# http://doc.qt.io/qt-5/qpainterpath.html

import sys

import TTConstants as TTC
from core.TodoItemOld import TodoItem
from graphics.TodoItemWidget import TodoItemWidget
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget, QApplication


# https://stackoverflow.com/questions/1337523/measuring-text-width-in-qt
# QString == Py3 str (as in str())



class ParentWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.updateTimer = QTimer()
        self.initUI()

        # self.updateTimer.setSingleShot(False)
        # self.updateTimer.timeout.connect(self.doUpdate)
        # self.updateTimer.start(2)

    def initUI(self):
        self.setWindowTitle("Parent Windows")
        self.setGeometry(300,150,800,600)
        TodoItem(None, TTC.TodoItemState.TODO, "Test Todo Item", self)
        #self.ti = TodoItemWidget(self, TodoItem(description = "Henkie Sperma Tankie"))
        self.tempx = 150
        #self.ti.set_position(self.tempx,100,TTC.GeometryAnchor.TOP_CENTER)
        #TodoItem(self, 600, 400, 60,60, 14, 14)
        self.show()

    def doUpdate(self):
        self.tempx += 0.5
        self.ti.set_position(self.tempx, 100, TTC.GeometryAnchor.TOP_CENTER)

        self.update()
    # def updateStuff(self):
        # self.ti.


if __name__ == '__main__':

    app = QApplication(sys.argv)
    iat = ParentWidget()
    sys.exit(app.exec_())