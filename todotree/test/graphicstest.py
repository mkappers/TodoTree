import sys
sys.path.append(r"C:\Users\Maurits\Python\Projects\TodoTree")

import unittest

from PyQt5.QtWidgets import QApplication

from todotree.core import TodoItem, TodoItemState
from todotree.graphics.canvas import CanvasSystem
from todotree.graphics.TodoItemWidget import TodoItemWidget
from todotree.graphics.TodoIconWidget import TodoIconWidget
from todotree.graphics.widgetPositionWrapper import AnchorPositionWrapper, HorizontalAnchor, VerticalAnchor
from todotree.physics import Vector2, Edge

class TestGraphics:
    def __init__(self):
        self.canvas = CanvasSystem(width = 600, height = 400)
        self.init_widgets()
        self.init_position_wrappers()
        # self.init_points()
        # self.init_lines()

    def init_widgets(self):
        done = TodoItemWidget(self.canvas, TodoItemState.DONE, "done", None, None, 100, 100)
        todo = TodoItemWidget(self.canvas, TodoItemState.TODO, "todo", None, None, 300, 100)
        pdone = TodoItemWidget(self.canvas, TodoItemState.PARENTDONE, "pdone", None, None, 500, 100)

        print(done.textwidget.document().documentMargin())

    def init_position_wrappers(self):
        icon = TodoIconWidget(None)
        icon2 = TodoIconWidget(None, TodoItemState.DONE)
        wrapper = AnchorPositionWrapper(self.canvas, icon)
        wrapper2 = AnchorPositionWrapper.with_anchor(self.canvas, icon2, HorizontalAnchor.RIGHT, VerticalAnchor.BOTTOM)

        wrapper.set_render_anchor(HorizontalAnchor.CENTER, VerticalAnchor.CENTER)
        wrapper.move(100, 300)
        wrapper2.move(20, 300)

    def init_points(self):
        self.canvas.addPointReference(Vector2(100,100))

    def init_lines(self):
        self.canvas.addLineReference(Edge(Vector2(0, 100), Vector2(200, 100)))
        self.canvas.addLineReference(Edge(Vector2(100, 0), Vector2(100, 400)))
        self.canvas.addLineReference(Edge(Vector2(0, 300), Vector2(600, 300)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    testplatform = TestGraphics()
    sys.exit(app.exec_())
