from ttphysics import Node, Edge, Spring

class PhysicsSystem:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.springs = []

    def createNode(self):
        node = Node()
        self.nodes.append(node)
        return node

    def createEdge(self, a, b):
        edge = Edge(a, b)
        self.edges.append(edge)
        return edge

    def createSpring(self, edge):
        spring = Spring(edge = edge)
        self.springs.append(spring)
        return spring

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