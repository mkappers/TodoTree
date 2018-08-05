from core import TodoItemState as TIS
from TTGraphics import HollowRoundedRectanglePath, getAnchoredGeometryRect

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QWidget

class TodoIconWidget(QWidget):
    __state = None

    todo_icon = None
    done_icon = None

    qpainter = QPainter()
    updateTimer = QTimer()

    __size = None

    # rimsize = None
    curdonerim = 0
    rimsize = 40

    def __init__(self, parent, state = TIS.TODO):
        super().__init__(parent)

        self.__state = state

        self.updateTimer.setSingleShot(False)
        self.updateTimer.timeout.connect(self.rim_update)
        self.updateTimer.start(10)

    def setGeometry(self, x, y, width, height):
        self.width = width
        self.height = height

        self.todo_icon = HollowRoundedRectanglePath(width, height)
        self.done_icon = HollowRoundedRectanglePath(width, height, self.curdonerim)

        super().setGeometry(x, y, width, height)
        self.show()

    def set_position(self, x, y):
        super().setGeometry(x, y, self.width, self.height)

    def paintEvent(self, event):
        self.qpainter.begin(self)
        self.qpainter.setRenderHint(QPainter.Antialiasing)
        self.qpainter.setPen(QPen(Qt.NoPen))

        self.qpainter.setBrush(QColor(244, 67, 54))
        self.qpainter.drawPath(self.todo_icon.getPath())

        self.qpainter.setBrush(QColor(76, 175, 80))
        self.qpainter.drawPath(self.done_icon.getPath())

        self.qpainter.end()

    def mousePressEvent(self, QMouseEvent):
        print("Click!")
        if self.__state == TIS.TODO:
            self.__state = TIS.DONE
        elif self.__state == TIS.DONE:
            self.__state = TIS.PARENTDONE
        elif self.__state == TIS.PARENTDONE:
            self.__state = TIS.TODO

    def rim_update(self):
        if self.__state == TIS.DONE and self.curdonerim < 100:
            self.curdonerim += 5
        elif self.__state == TIS.TODO and self.curdonerim > 0:
            self.curdonerim -= 5
        elif self.__state == TIS.PARENTDONE:
            if self.curdonerim > self.rimsize:
                self.curdonerim -= 5
            elif self.curdonerim < self.rimsize:
                self.curdonerim += 5

        self.done_icon.updateRim(self.curdonerim)
        self.update()

    def set_size(self, width, height):
        self.width = width
        self.height = height

    def size(self):
        return self.__size