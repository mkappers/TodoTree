# https://www.gamedev.net/forums/topic/486122-is-there-a-built-in-python-vector-class/
# This file contains a generic vector implementation and an vector2 class with x and y properties

from math import sqrt

import operator

class Vector:
    def __init__(self, *args):
        self.itercount = 0
        self.dimensions = args

    def __add__(self, other):
        return type(self)(*tuple(map(operator.add, self.dimensions, other.dimensions)))

    def __sub__(self, other):
        return type(self)(*tuple(map(operator.sub, self.dimensions, other.dimensions)))

    def __iadd__(self, other):
        self.dimensions = (self + other).dimensions
        return self

    def __isub__(self, other):
        self.dimensions = (self - other).dimensions
        return self

    def __truediv__(self, value):
        return type(self)(*tuple(map(lambda x: x / value, self.dimensions)))

    def __mul__(self, value):
        return type(self)(*tuple(map(lambda x: x * value, self.dimensions)))

    def __idiv__(self, value):
        self.dimensions = (self / value).dimensions
        return self

    def __imul__(self, value):
        self.dimensions = (self * value).dimensions
        return self

    def __eq__(self, other):
        if len(self) != len(other):
            return False

        for i,a in enumerate(other):
            if a != self.dimensions[i]:
                return False

        return True

    def __ne__(self, other):
        if len(self) != len(other):
            return True

        for i,a in enumerate(other):
            if a != self.dimensions[i]:
                return True

        return False

    def __len__(self):
        return len(self.dimensions)

    def __str__(self):
        return str(self.dimensions)

    # Make vector iterable
    def __iter__(self):
        return self

    def __next__(self):
        self.itercount += 1

        try:
            return self.dimensions[self.itercount - 1]
        except IndexError:
            self.itercount = 0
            raise StopIteration

    def magnitude(self):
        return sqrt(sum(map(lambda x: x**2, self.dimensions)))

    def normalize(self):
        if len(self) == 0:
            return type(self)()

        if self.magnitude() == 0:
            return type(self)(*self.dimensions)

        return self / self.magnitude()


class Vector2(Vector):
    def __init__(self, x = 0, y = 0):
        dimensions = (x,y)
        super().__init__(*dimensions)

    @property
    def x(self):
        return self.dimensions[0]

    @property
    def y(self):
        return self.dimensions[1]

    def set_x(self, x):
        self.dimensions = (x, self.y)

    def set_y(self, y):
        self.dimensions = (self.x, y)

    def set_dimensions(self, x, y):
        self.dimensions = (x, y)
