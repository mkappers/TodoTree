# https://en.wikipedia.org/wiki/Tree_(data_structure)
# https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/


class TreeNode():
    def __init__(self, parent = None, children = None):
        """Initialize a tree node.

        If no children are passed, children will be initialized as an empty list.

        Keyword arguments:
        parent -- the parent of this node (default None)
        children -- the children of this node (default None)
        """
        self.parent = parent
        self.children = children

        if self.children is None:
            self.children = []

    # TODO Magic methods (eq etc), add children, size, add branch, pruning, and more.
    def appendChild(self, child):
        """Append a child to this node's children list.

        Keyword arguments:
        child -- the child to append
        """
        child.parent = self
        self.children.append(child)

    def insertChild(self, index, child):
        """Insert a child at this specific index of the children collection.

        Keyword arguments:
        index -- the index where the child is inserted
        child -- the child to insert
        """
        child.parent = self
        self.children.insert(index, child)

    def insertChildBefore(self, a, b):
        """Insert (child) a before (child) b in this node.

        If b does not exist, a ValueError is raised.

        Keyword arguments:
        a -- the child to be inserted
        b -- the child after which a will be inserted
        """
        try:
            index = self.children.index(b)
        except ValueError:
            raise

        self.insertChild(index, a)

    def removeChild(self, child):
        """Remove child from this node.

        Returns child.

        Keyword arguments:
        child -- the child to be removed
        """
        child.parent = None
        self.children.remove(child)
        return child

    def cutTree(self):
        """Cut this tree.

        Returns this node.
        """
        if self.parent is not None:
            self.parent.removeChild(self)
        return self

    def cut(self):
        """Cut only this node.

        Childrens' parent is set to this node's parent.
        """
        if self.parent is not None:
            for child in self.children:
                self.parent.insertChildBefore(child, self)
        else:
            for child in self.children:
                child.parent = None

        self.children = []
        return self.parent.removeChild(self)


    # Traversals:
    # Depth first
    # def getDescendantsPreOrder(self):
    #     _, *tail = self.getPreOrder()
    #     return tail

    def getPreOrder(self):
        preOrderList = [self]

        if len(self.children) == 0:
            return preOrderList
        else:
            for child in self.children:
                preOrderList.extend(child.getPreOrder())

        return preOrderList

    # Level Order - Top to bottom
    def getLevelOrder(self):
        levelOrderList = [self]
        levelChildren = self.children

        while not len(levelChildren) == 0:
            levelOrderList.extend(levelChildren)
            levelChildrenTemp = []

            for child in levelChildren:
                levelChildrenTemp.extend(child.children)

            levelChildren = levelChildrenTemp

        return levelOrderList