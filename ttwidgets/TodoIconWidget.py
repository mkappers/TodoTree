import TTConstants as TTC

from TTGraphics import HollowRoundedRectanglePath, getAnchoredGeometryRect

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QWidget

class TodoIconWidget(QWidget):
    __state = None
    qpainter = QPainter()

    todo_icon = None
    done_icon = None

    updateTimer = QTimer()

    __size = None

    # rimsize = None
    curdonerim = 0

    def __init__(self, parent, state = TTC.TodoItemState.TODO):
        super().__init__(parent)

        self.__state = state

        self.updateTimer.setSingleShot(False)
        self.updateTimer.timeout.connect(self.rimUpdate)
        self.updateTimer.start(10)

    def setGeometry(self, anchor, x, y, width, height):
        self.todo_icon = HollowRoundedRectanglePath(width, height)
        self.done_icon = HollowRoundedRectanglePath(width, height, self.curdonerim)

        super().setGeometry(getAnchoredGeometryRect(x,y,width,height,anchor))

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
        if self.__state == TTC.TodoItemState.TODO:
            self.__state = TTC.TodoItemState.DONE
        elif self.__state == TTC.TodoItemState.DONE:
            self.__state = TTC.TodoItemState.PARENTDONE
        elif self.__state == TTC.TodoItemState.PARENTDONE:
            self.__state = TTC.TodoItemState.TODO

    def rimUpdate(self):
        if self.__state == TTC.TodoItemState.DONE and self.curdonerim < 100:
            self.curdonerim += 5
        elif self.__state == TTC.TodoItemState.TODO and self.curdonerim > 0:
            self.curdonerim -= 5
        elif self.__state == TTC.TodoItemState.PARENTDONE:
            if self.curdonerim > TTC.ICON_RIM_SIZE:
                self.curdonerim -= 5
            elif self.curdonerim < TTC.ICON_RIM_SIZE:
                self.curdonerim += 5

        self.done_icon.updateRim(self.curdonerim)
        self.update()

    def size(self):
        return self.__size