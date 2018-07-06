# This file contains the most basic todoitem properties: the item state and item description
from ttcore.tree import TreeNode

class TodoItem():
    def __init__(self, state = None, description = None):
        self.__state = state
        self.__description = description

    @property
    def state(self):
        return self.__state

    @property
    def description(self):
        return self.__description

    def setState(self, state):
        self.__state = state

    def setDescription(self, description):
        self.__description = description


class TodoNode(TodoItem, TreeNode):
    def __init__(self, state = None, description = None, parent = None, children = None):
        TodoItem.__init__(self, state, description)
        TreeNode.__init__(self, parent, children)