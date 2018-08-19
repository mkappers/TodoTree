import sys
sys.path.append(r"C:\Users\Maurits\Python\Projects\TodoTree")

from PyQt5.QtWidgets import QApplication

from todotree.core import TodoItemState
from todotree.graphics import TodoTextWidget, TodoIconWidget, TodoItemWidget, CanvasSystem, \
    AnchoredWidgetWrapper, HorizontalAnchor, VerticalAnchor
from todotree.physics import Vector2, Edge

class TestGraphics:
    def __init__(self):
        self.canvas = CanvasSystem(width = 600, height = 200)
        self.init_widgets()
        # self.init_points()
        self.init_lines()

    def init_widgets(self):

        done = AnchoredWidgetWrapper(self.canvas, TodoItemWidget(self.canvas, TodoItemState.DONE, "done", None, None))
        done.set_render_anchor(HorizontalAnchor.CENTER, VerticalAnchor.TOP)
        done.move(100, 100)
        done.show()

        todo = TodoItemWidget(self.canvas, TodoItemState.TODO, "todo", None, None)
        todo.move(300, 100)
        todo.show()

        pdoneicon = AnchoredWidgetWrapper.with_anchor(self.canvas, TodoIconWidget(None, TodoItemState.PARENTDONE), HorizontalAnchor.CENTER, VerticalAnchor.TOP)
        pdoneicon.move(500, 100)
        pdoneicon.show()
        pdonetext = AnchoredWidgetWrapper.with_anchor(self.canvas, TodoTextWidget(None, "parent done"), HorizontalAnchor.CENTER, VerticalAnchor.TOP)
        pdonetext.move(500, 144)
        pdonetext.show()

    def init_points(self):
        self.canvas.addPointReference(Vector2(100,100))

    def init_lines(self):
        self.canvas.addLineReference(Edge(Vector2(0, 100), Vector2(600, 100)))
        self.canvas.addLineReference(Edge(Vector2(100, 0), Vector2(100, 200)))
        self.canvas.addLineReference(Edge(Vector2(300, 0), Vector2(300, 200)))
        self.canvas.addLineReference(Edge(Vector2(500, 0), Vector2(500, 200)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    testplatform = TestGraphics()
    sys.exit(app.exec_())
