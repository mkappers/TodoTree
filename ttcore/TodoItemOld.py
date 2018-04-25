# TodoItem

from ttcore.TodoItemCore import TodoItemCore
from ttphysics.node import Node
from ttwidgets.TodoItemWidget import TodoItemWidget

class TodoItem:
    def __init__(self, tiparent, tistate, tidescription, graphicsparent):
        self.core = TodoItemCore(parent = tiparent, state = tistate, description = tidescription)
        self.node = Node()
        self.widget = TodoItemWidget(graphicsparent, self.core)
        self.widget.setPosition(self.node.position[0], self.node.position[1])



