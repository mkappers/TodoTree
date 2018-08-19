import sys

from todotree.graphics import CanvasSystem, TodoIconWidget, HorizontalAnchor, VerticalAnchor
from todotree.physics import System, Spring
from todotree.wrappers import PhysicsNodeAnchoredWidgetWrapper as PhysicsWrapper
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication



class TestGraphics:
    def __init__(self):
        self.canvas = CanvasSystem(width = 600, height = 600)
        self.physics = System()
        self.init_items()
        self.init_physics()

        self.changenum = 1

        self.updatetimer = QTimer()
        self.updatetimer.setSingleShot(False)
        #self.updatetimer.timeout.connect(self.init_change)
        self.updatetimer.timeout.connect(self.update_physics)
        self.updatetimer.start(20)


    def init_items(self):
        self.physicstest = PhysicsWrapper(self.canvas, TodoIconWidget(None))
        self.physicstest.set_render_anchor(HorizontalAnchor.CENTER, VerticalAnchor.CENTER)
        self.physicstest.move(100, 100)
        self.physicstest.show()

    def init_change(self):
        self.physicstest.move(self.physicstest.x + 2, self.physicstest.y)

    def init_physics(self):
        a = PhysicsWrapper(self.canvas, TodoIconWidget(None))
        a.set_render_anchor(HorizontalAnchor.CENTER, VerticalAnchor.CENTER)
        a.move(100, 300)
        a.show()

        b = PhysicsWrapper(self.canvas, TodoIconWidget(None))
        b.set_render_anchor(HorizontalAnchor.CENTER, VerticalAnchor.CENTER)
        b.move(500, 300)
        b.show()

        c = PhysicsWrapper(self.canvas, TodoIconWidget(None))
        c.set_render_anchor(HorizontalAnchor.CENTER, VerticalAnchor.CENTER)
        c.move(300, 400)
        c.show()

        spring = Spring(a, b, 100)
        spring2 = Spring(b, c, 100)
        spring3 = Spring(c, a, 100)

        self.physics.add_node(a)
        self.physics.add_node(b)
        self.physics.add_node(c)
        self.physics.add_spring(spring)
        self.physics.add_spring(spring2)
        self.physics.add_spring(spring3)

    def update_physics(self):
        self.physics.update(20)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    testplatform = TestGraphics()
    testplatform.init_change()
    sys.exit(app.exec_())
