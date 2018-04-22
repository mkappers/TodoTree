import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication

from CoreSystem import CoreSystem
from PhysicsSystem import PhysicsSystem
from CanvasSystem import CanvasSystem

class TestingPlatform:
    def __init__(self):
        self.core = CoreSystem()
        self.physics = PhysicsSystem()
        self.canvas = CanvasSystem()

        self.initCore()
        self.initPhysics()
        self.initCanvas()

        self.updatetimer = QTimer()
        self.updatetimer.setSingleShot(False)
        self.updatetimer.timeout.connect(self.update)
        self.updatetimer.start(20)

    def initCore(self):
        # TODO Make core init dynamic, also, be able to load trees

        # Create 2 todo items
        self.coreitem1 = self.core.createTodoItem()
        self.coreitem2 = self.core.createTodoItem()

    def initPhysics(self):
        # TODO Make physics init dynamic.

        # Create 2 physics nodes, 1 edge, and a spring
        self.node1 = self.physics.createNode()
        self.node1.setPosition(100,100)

        self.node2 = self.physics.createNode()
        self.node2.setPosition(100,250)

        self.edge12 = self.physics.createEdge(self.node1, self.node2)
        self.spring12 = self.physics.createSpring(self.edge12)
        self.spring12.length = 100
        self.spring12.stiffness = 3
        self.spring12.damping = 3

    def initCanvas(self):
        # TODO Fix canvas init
        print(self.node1.position)
        self.canvas.addPointReference(self.node1.position)
        self.canvas.addPointReference(self.node2.position)
        self.canvas.addLineReference(self.edge12)

    def update(self):
        self.physics.update(20)
        #print("Accel: ", self.node2.acceleration)
        #print("Damping: ", self.spring12.getdampingforce())
        print("Node 2 position: ", self.node2.y)
        print("Node 2 velocity: ", self.node2.velocity)
        if self.spring12.edge.magnitude() < self.spring12.length:
            print("Restoring force should be positive: ", self.spring12.getrestoringforce())
        else:
            print("Restoring force should be negative: ", self.spring12.getrestoringforce())
        print("Spr. Length: ", self.spring12.edge.magnitude())
        self.canvas.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    testplatform = TestingPlatform()
    sys.exit(app.exec_())
