# File for the TTPhysics system

class System():
    def __init__(self):
        '''Initialize empty physics system.'''
        self.nodes = []
        self.springs = []

    def addNode(self, node):
        self.nodes.append(node)

    def addNodeCollection(self, nodecollection):
        for node in nodecollection:
            self.nodes.append(node)

    def addSpring(self, spring):
        self.springs.append(spring)

    def addSpringCollection(self, springcollection):
        for spring in springcollection:
            self.springs.append(spring)

    def update(self, timestepinmilliseconds):
        tsinseconds = timestepinmilliseconds / 1000

        self.applyHookesLaw(tsinseconds)
        self.updateVelocity(tsinseconds)
        self.updatePosition(tsinseconds)

    def applyHookesLaw(self, timestep, damping = True):
        for spring in self.springs:
            d = spring.edge.direction()
            displacement = d.magnitude() - spring.length
            unit = d.normalize()

            spring.b.acceleration = (unit * (-spring.stiffness * displacement))
            if damping:
                spring.b.acceleration += spring.b.velocity * -spring.damping

    def applyRepulsion(self, timestep):
        for node in self.nodes:
            # Repulsion: smaller distance = larger repulsion between nodes
            pass

    def updateVelocity(self, timestep):
        for node in self.nodes:
            node.velocity += (node.acceleration * timestep)

    def updatePosition(self, timestep):
        for node in self.nodes:
            node.position += (node.velocity * timestep)