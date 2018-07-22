from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QFontMetrics
from PyQt5.QtWidgets import QTextEdit, QFrame

from TTGraphics import getAnchoredGeometryRect

class TodoTextWidget(QTextEdit):
    font = QFont("Century Gothic", 12, QFont.Medium)
    fontmetrics = QFontMetrics(font)

    def __init__(self, parent, text):
        super().__init__(parent)

        self.initTodoText(text)
        print(self.contentsRect())

    def initTodoText(self, text):
        qfm = QFontMetrics(self.font)
        print("Text width: ", qfm.width(text))

        self.setText(text)
        self.setFont(self.font)
        self.setAlignment(Qt.AlignCenter)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setActive(False)

    # http://www.qtcentre.org/threads/20332-QGraphicsTextItem-and-text-cursor-position-via-QPoint
    def mousePressEvent(self, QMouseEvent):
        self.setActive(True)
        henk = super().textCursor()

        # Goddamn genius:
        super().mousePressEvent(QMouseEvent)

    def setGeometry(self, anchor, x, y, width, height):
        super().setGeometry(getAnchoredGeometryRect(x, y, width, height, anchor))

    def setActive(self, active):
        if active:
            self.__activate()
        else:
            self.__deactivate()

    def __activate(self):
        self.viewport().setAutoFillBackground(True)
        super().setTextInteractionFlags(Qt.TextEditorInteraction)

    def __deactivate(self):
        self.viewport().setAutoFillBackground(False)
        self.setFrameStyle(QFrame.NoFrame)

        super().setTextInteractionFlags(Qt.NoTextInteraction)

    def width(self):
        return self.fontmetrics.width(self.toPlainText())

    def height(self):
        # 10 should become the margins.
        return self.fontmetrics.height() + 10

    def textRect(self):
        return self.contentsRect()