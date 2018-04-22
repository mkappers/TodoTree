# File containing the class for the physics node

# So, if these nodes contain the TodoItems then:
#   Node position -> TI position
#   In other words, update here is update there.
from ttphysics.vector import Vector

class Node:
    def __init__(self, mass = 1, position = None, velocity = None, acceleration = None):
        self.mass = mass

        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

        if self.position is None:
            self.position = Vector()
        if self.velocity is None:
            self.velocity = Vector()
        if self.acceleration is None:
            self.acceleration = Vector()

    def applyForce(self, force):
        if isinstance(force, Vector):
            self.acceleration += force / self.mass

    def setPosition(self, x, y):
        self.position.x = x
        self.position.y = y

    @property
    def x(self):
        return self.position.x

    @property
    def y(self):
        return self.position.y

