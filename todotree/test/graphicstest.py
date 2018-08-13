import sys
sys.path.append(r"C:\Users\Maurits\Python\Projects\TodoTree")

import unittest

from PyQt5.QtWidgets import QApplication

from todotree.core import TodoItem, TodoItemState
from todotree.graphics.canvas import CanvasSystem
from todotree.graphics.TodoItemWidget import TodoItemWidget
from todotree.graphics.TodoIconWidget import TodoIconWidget
from todotree.graphics.TodoTextWidget import TodoTextWidget
from todotree.graphics.widgetPositionWrapper import AnchorPositionWrapper, HorizontalAnchor, VerticalAnchor
from todotree.physics import Vector2, Edge

class TestGraphics:
    def __init__(self):
        self.canvas = CanvasSystem(width = 600, height = 250)
        self.init_widgets()
        # self.init_points()
        self.init_lines()

    def init_widgets(self):

        done = AnchorPositionWrapper(self.canvas,  TodoItemWidget(self.canvas, TodoItemState.DONE, "done", None, None))
        done.set_render_anchor(HorizontalAnchor.CENTER, VerticalAnchor.TOP)
        done.move(100, 100)
        done.show()

        todo = TodoItemWidget(self.canvas, TodoItemState.TODO, "todo", None, None)
        todo.move(300, 100)
        todo.show()

        pdoneicon = AnchorPositionWrapper.with_anchor(self.canvas, TodoIconWidget(None, TodoItemState.PARENTDONE), HorizontalAnchor.CENTER, VerticalAnchor.TOP)
        pdoneicon.move(500, 100)
        pdoneicon.show()
        pdonetext = AnchorPositionWrapper.with_anchor(self.canvas, TodoTextWidget(None, "parent done"), HorizontalAnchor.CENTER, VerticalAnchor.TOP)
        pdonetext.move(500, 144)
        pdonetext.show()

    def init_points(self):
        self.canvas.addPointReference(Vector2(100,100))

    def init_lines(self):
        self.canvas.addLineReference(Edge(Vector2(0, 100), Vector2(600, 100)))
        self.canvas.addLineReference(Edge(Vector2(100, 0), Vector2(100, 250)))
        self.canvas.addLineReference(Edge(Vector2(300, 0), Vector2(300, 250)))
        self.canvas.addLineReference(Edge(Vector2(500, 0), Vector2(500, 250)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    testplatform = TestGraphics()
    sys.exit(app.exec_())
