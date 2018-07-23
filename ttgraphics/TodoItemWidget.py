#File containing the TodoItem class

import TTConstants as TTC

from ttcore import TodoItem
from TTGraphics import getAnchoredGeometryRect
from ttgraphics.TodoIconWidget import TodoIconWidget
from ttgraphics.TodoTextWidget import TodoTextWidget

from PyQt5.QtWidgets import QWidget

# TodoItem should also have physics node properties, and have kids and parents and shit, but shouldn't have that
# internally

# Should just have Icon, State, and Text
# TodoItemWidget anchor is center of icon

from ttcore import TodoNode

class TodoItemWidget(QWidget):
    iconsize = 30

    def __init__(self, parent, state, description, nodeparent, nodechildren, x, y):
        super().__init__(parent)

        self.todonode = TodoNode(state, description, nodeparent, nodechildren)
        self.iconwidget = TodoIconWidget(self, state)
        self.textwidget = TodoTextWidget(self, description)
        self.textwidget.update()

        self.textwidget.textChanged.connect(self.updateTextWidgetSize)

        self.ox = x
        self.oy = y
        self.setPosition(x, y)
        self.show()

    @classmethod
    def fromTodoItem(cls, parent, todoitem, x, y):
        return cls(parent, todoitem.state, todoitem.description, None, None, x, y)

    @classmethod
    def fromTodoNode(cls, parent, todonode, x, y):
        return cls(parent, todonode.state, todonode.description, todonode.parent, todonode.children)

    def setPosition(self, x, y):
        width = max(self.iconsize, self.textwidget.width())
        height = self.iconsize + self.textwidget.height() + 4

        #self.iconwidget.setGeometry(0, 0, self.iconsize, self.iconsize)
        self.iconwidget.setGeometry((width / 2) - (self.iconsize / 2), 0, self.iconsize, self.iconsize)
        self.textwidget.setGeometry(0, self.iconsize + 4, self.textwidget.width(), self.textwidget.height())

        super().setGeometry(x - (width / 2), y - (self.iconsize / 2), width, height)

    # def __update_size(self):
    #     ir = self.icon.geometry()
    #     tr = self.text.geometry()
    #
    #     self.width = max(ir.width(), tr.width())
    #     self.height = max(ir.height(), tr.height())

    def updateTextWidgetSize(self):
        self.setPosition(self.ox,self.oy)

    def state(self):
        return self.iconwidget.state

    def description(self):
        return self.textwidget.toPlainText()






