# File containing the class for the physics node

# Currently only effects self.
from todotree.physics.vector import Vector2

class PhysicsNode:
    def __init__(self, mass = 1, position: Vector2 = None, velocity: Vector2 = None, acceleration: Vector2 = None):
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

        self.edges = []

    def apply_force(self, force):
        """Apply force to this node.

        Keyword arguments:
        force -- (Vector2) the force to be applied to this node
        """
        if isinstance(force, Vector2):
            self.acceleration += force / self.mass

    def update_properties(self, timestep_in_seconds):
        self.velocity += self.acceleration * timestep_in_seconds
        self.position += self.velocity * timestep_in_seconds

    def set_x(self, x):
        self.position.set_x(x)

    def set_y(self, y):
        self.position.set_y(y)

    def set_position(self, x, y):
        self.position.set_x(x)
        self.position.set_y(y)

    @property
    def x(self):
        return self.position.x

    @property
    def y(self):
        return self.position.y

    def add_edge(self, edge):
        self.edges.append(edge)

    def remove_edge(self, edge):
        self.edges.remove(edge)

