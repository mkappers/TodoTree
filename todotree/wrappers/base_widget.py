# This file contains the base widget wrapper for PyQt5
import sys

from PyQt5.QtWidgets import QWidget

class Widget:
    def __init__(self, parent = None):
        self.qwidget = QWidget(parent)

    def set_size(self, width, height):
        # Should also set geometry, how to solve this...
        self.width = width
        self.height = height

    def set_position(self, x, y):
        # Should also set geometry, how to solve this...
        self.x = x
        self.y = y

    # Maybe make 'update_geometry' function instead? Same problem though, unless you have to explicitly call it.
    def set_geometry(self, x = None, y = None, width = None, height = None):
        if x != None: self.x = x
        if y != None: self.y = y
        if width != None: self.width = width
        if height != None: self.height = height

        try:
            self.qwidget.setGeometry(self.x, self.y, self.width, self.height)
        except:
            print("Error while setting geometry for QWidget:", sys.exc_info()[0])
            raise

    def show(self):
        self.qwidget.show()
