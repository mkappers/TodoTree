# https://en.wikipedia.org/wiki/Tree_(data_structure)
# https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/

class TreeNode():
    def __init__(self, parent = None, children = []):
        self.parent = parent
        self.children = children


    # TODO Magic methods (eq etc), add children, size, add branch, pruning, and more.

    # Traversals:

    # Depth first
    def getPreOrder(self):
        preOrderList = [self]

        if len(self.children) == 0:
            return preOrderList
        else:
            for child in self.children:
                preOrderList.extend(child.getPreOrder())

        return preOrderList

    def getPreOrderDescendants(self):
        _, *tail = self.getPreOrder()
        return tail

    # Level Order - Top to bottom
    def getLevelOrder(self):
        pass