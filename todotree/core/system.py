from todotree.core import TodoItemCore

# Is this class necessary? Maybe for search functions or sumt'n?

class CoreSystem:
    def __init__(self):
        self.todoitems = []

    def createTodoItem(self):
        item = TodoItemCore()
        self.todoitems.append(item)

        return item