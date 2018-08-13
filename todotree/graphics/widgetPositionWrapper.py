import math

from PyQt5.QtCore import QEvent, pyqtSignal
from PyQt5.QtWidgets import QWidget

from enum import Enum


class HorizontalAnchor(Enum):
    LEFT = 1
    CENTER = 2
    RIGHT = 3


class VerticalAnchor(Enum):
    TOP = 1
    CENTER = 2
    BOTTOM = 3


class AnchorPositionWrapper(QWidget):
    """AnchorPositionWrapper(QWidget)

    An AnchorPositionWrapper instance has no size of its own, it will always have the size of its childrenRect().
    """
    resized = pyqtSignal()

    def __init__(self, parent, widget):
        super().__init__(parent)

        self.widget = widget
        self.widget.setParent(self)
        self.widget.move(0, 0)
        self.widget.resized.connect(self.resize_to_widget)

        self.anchor_x = 0
        self.anchor_y = 0

        self.x_function = lambda x: x
        self.y_function = lambda y: y
        self.resize_to_widget()

    @classmethod
    def with_anchor(cls, parent, widget: QWidget, horizontal: HorizontalAnchor, vertical: VerticalAnchor):
        returnWrapper = cls(parent, widget)
        returnWrapper.set_render_anchor(horizontal, vertical)

        return returnWrapper

    def move(self, x, y):
        self.anchor_x = x
        self.anchor_y = y

        super().move(self.x_function(x), self.y_function(y))

    def resize_to_widget(self):
        self.resize(self.childrenRect().size())
        self.move(self.anchor_x, self.anchor_y)
        self.resized.emit()

    def set_render_anchor(self, horizontal: HorizontalAnchor, vertical: VerticalAnchor):
        if (horizontal == HorizontalAnchor.CENTER):
            self.x_function = lambda x: x - math.floor(self.width() / 2.0)
        elif(horizontal == HorizontalAnchor.RIGHT):
            self.x_function = lambda x: x - (self.width())
        else:
            self.x_function = lambda x: x

        if (vertical == VerticalAnchor.CENTER):
            self.y_function = lambda y: y - math.floor(self.height() / 2.0)
        elif (vertical == VerticalAnchor.BOTTOM):
            self.y_function = lambda y: y - (self.height())
        else:
            self.y_function = lambda y: y