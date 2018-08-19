from todotree.core import TodoItemState
from TTGraphics import HollowRoundedRectanglePath, getAnchoredGeometryRect

from PyQt5.QtCore import Qt, QTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QWidget

class TodoIconWidget(QWidget):
    resized = pyqtSignal()
    state_changed = pyqtSignal()

    def __init__(self, parent, state = TodoItemState.TODO, side_length = 40):
        super().__init__(parent)

        self.curdonerim = 0
        self.resize(side_length, side_length)

        self.todo_icon = HollowRoundedRectanglePath(self.side_length, self.side_length)
        self.done_icon = HollowRoundedRectanglePath(self.side_length, self.side_length, self.curdonerim)

        self.state = state
        self.qpainter = QPainter()
        self.set_update_timer(10)

    @property
    def side_length(self):
        return self.width()

    def set_size(self, side_length):
        self.resize(side_length, side_length)
        self.resized.emit()

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
        if self.state == TodoItemState.TODO:
            self.set_state(TodoItemState.DONE)
        elif self.state == TodoItemState.DONE:
            self.set_state(TodoItemState.PARENTDONE)
        elif self.state == TodoItemState.PARENTDONE:
            self.set_state(TodoItemState.TODO)
    
    def set_state(self, state: TodoItemState):
        self.state = state
        self.state_changed.emit()

    def rim_update(self):
        if self.state == TodoItemState.DONE and self.curdonerim < 100:
            self.curdonerim += 5
        elif self.state == TodoItemState.TODO and self.curdonerim > 0:
            self.curdonerim -= 5
        elif self.state == TodoItemState.PARENTDONE:
            if self.curdonerim > self.side_length:
                self.curdonerim -= 5
            elif self.curdonerim < self.side_length:
                self.curdonerim += 5

        self.done_icon.updateRim(self.curdonerim)
        self.update()

    def set_update_timer(self, milliseconds):
        self.updateTimer = QTimer()
        self.updateTimer.setSingleShot(False)
        self.updateTimer.timeout.connect(self.rim_update)
        self.updateTimer.start(milliseconds)
