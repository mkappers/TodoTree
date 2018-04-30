# This file contains the most basic todoitem properties: the item state and item description

class TodoItem():
    def __init__(self, state = None, description = None):
        self.state = state
        self.description = description

class TodoItemNode(TodoItem):
    def __init__(self, state = None, description = None, parent = None, children = None):
        super().__init__(state, description)

        self.parent = parent
        self.children = children