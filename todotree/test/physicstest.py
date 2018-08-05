import sys
import unittest

import TTConstants as TTC

from PyQt5.QtWidgets import QApplication

from core import TodoItem, TodoItemState
from graphics.canvas import CanvasSystem
from graphics.TodoIconWidget import TodoIconWidget
from physics import Vector2, Spring, System

class TestGraphics:
    def __init__(self):
        self.canvas = CanvasSystem(width = 600, height = 200)
        self.physics = System()
        self.init_widgets()

    def init_items(self):
        a = TodoIconWidget(self.canvas)
        b = TodoIconWidget(self.canvas)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    testplatform = TestGraphics()
    sys.exit(app.exec_())
