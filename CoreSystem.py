from ttcore.TodoItemCore import TodoItemCore

class CoreSystem:
    def __init__(self):
        self.todoitems = []

    def createTodoItem(self):
        item = TodoItemCore()
        self.todoitems.append(item)

        return item