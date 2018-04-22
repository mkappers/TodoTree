# File for TodoItem

import TTConstants as TTC

class TodoItemCore():
    def __init__(self, parent = None, children = [], state = TTC.TodoItemState.TODO, description = None):
        # Core
        self.__state = state
        self.__description = description

        # Relations with other TodoItems
        self.__parent = parent
        self.__children = children

    @property
    def state(self):
        return self.__state

    @property
    def description(self):
        return self.__description

    @property
    def parent(self):
        return self.__parent

    @property
    def children(self):
        return self.__children