from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget

class CanvasSystem(QWidget):
    def __init__(self, x = 600, y = 400, width = 400, height = 400):
        super().__init__()
        self.qpainter = QPainter()

        self.pointrefs = []
        self.linerefs = []

        self.initWindow(x, y, width, height)

    def initWindow(self, x, y, width, height):
        self.setGeometry(x, y, width, height)
        self.show()

    def addPointReference(self, position):
        self.pointrefs.append(position)

    def addLineReference(self, edge):
        self.linerefs.append(edge)

    def paintEvent(self, QPaintEvent):
        self.qpainter.begin(self)

        for point in self.pointrefs:
            self.qpainter.drawRect(QRectF(point.x - 5, point.y - 5, 10, 10))

        for line in self.linerefs:
            self.qpainter.drawLine(line.a.x, line.a.y, line.b.x, line.b.y)

        self.qpainter.end()