# File for the TTPhysics system

class System():
    def __init__(self):
        '''Initialize empty physics system.'''
        self.nodes = []
        self.springs = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_node_collection(self, nodecollection):
        for node in nodecollection:
            self.nodes.append(node)

    def add_spring(self, spring):
        self.springs.append(spring)

    def add_spring_collection(self, springcollection):
        for spring in springcollection:
            self.springs.append(spring)

    def update(self, timestepinmilliseconds):
        tsinseconds = timestepinmilliseconds / 1000

        self.apply_hookes_law(tsinseconds)
        self.update_velocity(tsinseconds)
        self.update_position(tsinseconds)

    def apply_hookes_law(self, timestep, damping = True):
        for spring in self.springs:
            d = spring.edge.direction()
            displacement = d.magnitude() - spring.length
            unit = d.normalize()

            spring.b.acceleration = (unit * (-spring.stiffness * displacement))
            if damping:
                spring.b.acceleration += spring.b.velocity * -spring.damping

    def apply_repulsion(self, timestep):
        for node in self.nodes:
            # Repulsion: smaller distance = larger repulsion between nodes
            pass

    def update_velocity(self, timestep):
        for node in self.nodes:
            node.velocity += (node.acceleration * timestep)

    def update_position(self, timestep):
        for node in self.nodes:
            node.position += (node.velocity * timestep)