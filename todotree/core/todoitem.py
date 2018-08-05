from enum import Enum

from core.tree import TreeNode

class TodoItemState(Enum):
    TODO = 1
    DONE = 2
    PARENTDONE = 3


class TodoItem():
    def __init__(self, state = TodoItemState.DONE, description = None):
        """Initialize a TodoItem.

        Keyword arguments:
        state -- (TodoItemState) the state of this item (default DONE)
        description -- (String) the description of this item (default None)
        """
        self.__state = state
        self.__description = description

    @property
    def state(self):
        return self.__state

    @property
    def description(self):
        return self.__description

    def set_state(self, state):
        self.__state = state

    def set_description(self, description):
        self.__description = description


class TodoNode(TodoItem, TreeNode):
    def __init__(self, state = None, description = None, parent = None, children = None):
        TodoItem.__init__(self, state, description)
        TreeNode.__init__(self, parent, children)