from todotree.graphics import AnchoredWidgetWrapper
from todotree.physics import PhysicsNode

class PhysicsNodeAnchoredWidgetWrapper(AnchoredWidgetWrapper, PhysicsNode):
    def __init__(self, parent, widget):
        # Init AWG and PhysicsNode
        # Override position functions
        # Signals?
        AnchoredWidgetWrapper.__init__(self, parent, widget)
        PhysicsNode.__init__(self)

    # Maybe also override set_x and set_y?
    def set_position(self, x, y):
        PhysicsNode.set_position(self, x, y)

        if AnchoredWidgetWrapper.get_position(self).x() != x or \
                AnchoredWidgetWrapper.get_position(self).y() != y:
            AnchoredWidgetWrapper.move(self, x, y)

    def move(self, x, y):
        AnchoredWidgetWrapper.move(self, x, y)

        if self.position.x != x or self.position.y != y:
            PhysicsNode.set_position(self, x, y)

    def update_wrapper_position(self):
        self.move(self.position.x, self.position.y)

    @property
    def x(self):
        return AnchoredWidgetWrapper.get_position(self).x()

    @property
    def y(self):
        return AnchoredWidgetWrapper.get_position(self).y()
