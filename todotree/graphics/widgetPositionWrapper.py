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


class RenderPositionWrapper(QWidget):
    def __init__(self, parent, widget: QWidget):
        super().__init__(parent)
        self.widget = widget
        self.widget.setGeometry(0,0,self.widget.width, self.widget.height)

        self.x_function = lambda x: x
        self.y_function = lambda y: y

    def set_position(self, x, y):
        self.setGeometry(self.x_function(x), self.y_function(y), self.widget.width, self.widget.height)
        self.show()

    def set_render_anchor(self, horizontal: HorizontalAnchor, vertical: VerticalAnchor):
        if (horizontal == HorizontalAnchor.CENTER):
            self.x_function = lambda x: x - (self.widget.width / 2)
        elif(horizontal == HorizontalAnchor.RIGHT):
            self.x_function = lambda x: x - (self.widget.width)
        else:
            self.x_function = lambda x: x

        if (vertical == VerticalAnchor.CENTER):
            self.y_function = lambda y: y - (self.widget.height / 2)
        elif (vertical == VerticalAnchor.BOTTOM):
            self.y_function = lambda y: y - (self.widget.height)
        else:
            self.y_function = lambda y: y


'''
    class Anchor(Enum):
        CENTER = 1
        TOP_LEFT = 2
        TOP_CENTER = 3
        TOP_RIGHT = 4
        RIGHT_CENTER = 5
        LEFT_CENTER = 6
        BOTTOM_LEFT = 7
        BOTTOM_CENTER = 8
        BOTTOM_RIGHT = 9
'''