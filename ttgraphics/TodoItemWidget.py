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

class TodoItemWidget(QWidget):
    todoitem = None
    iconwidget = None
    textwidget = None

    def __init__(self, parent, todoitem):
        super().__init__(parent)

        self.todoitem = todoitem

        self.iconwidget = TodoIconWidget(self, todoitem.state)
        self.textwidget = TodoTextWidget(self, todoitem.description)
        self.textwidget.update()

    def setPosition(self, x, y, anchor = TTC.GeometryAnchor.TOP_CENTER):
        width = max(TTC.ICON_SIZE, self.textwidget.width())
        height = TTC.ICON_SIZE + self.textwidget.height() + 5

        self.iconwidget.setGeometry(TTC.GeometryAnchor.TOP_CENTER, width / 2, 0, TTC.ICON_SIZE, TTC.ICON_SIZE)
        self.textwidget.setGeometry(TTC.GeometryAnchor.BOTTOM_CENTER, width / 2, height, self.textwidget.width(), self.textwidget.height())

        super().setGeometry(getAnchoredGeometryRect(x,y,width,height,anchor))

    # def __update_size(self):
    #     ir = self.icon.geometry()
    #     tr = self.text.geometry()
    #
    #     self.width = max(ir.width(), tr.width())
    #     self.height = max(ir.height(), tr.height())

    def state(self):
        return self.iconwidget.state

    def description(self):
        return self.textwidget.toPlainText()






