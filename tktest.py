# http://effbot.org/tkinterbook/
# http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html

import tkinter as tk

from enum import Enum

class TestWindow(tk.Frame):

    items = []

    def __init__(self):
        super().__init__()

        self.canvas = tk.Canvas(self, background="#FFF9C4")
        self.initUI()

    def initUI(self):
        self.master.title("Polygon Animation Test")
        self.pack(fill=tk.BOTH, expand=1)

        self.canvas.pack(fill=tk.BOTH, expand=1)

        # MorphPolygon(self.canvas)

        self.items.append(TodoItem(self.canvas))
        self.items.append(TodoItem(self.canvas, posX=100, size=40))
        self.items.append(TodoItem(self.canvas, posX=200, posY=200, size=40))
        self.items.append(TodoItem(self.canvas, posX=300, posY=300, size=160))

    def round_rectangle(self, x1, y1, x2, y2, radius=5, **kwargs):

        points = [x1 + radius, y1,
                  x1 + radius, y1,
                  x2 - radius, y1,
                  x2 - radius, y1,
                  x2, y1,
                  x2, y1 + radius,
                  x2, y1 + radius,
                  x2, y2 - radius,
                  x2, y2 - radius,
                  x2, y2,
                  x2 - radius, y2,
                  x2 - radius, y2,
                  x1 + radius, y2,
                  x1 + radius, y2,
                  x1, y2,
                  x1, y2 - radius,
                  x1, y2 - radius,
                  x1, y1 + radius,
                  x1, y1 + radius,
                  x1, y1]

        self.canvas.create_polygon(points, kwargs, smooth=True)


class TodoItemState(Enum):
    TODO = 1
    DONE = 2
    PARENTDONE = 3


