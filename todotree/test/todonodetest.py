import unittest
from core.todoitem import TodoNode

class TestTodoNode(unittest.TestCase):
    def test_init(self):
        todonode = TodoNode()

        self.assertTrue(todonode.parent == None)
        self.assertTrue(len(todonode.children) == 0)
        self.assertTrue(todonode.children == [])

    def test_add_children(self):
        todonode = TodoNode()

        todonode.appendChild(TodoNode())
        todonode.appendChild(TodoNode())
        todonode.appendChild(TodoNode())

        self.assertTrue(len(todonode.children) == 3)

    def test_remove_child(self):
        todonode = TodoNode()

        a = TodoNode()
        b = TodoNode()
        c = TodoNode()
        d = TodoNode()

        todonode.appendChild(a)
        todonode.appendChild(b)
        todonode.appendChild(c)
        todonode.appendChild(d)

        self.assertTrue(todonode.children == [a,b,c,d])

        todonode.removeChild(a)
        self.assertTrue(todonode.children == [b,c,d])

        todonode.removeChild(c)
        self.assertTrue(todonode.children == [b,d])

        todonode.removeChild(d)
        self.assertTrue(todonode.children == [b])

    def test_insert_child(self):
        todonode = TodoNode()

        a = TodoNode()
        b = TodoNode()
        c = TodoNode()
        d = TodoNode()
        e = TodoNode()

        todonode.insertChild(0,a)
        self.assertTrue(todonode.children == [a])

        todonode.insertChild(0,c)
        self.assertTrue(todonode.children == [c,a])

        todonode.insertChild(1,b)
        self.assertTrue(todonode.children == [c,b,a])

        # Weird inserts, but work due to python list implementation
        todonode.insertChild(5,d)
        self.assertTrue(todonode.children == [c,b,a,d])
        todonode.insertChild(-1, e)
        self.assertTrue(todonode.children == [c,b,a,e,d])

    def test_insert_child_before(self):
        todonode = TodoNode()

        a = TodoNode()
        b = TodoNode()
        c = TodoNode()
        d = TodoNode()

        todonode.appendChild(a)
        todonode.insertChildBefore(b,a)
        self.assertTrue(todonode.children == [b,a])

        todonode.insertChildBefore(c,a)
        self.assertTrue(todonode.children == [b,c,a])

        with self.assertRaises(ValueError):
            todonode.insertChildBefore(d, TodoNode())

    def test_cut_todonode(self):
        todonode = TodoNode()

        a = TodoNode()
        b = TodoNode()
        c = TodoNode()
        d = TodoNode()

        todonode.appendChild(a)
        todonode.appendChild(b)
        b.appendChild(c)
        b.appendChild(d)

        self.assertTrue(todonode.getLevelOrder() == [todonode,a,b,c,d])

        b2 = b.cutTree()

        self.assertTrue(todonode.getLevelOrder() == [todonode,a])
        self.assertTrue(b2.parent == None)
        self.assertTrue(b2.getLevelOrder() == [b,c,d])

        self.assertTrue(todonode.cutTree() == todonode)

        # Also test todonode insert
        todonode.appendChild(b2)
        self.assertTrue(todonode.getLevelOrder() == [todonode,a,b,c,d])

    def test_cut_node(self):
        todonode = TodoNode()

        a = TodoNode()
        b = TodoNode()
        c = TodoNode()
        d = TodoNode()

        todonode.appendChild(a)
        todonode.appendChild(b)
        b.appendChild(c)
        b.appendChild(d)

        self.assertTrue(todonode.getLevelOrder() == [todonode,a,b,c,d])

        b2 = b.cut()
        self.assertTrue(todonode.children == [a,c,d])
        self.assertTrue(b2.parent == None)
        self.assertTrue(b2.children == [])

    def test_traversal_preorder(self):
        a = TodoNode()
        b = TodoNode()
        c = TodoNode()
        d = TodoNode()
        e = TodoNode()

        a.appendChild(b)
        a.appendChild(c)
        b.appendChild(d)
        b.appendChild(e)

        preorderlist_check = [a,b,d,e,c]
        preorderlist = a.getPreOrder()

        self.assertTrue(preorderlist_check == preorderlist)

    def test_traversal_levelorder(self):
        a = TodoNode()
        b = TodoNode()
        c = TodoNode()
        d = TodoNode()
        e = TodoNode()

        a.appendChild(b)
        a.appendChild(c)
        b.appendChild(d)
        b.appendChild(e)

        levelorderlist_check = [a,b,c,d,e]
        levelorderlist = a.getLevelOrder()

        self.assertTrue(levelorderlist_check == levelorderlist)


if __name__ == '__main__':
    unittest.main()