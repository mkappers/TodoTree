from ttphysics.vector import Vector

class Edge:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def magnitude(self):
        return self.direction().magnitude()

    def normalize(self):
        return self.direction().normalize()

    def direction(self):
        return self.b.position - self.a.position
