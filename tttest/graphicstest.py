import sys
import unittest

import TTConstants as TTC

from PyQt5.QtWidgets import QApplication

from ttcore import TodoItem
from ttgraphics.canvas import CanvasSystem
from ttgraphics.TodoIconWidget import TodoIconWidget
from ttgraphics.TodoItemWidget import TodoItemWidget
from ttphysics import Vector2, Edge

class TestGraphics:
    def __init__(self):
        self.canvas = CanvasSystem(width = 600, height = 200)
        self.initWidgets()
        self.initPoints()
        self.initLines()

    def initWidgets(self):
        a = TodoIconWidget(self.canvas)
        a.setGeometry(TTC.GeometryAnchor.CENTER, 100, 100, 40, 40)

        b = TodoItemWidget(self.canvas, TodoItem(TTC.TodoItemState.DONE, "Henk"))
        b.setPosition(300, 100, TTC.GeometryAnchor.CENTER)
        b.show()

    def initPoints(self):
        self.canvas.addPointReference(Vector2(100,100))

    def initLines(self):
        self.canvas.addLineReference(Edge(Vector2(0, 100), Vector2(200, 100)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    testplatform = TestGraphics()
    sys.exit(app.exec_())
