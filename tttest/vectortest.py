import unittest
from ttphysics import Vector

class TestVector(unittest.TestCase):

    def test_eq_ne(self):
        a = Vector(0, 0)
        b = Vector(0, 0)
        c = Vector(1, 0)
        d = Vector(0, 1)

        self.assertTrue(a == a)
        self.assertTrue(a == b)
        self.assertFalse(a != b)
        self.assertTrue(a != c)
        self.assertTrue(a != d)

        # This fails
        # self.assertTrue(a == c)

    def test_init(self):
        a = Vector(0,0)
        init = Vector()

        self.assertTrue(a == init)

        b = Vector(3,4)
        self.assertTrue(b.x == 3)
        self.assertTrue(b.y == 4)

    def test_add_iadd(self):
        a = Vector(1, 2)
        b = Vector(3, 4)

        c = a + b
        self.assertTrue(c.x == 4)
        self.assertTrue(c.y == 6)

        a += b
        self.assertTrue(a.x == 4)
        self.assertTrue(a.y == 6)

    def test_sub_isub(self):
        a = Vector(1,2)
        b = Vector(3,4)

        c = a - b
        self.assertTrue(c.x == -2)
        self.assertTrue(c.y == -2)

        a -= b
        self.assertTrue(a.x == -2)
        self.assertTrue(a.y == -2)

    def test_div_idiv(self):
        a = Vector(4,8)
        v = 2

        b = a / v
        self.assertTrue(b.x == 2)
        self.assertTrue(b.y == 4)

        a /= v
        self.assertTrue(a.x == 2)
        self.assertTrue(a.y == 4)

        c = Vector(2, 3)
        v2 = 4
        c /= v2
        self.assertTrue(c.x == 0.5)
        self.assertTrue(c.y == 0.75)

    def test_mul_imul(self):
        a = Vector(1,2)
        v = 2

        b = a * v
        self.assertTrue(b.x == 2)
        self.assertTrue(b.y == 4)

        a *= v
        self.assertTrue(a.x == 2)
        self.assertTrue(a.y == 4)

    def test_str(self):
        a = Vector()
        b = Vector(2,4)

        self.assertTrue(str(a) == "(0,0)")
        self.assertTrue(str(b) == "(2,4)")

    def test_magnitude(self):
        a = Vector(3,4)

        self.assertTrue(a.magnitude() == 5)
        self.assertFalse(a.magnitude() != 5)

    def test_normalize(self):
        pass

if __name__ == '__main__':
    unittest.main()