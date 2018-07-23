# The TodoTree class combines everything needed to get a functioning TodoTree
# on screen

from PyQt5.QtWidgets import QWidget


class TodoTree(QWidget):
    def __init__(self, parent = None, x = 0, y = 0,
                 width = 800, height = 600, root = None):
        """Initialize a TodoTree widget.

        Keyword arguments:
        parent -- (QWidget) the parent for this widget (default None)
        x -- (Int) x position (default 0)
        y -- (Int) y position (default 0)
        width -- (Int) widget width (default 800)
        height -- (Int) widget height (default 600)
        root -- (TodoNode/TodoNodeWidget) root of this todotree
        """
        super().__init__(self, parent = parent)
        self.setGeometry(x,y,width,height)
        self.root = root
