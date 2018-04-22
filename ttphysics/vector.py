# https://www.gamedev.net/forums/topic/486122-is-there-a-built-in-python-vector-class/
from math import sqrt

class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __truediv__(self, value):
        return Vector(self.x / value, self.y / value)

    def __mul__(self, value):
        return Vector(self.x * value, self.y * value)

    def __idiv__(self, value):
        self.x /= value
        self.y /= value
        return self

    def __imul__(self, value):
        self.x *= value
        self.y *= value
        return self

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.x != other.x or self.y != other.y:
            return True
        else:
            return False

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def magnitude(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        if self.x == 0 and self.y == 0:
            return Vector()

        return self / self.magnitude()