class TodoItem:
    itemState = None

    x1 = 0.0
    y1 = 0.0
    x2 = None
    y2 = None
    size = None
    posX = None
    posY = None

    standardRim = None
    currentRim = None

    radius = None
    canvas = None

    _todoPolygon = None
    _clickPolygon = None

    def __init__(self, canvas, posX = 0.0, posY = 0.0, size = 80.0, arcradius = 0.25, rimwidth = 0.30):
        self.itemState = TodoItemState.TODO

        self.posX = posX
        self.posY = posY
        self.x2 = size
        self.y2 = size
        self.size = size
        self.radius = arcradius
        self.canvas = canvas
        
        self.standardRim = rimwidth
        self.currentRim = rimwidth

        #self.initRims()
        self._todoPolygon = self.generateItemPolygon()
        self._clickPolygon = self.generateClickPolygon()
        self.update()

    '''    
    def initRims(self):
        outerRadius = self.radius * self.size
        self._itemOuterRim = [
            self.x2 / 2, self.y1,           # Middle center top
            self.x2 / 2, self.y1,
            self.x2 - outerRadius, self.y1, # Double points to straighten line
            self.x2 - outerRadius, self.y1,
            self.x2, self.y1,               # Top right corner point for smooth arc
            self.x2, self.y1 + outerRadius,
            self.x2, self.y1 + outerRadius,
            self.x2, self.y2 - outerRadius,
            self.x2, self.y2 - outerRadius,
            self.x2, self.y2,               # Bottom right
            self.x2 - outerRadius, self.y2,
            self.x2 - outerRadius, self.y2,
            self.x1 + outerRadius, self.y2,
            self.x1 + outerRadius, self.y2,
            self.x1, self.y2,               # Bottom left
            self.x1, self.y2 - outerRadius,
            self.x1, self.y2 - outerRadius,
            self.x1, self.y1 + outerRadius,
            self.x1, self.y1 + outerRadius,
            self.x1, self.y1,               # Top left
            self.x1 + outerRadius, self.y1,
            self.x1 + outerRadius, self.y1,
            self.x2 / 2, self.y1,           # Middle center top
            self.x2 / 2, self.y1
        ]

        # Inner rim arc formula: corner +- radius * 1 - rim / (w|h / 2)
        innerRadius = self.size * self.radius * (1 - self.currentRim)

        innerX1 = self.x1 + self.currentRim * (self.size / 2)
        innerY1 = self.y1 + self.currentRim * (self.size / 2)
        innerX2 = self.x2 - self.currentRim * (self.size / 2)
        innerY2 = self.y2 - self.currentRim * (self.size / 2)

        self._todoInnerRim = [
            self.x2 / 2, innerY1,           # Middle center top
            self.x2 / 2, innerY1,
            innerX1 + innerRadius, innerY1,
            innerX1 + innerRadius, innerY1,
            innerX1, innerY1,               # Top left
            innerX1, innerY1 + innerRadius,
            innerX1, innerY1 + innerRadius,
            innerX1, innerY2 - innerRadius,
            innerX1, innerY2 - innerRadius,
            innerX1, innerY2,               # Bottom left
            innerX1 + innerRadius, innerY2,
            innerX1 + innerRadius, innerY2,
            innerX2 - innerRadius, innerY2,
            innerX2 - innerRadius, innerY2,
            innerX2, innerY2,               # Bottom right
            innerX2, innerY2 - innerRadius,
            innerX2, innerY2 - innerRadius,
            innerX2, innerY1 + innerRadius,
            innerX2, innerY1 + innerRadius,
            innerX2, innerY1,               # Top right
            innerX2 - innerRadius, innerY1,
            innerX2 - innerRadius, innerY1,
            self.x2 / 2, innerY1,            # Middle center top
            self.x2 / 2, innerY1
        ]
    '''

    def generateRimPoints(self, margin, radius):
        # Center is simply the x center of the polygon
        center = self.x2 / 2 + self.posX

        # Margin is ratio, between 0 and 1, so is radius
        # print("Generating rim: Margin:" + str(margin) + ", Radius: " + str(radius))
        # Top left and bottom right coords, respectively
        tlx = self.x1 + margin * (self.size / 2) + self.posX
        tly = self.y1 + margin * (self.size / 2) + self.posY
        brx = self.x2 - margin * (self.size / 2) + self.posX
        bry = self.y2 - margin * (self.size / 2) + self.posY

        rimradius = self.size * radius * (1 - margin)

        rimPoints = [
            center, tly,  # Middle center top
            center, tly,

            brx - rimradius, tly,
            brx - rimradius, tly,

            brx, tly,  # Top right

            brx, tly + rimradius,
            brx, tly + rimradius,
            brx, bry - rimradius,
            brx, bry - rimradius,

            brx, bry,  # Bottom right

            brx - rimradius, bry,
            brx - rimradius, bry,
            tlx + rimradius, bry,
            tlx + rimradius, bry,

            tlx, bry,  # Bottom left

            tlx, bry - rimradius,
            tlx, bry - rimradius,
            tlx, tly + rimradius,
            tlx, tly + rimradius,

            tlx, tly,  # Top left

            tlx + rimradius, tly,
            tlx + rimradius, tly,

            center, tly,  # Middle center top
            center, tly
        ]

        return rimPoints

    # http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
    def onItemClick(self, event):
        print("Click!")
        if self.itemState == TodoItemState.TODO:
            self.itemState = TodoItemState.DONE
        else:
            self.itemState = TodoItemState.TODO

    def generateItemPolygon(self):
        outerRim = self.generateRimPoints(0, self.radius)
        innerRimPoints = self.generateRimPoints(self.currentRim, self.radius)

        innerRim = []
        innerX = innerRimPoints[-2::-2]
        innerY = innerRimPoints[-1::-2]
        for i in zip(innerX, innerY):
            innerRim.append(i[0])
            innerRim.append(i[1])

        polygonPoints = outerRim + innerRim
        return self.canvas.create_polygon(polygonPoints, fill="#F44336", smooth=True)

    def generateClickPolygon(self):
        return self.canvas.create_polygon(self.generateRimPoints(0.0, self.radius), smooth=True)

    def draw(self):
        self.canvas.delete(self._todoPolygon)
        self.canvas.delete(self._clickPolygon)
        self._todoPolygon = self.generateItemPolygon()
        self._clickPolygon = self.generateClickPolygon()

    def update(self):
        self.draw()
        self.canvas.tag_bind(self._clickPolygon, '<Button-1>', self.onItemClick)

        if self.itemState == TodoItemState.DONE and self.currentRim < 1:
            self.currentRim += 0.025
        elif self.itemState == TodoItemState.TODO and self.currentRim > self.standardRim:
            self.currentRim -= 0.025

        self.canvas.after(10, self.update)


def main():
    root = tk.Tk()
    tw = TestWindow()
    root.geometry("800x600+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()
