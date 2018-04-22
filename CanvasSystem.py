from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget

class CanvasSystem(QWidget):
    def __init__(self):
        super().__init__()
        self.qpainter = QPainter()

        self.pointrefs = []
        self.linerefs = []

        self.initWindow()

    def initWindow(self):
        self.setGeometry(600, 400, 400, 400)
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