# File for the spring class

# Spring from one side?

class Spring():
    def __init__(self, length = None, stiffness = None, damping = None, edge = None):
        self.length = length
        self.stiffness = stiffness
        self.damping = damping
        self.edge = edge

    def getrestoringforce(self):
        displacement = self.edge.magnitude() - self.length
        unit = self.edge.normalize()

        # Hooke's Law: F = kD, where k = stiffness, and D = displacement
        unit *= (-self.stiffness * displacement)

        return unit

    def getdampingforce(self):
        return self.edge.b.velocity * -self.damping

    @property
    def a(self):
        return self.edge.a

    @property
    def b(self):
        return self.edge.b