#File containing the TodoItem class

import math

from todotree.graphics.todoiconwidget import TodoIconWidget
from todotree.graphics.todotextwidget import TodoTextWidget
from todotree.graphics.anchor_position_wrapper import AnchoredWidgetWrapper, HorizontalAnchor, VerticalAnchor

from PyQt5.QtCore import QEvent, pyqtSignal
from PyQt5.QtWidgets import QWidget

# TodoItem should also have physics node properties, and have kids and parents and shit, but shouldn't have that
# internally

# Should just have Icon, State, and Text
# TodoItemWidget anchor is center of icon

from todotree.core import TodoNode

class TodoItemWidget(QWidget):
    resized = pyqtSignal()

    def __init__(self, parent, state, description, nodeparent, nodechildren):
        super().__init__(parent)

        self.todonode = TodoNode(state, description, nodeparent, nodechildren)
        self.icon = AnchoredWidgetWrapper.with_anchor(self, TodoIconWidget(None, state), HorizontalAnchor.CENTER, VerticalAnchor.TOP)
        self.text = AnchoredWidgetWrapper.with_anchor(self, TodoTextWidget(None, description), HorizontalAnchor.CENTER, VerticalAnchor.TOP)

        self.icon.resized.connect(self.resize_to_children)
        self.text.resized.connect(self.resize_to_children)
        self.text.widget.textChanged.connect(self.update_description)
        self.text.widget.update()

        self.resize_to_children()

    @classmethod
    def from_todo_item(cls, parent, todoitem):
        return cls(parent, todoitem.state, todoitem.description, None, None)

    @classmethod
    def from_todo_node(cls, parent, todonode):
        return cls(parent, todonode.state, todonode.description, todonode.parent, todonode.children)

    def resize_to_children(self):
        width = max(self.icon.width(), self.text.width())
        height = self.icon.height() + self.text.height() + 4
        center = math.floor(width / 2)

        self.resize(width, height)
        self.icon.move(center, 0)
        self.text.move(center, self.icon.widget.side_length + 4)

        self.resized.emit()

    def update_description(self):
        self.todonode.set_description(self.text.widget.toPlainText())

    def state(self):
        return self.iconwidget.state

    def description(self):
        return self.text.widget.toPlainText()







