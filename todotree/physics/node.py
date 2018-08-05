# File containing the class for the physics node

# So, if these nodes contain the TodoItems then:
#   Node position -> TI position
#   In other words, update here is update there.
from physics.vector import Vector2

class Node:
    def __init__(self, mass = 1, position = None, velocity = None, acceleration = None):
        """Initialize a physics node.

        Keyword arguments:
        mass -- mass of this node (default 1)
        position -- (Vector2) position of this node (default Vector2())
        velocity -- (Vector2) position of this node (default Vector2())
        acceleration -- (Vector2) position of this node (default Vector2())
        """
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

        if self.position is None:
            self.position = Vector2()
        if self.velocity is None:
            self.velocity = Vector2()
        if self.acceleration is None:
            self.acceleration = Vector2()

    def apply_force(self, force):
        """Apply force to this node.

        Keyword arguments:
        force -- (Vector2) the force to be applied to this node
        """
        if isinstance(force, Vector2):
            self.acceleration += force / self.mass

    def set_x(self, x):
        self.position.set_x(x)

    def set_y(self, y):
        self.position.set_y(y)

    def setPosition(self, x, y):
        self.position.set_x(x)
        self.position.set_y(y)

    @property
    def x(self):
        return self.position.x

    @property
    def y(self):
        return self.position.y

