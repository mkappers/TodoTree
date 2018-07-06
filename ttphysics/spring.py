# File for the spring class

# Spring from one side?
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


class Spring(Edge):
    def __init__(self, a, b, length, stiffness = 1, damping = 1):
        super().__init__(self, a, b)
        self.length = length
        self.stiffness = stiffness
        self.damping = damping

    def getrestoringforce(self):
        displacement = self.edge.magnitude() - self.length
        unit = self.edge.normalize()

        # Hooke's Law: F = kD, where k = stiffness, and D = displacement
        unit *= (-self.stiffness * displacement)

        return unit

    def getdampingforce(self):
        return self.edge.b.velocity * -self.damping