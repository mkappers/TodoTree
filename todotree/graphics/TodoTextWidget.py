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
        self.margin = 10 #self.document().documentMargin()
        self.init_todo_text(text)

    def init_todo_text(self, text):
        qfm = QFontMetrics(self.font)
        print("Text width: ", qfm.width(text))

        # Set text, font, alignment, scrollbar policy, and frame style
        self.setText(text)
        self.setFont(self.font)
        self.setAlignment(Qt.AlignCenter)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setFrameStyle(QFrame.NoFrame)

        # Adjust textwidget size to text
        self.document().adjustSize()
        self.set_active(False)

        self.textChanged.connect(self.update_size)

    def setGeometry(self, x, y):
        super().setGeometry(x, y, self.document().size().width(), self.document().size().height())

    def update_size(self):
        self.document().adjustSize()
        super().setGeometry(self.x(), self.y(), self.width(), self.height())

    # http://www.qtcentre.org/threads/20332-QGraphicsTextItem-and-text-cursor-position-via-QPoint
    def mousePressEvent(self, QMouseEvent):
        self.set_active(True)
        super().mousePressEvent(QMouseEvent)

    def set_active(self, active):
        if active:
            self.__activate()
        else:
            self.__deactivate()

    def __activate(self):
        """Makes the text available for editing."""
        self.viewport().setAutoFillBackground(True)
        super().setTextInteractionFlags(Qt.TextEditorInteraction)

    def __deactivate(self):
        """Makes the text uneditable."""
        self.viewport().setAutoFillBackground(False)
        super().setTextInteractionFlags(Qt.NoTextInteraction)

    def width(self):
        return self.document().size().width()
        #return self.fontmetrics.width(self.toPlainText()) + (2*self.margin)

    def height(self):
        return self.document().size().height()
        #return self.fontmetrics.height() + (2*self.margin)