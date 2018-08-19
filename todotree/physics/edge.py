# File for the spring class

# Spring from one side?



from todotree.physics import Vector2, PhysicsNode

class Edge:
    def __init__(self, a: PhysicsNode, b: PhysicsNode):
        self.a = a
        self.b = b

    def magnitude(self) -> float:
        return self.direction().magnitude()

    def normalize(self) -> Vector2:
        return self.direction().normalize()

    def direction(self) -> Vector2:
        return self.b.position - self.a.position

# Currently only effects self. Damping force only pulls from B

class Spring(Edge):
    def __init__(self, a: PhysicsNode, b: PhysicsNode, length, stiffness = 1, damping = 1):
        super().__init__(a, b)
        self.length = length
        self.stiffness = stiffness
        self.damping = damping

    def get_restoring_force(self):
        displacement = self.magnitude() - self.length
        unit = self.normalize()

        # Hooke's Law: F = kD, where k = stiffness, and D = displacement
        unit *= (-self.stiffness * displacement)

        return unit

    def get_damping_force(self):
        return self.b.velocity * -self.damping