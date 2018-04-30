import unittest
from ttcore.tree import TreeNode

class TestTree(unittest.TestCase):
    def test_init(self):
        tree = TreeNode()

        self.assertTrue(tree.parent == None)
        self.assertTrue(len(tree.children) == 0)
