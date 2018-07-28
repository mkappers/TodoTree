import sys
import unittest

import TTConstants as TTC

from PyQt5.QtWidgets import QApplication

from ttcore import TodoItem, TodoItemState
from ttgraphics.canvas import CanvasSystem
from ttgraphics.TodoItemWidget import TodoItemWidget
from ttphysics import Vector2, Edge

class TestGraphics:
    def __init__(self):
        self.canvas = CanvasSystem(width = 600, height = 200)
        self.init_widgets()
        self.init_points()
        self.init_lines()

    def init_widgets(self):
        done = TodoItemWidget(self.canvas, TodoItemState.DONE, "done", None, None, 100, 100)
        todo = TodoItemWidget(self.canvas, TodoItemState.TODO, "todo", None, None, 300, 100)
        pdone = TodoItemWidget(self.canvas, TodoItemState.PARENTDONE, "pdone", None, None, 500, 100)

        print(done.textwidget.document().documentMargin())

    def init_points(self):
        self.canvas.addPointReference(Vector2(100,100))

    def init_lines(self):
        self.canvas.addLineReference(Edge(Vector2(0, 100), Vector2(200, 100)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    testplatform = TestGraphics()
    sys.exit(app.exec_())
