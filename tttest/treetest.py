import unittest
from ttcore.tree import TreeNode

class TestTree(unittest.TestCase):
    def test_init(self):
        tree = TreeNode()

        self.assertTrue(tree.parent == None)
        self.assertTrue(len(tree.children) == 0)
        self.assertTrue(tree.children == [])

    def test_add_children(self):
        tree = TreeNode()

        tree.appendChild(TreeNode())
        tree.appendChild(TreeNode())
        tree.appendChild(TreeNode())

        self.assertTrue(len(tree.children) == 3)

    def test_remove_child(self):
        tree = TreeNode()

        a = TreeNode()
        b = TreeNode()
        c = TreeNode()
        d = TreeNode()

        tree.appendChild(a)
        tree.appendChild(b)
        tree.appendChild(c)
        tree.appendChild(d)

        self.assertTrue(tree.children == [a,b,c,d])

        tree.removeChild(a)
        self.assertTrue(tree.children == [b,c,d])

        tree.removeChild(c)
        self.assertTrue(tree.children == [b,d])

        tree.removeChild(d)
        self.assertTrue(tree.children == [b])

    def test_insert_child(self):
        tree = TreeNode()

        a = TreeNode()
        b = TreeNode()
        c = TreeNode()
        d = TreeNode()
        e = TreeNode()

        tree.insertChild(0,a)
        self.assertTrue(tree.children == [a])

        tree.insertChild(0,c)
        self.assertTrue(tree.children == [c,a])

        tree.insertChild(1,b)
        self.assertTrue(tree.children == [c,b,a])

        # Weird inserts, but work due to python list implementation
        tree.insertChild(5,d)
        self.assertTrue(tree.children == [c,b,a,d])
        tree.insertChild(-1, e)
        self.assertTrue(tree.children == [c,b,a,e,d])

    def test_insert_child_before(self):
        tree = TreeNode()

        a = TreeNode()
        b = TreeNode()
        c = TreeNode()
        d = TreeNode()

        tree.appendChild(a)
        tree.insertChildBefore(b,a)
        self.assertTrue(tree.children == [b,a])

        tree.insertChildBefore(c,a)
        self.assertTrue(tree.children == [b,c,a])

        with self.assertRaises(ValueError):
            tree.insertChildBefore(d, TreeNode())

    def test_cut_tree(self):
        tree = TreeNode()

        a = TreeNode()
        b = TreeNode()
        c = TreeNode()
        d = TreeNode()

        tree.appendChild(a)
        tree.appendChild(b)
        b.appendChild(c)
        b.appendChild(d)

        self.assertTrue(tree.getLevelOrder() == [tree,a,b,c,d])

        b2 = b.cutTree()

        self.assertTrue(tree.getLevelOrder() == [tree,a])
        self.assertTrue(b2.parent == None)
        self.assertTrue(b2.getLevelOrder() == [b,c,d])

        self.assertTrue(tree.cutTree() == tree)

        # Also test tree insert
        tree.appendChild(b2)
        self.assertTrue(tree.getLevelOrder() == [tree,a,b,c,d])

    def test_cut_node(self):
        tree = TreeNode()

        a = TreeNode()
        b = TreeNode()
        c = TreeNode()
        d = TreeNode()

        tree.appendChild(a)
        tree.appendChild(b)
        b.appendChild(c)
        b.appendChild(d)

        self.assertTrue(tree.getLevelOrder() == [tree,a,b,c,d])

        b2 = b.cut()
        self.assertTrue(tree.children == [a,c,d])
        self.assertTrue(b2.parent == None)
        self.assertTrue(b2.children == [])

    def test_traversal_preorder(self):
        a = TreeNode()
        b = TreeNode()
        c = TreeNode()
        d = TreeNode()
        e = TreeNode()

        a.appendChild(b)
        a.appendChild(c)
        b.appendChild(d)
        b.appendChild(e)

        preorderlist_check = [a,b,d,e,c]
        preorderlist = a.getPreOrder()

        self.assertTrue(preorderlist_check == preorderlist)

    def test_traversal_levelorder(self):
        a = TreeNode()
        b = TreeNode()
        c = TreeNode()
        d = TreeNode()
        e = TreeNode()

        a.appendChild(b)
        a.appendChild(c)
        b.appendChild(d)
        b.appendChild(e)

        levelorderlist_check = [a,b,c,d,e]
        levelorderlist = a.getLevelOrder()

        self.assertTrue(levelorderlist_check == levelorderlist)


if __name__ == '__main__':
    unittest.main()