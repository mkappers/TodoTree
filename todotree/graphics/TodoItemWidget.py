#File containing the TodoItem class

from graphics.TodoIconWidget import TodoIconWidget
from graphics.TodoTextWidget import TodoTextWidget

from PyQt5.QtWidgets import QWidget

# TodoItem should also have physics node properties, and have kids and parents and shit, but shouldn't have that
# internally

# Should just have Icon, State, and Text
# TodoItemWidget anchor is center of icon

from core import TodoNode

class TodoItemWidget(QWidget):
    iconsize = 30

    def __init__(self, parent, state, description, nodeparent, nodechildren, x, y):
        super().__init__(parent)

        self.todonode = TodoNode(state, description, nodeparent, nodechildren)
        self.iconwidget = TodoIconWidget(self, state)
        self.textwidget = TodoTextWidget(self, description)
        self.textwidget.update()

        self.textwidget.textChanged.connect(self.update_text_widget_size)

        self.ox = x
        self.oy = y
        self.set_position(x, y)
        self.show()

    @classmethod
    def from_todo_item(cls, parent, todoitem, x, y):
        return cls(parent, todoitem.state, todoitem.description, None, None, x, y)

    @classmethod
    def from_todo_node(cls, parent, todonode, x, y):
        return cls(parent, todonode.state, todonode.description, todonode.parent, todonode.children)

    def set_position(self, x, y):
        width = max(self.iconsize, self.textwidget.width())
        height = self.iconsize + self.textwidget.height() + 4

        #self.iconwidget.setGeometry(0, 0, self.iconsize, self.iconsize)
        self.iconwidget.setGeometry((width / 2) - (self.iconsize / 2), 0, self.iconsize, self.iconsize)
        self.textwidget.setGeometry((width / 2) - (self.textwidget.width() / 2), self.iconsize + 4)

        super().setGeometry(x - (width / 2), y - (self.iconsize / 2), width, height)

    # def __update_size(self):
    #     ir = self.icon.geometry()
    #     tr = self.text.geometry()
    #
    #     self.width = max(ir.width(), tr.width())
    #     self.height = max(ir.height(), tr.height())

    def update_text_widget_size(self):
        self.set_position(self.ox, self.oy)
        self.todonode.set_description(self.description())

    def state(self):
        return self.iconwidget.state

    def description(self):
        return self.textwidget.toPlainText()






