from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QFontMetrics
from PyQt5.QtWidgets import QTextEdit, QFrame

from TTGraphics import getAnchoredGeometryRect

class TodoTextWidget(QTextEdit):
    font = QFont("Century Gothic", 12, QFont.Medium)
    fontmetrics = QFontMetrics(font)

    def __init__(self, parent, text):
        super().__init__(parent)
        # Margin is only the first thing to remember, there's also line-breaks, line-distance,
        # word-wrap (and the empty space it creates), etc.
        self.margin = self.document().documentMargin()

        self.initTodoText(text)

    def initTodoText(self, text):
        qfm = QFontMetrics(self.font)
        print("Text width: ", qfm.width(text))

        self.setText(text)
        self.setFont(self.font)
        self.setAlignment(Qt.AlignCenter)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setActive(False)
        self.textChanged.connect(self.updateSize)

    def setGeometry(self, x, y, width, height):
        super().setGeometry(x, y, width, height)

    def updateSize(self):
        super().setGeometry(self.x(), self.y(), self.width(), self.height())

    # http://www.qtcentre.org/threads/20332-QGraphicsTextItem-and-text-cursor-position-via-QPoint
    def mousePressEvent(self, QMouseEvent):
        self.setActive(True)
        henk = super().textCursor()

        # Goddamn genius:
        super().mousePressEvent(QMouseEvent)



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
        return self.fontmetrics.width(self.toPlainText()) + (2*self.margin)

    def height(self):
        return self.fontmetrics.height() + (2*self.margin)

    def textRect(self):
        return self.contentsRect()