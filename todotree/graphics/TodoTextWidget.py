from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QFontMetrics
from PyQt5.QtWidgets import QTextEdit, QFrame

from TTGraphics import getAnchoredGeometryRect

class TodoTextWidget(QTextEdit):
    resized = pyqtSignal()

    def __init__(self, parent, text):
        super().__init__(parent)

        # Set text, font, alignment, scrollbar policy, and frame style
        self.setText(text)
        self.setFont(QFont("Century Gothic", 12, QFont.Medium))
        self.setAlignment(Qt.AlignCenter)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setFrameStyle(QFrame.NoFrame)

        # Adjust textwidget size to text
        self.update_size()
        self.set_active(False)

        self.textChanged.connect(self.update_size)

    def update_size(self):
        """Sets widget size to be equal to (encapsulated) document size."""
        self.document().adjustSize()
        self.resize(self.width(), self.height())
        self.resized.emit()

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

    def height(self):
        return self.document().size().height()