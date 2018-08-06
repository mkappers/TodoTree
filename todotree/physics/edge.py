# File for the spring class

# Spring from one side?

from todotree.physics import Vector2

class Edge:
    def __init__(self, a: Vector2, b: Vector2):
        self.a = a
        self.b = b

    def magnitude(self) -> float:
        return self.direction().magnitude()

    def normalize(self) -> Vector2:
        return self.direction().normalize()

    def direction(self) -> Vector2:
        return self.b.position - self.a.position


class Spring(Edge):
    def __init__(self, a: Vector2, b: Vector2, length, stiffness = 1, damping = 1):
        super().__init__(self, a, b)
        self.length = length
        self.stiffness = stiffness
        self.damping = damping

    def get_restoring_force(self):
        displacement = self.edge.magnitude() - self.length
        unit = self.edge.normalize()

        # Hooke's Law: F = kD, where k = stiffness, and D = displacement
        unit *= (-self.stiffness * displacement)

        return unit

    def get_damping_force(self):
        return self.edge.b.velocity * -self.damping