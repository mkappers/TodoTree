
import TTConstants as TTC
from TTConstants import GeometryAnchor as Anchor

from PyQt5.QtCore import QPointF, QRect
from PyQt5.QtGui import QPainterPath


def getAnchoredGeometryRect(x, y, width, height, anchor):
    return calculateAnchoredGeometryRect(QRect(x, y, width, height), anchor)


def calculateAnchoredGeometryRect(rect, anchor):
    x = rect.x()
    y = rect.y()
    w = rect.width()
    h = rect.height()

    if anchor is Anchor.CENTER:
        return QRect(x - w / 2, y - h / 2, w, h)
    elif anchor is Anchor.TOP_CENTER:
        return QRect(x - w / 2, y, w, h)
    elif anchor is Anchor.TOP_RIGHT:
        return QRect(x - w, y, w, h)
    elif anchor is Anchor.RIGHT_CENTER:
        return QRect(x - w, y - h / 2, w, h)
    elif anchor is Anchor.LEFT_CENTER:
        return QRect(x, y - h / 2, w, h)
    elif anchor is Anchor.BOTTOM_LEFT:
        return QRect(x, y - h, w, h)
    elif anchor is Anchor.BOTTOM_CENTER:
        return QRect(x - w / 2, y - h, w, h)
    elif anchor is Anchor.BOTTOM_RIGHT:
        return QRect(x - w, y - h, w, h)
    else:   # This is Anchor.TOP_LEFT, and also the default
        return rect


class HollowRoundedRectanglePath():
    '''Class for creating a hollow rounded rectangle path.'''
    width = None
    height = None
    rim = None
    radius = None

    def __init__(self, width, height, rimpercentage = TTC.ICON_RIM_SIZE, outerradius = TTC.ICON_RADIUS):
        """Create a hollow rounded rectangle.

        Keyword arguments:
        rimWidth -- The width of the rim (ratio)
        arcRadius -- The radius of the corner arc (ratio)
        """
        self.width = width
        self.height = height
        self.rimpercentage = rimpercentage
        self.outerradius = outerradius

    def generateRimPoints(self, rimpercentage):
        # Margin is percentage of half the icon size (1 is a filled rounded rectangle)
        rimratio = rimpercentage / 100
        margin = (self.width / 2) * rimratio
        rimradius = (self.width) * (self.outerradius / 100) * (1.0 - rimratio)

        topLeft =       {'leftSidePoint': QPointF(margin, rimradius + margin),
                         'topSidePoint': QPointF(rimradius + margin, margin),
                         'controlPoint': QPointF(margin, margin)}
        topRight =      {'rightSidePoint': QPointF(self.width - margin, rimradius + margin),
                         'topSidePoint': QPointF(self.width - rimradius - margin, margin),
                         'controlPoint': QPointF(self.width - margin, margin)}
        bottomRight =   {'rightSidePoint': QPointF(self.width - margin, self.height - rimradius - margin),
                         'bottomSidePoint': QPointF(self.width - rimradius - margin, self.height - margin),
                         'controlPoint': QPointF(self.width - margin, self.height - margin)}
        bottomLeft =    {'bottomSidePoint': QPointF(rimradius + margin, self.height - margin),
                         'leftSidePoint': QPointF(margin, self.height - rimradius - margin),
                         'controlPoint': QPointF(margin, self.height - margin)}
        topCenter =     QPointF(self.width / 2, margin)

        rimPoints = {'topLeft': topLeft, 'topRight': topRight, 'bottomLeft': bottomLeft, 'bottomRight': bottomRight,
                      'topCenter': topCenter}

        return rimPoints

    def generatePath(self, outerRimPoints, innerRimPoints):
        # MoveTo, LineTo, QuadTo
        orp = outerRimPoints
        irp = innerRimPoints

        # For debugging purposes:
        #print("Outer: " + str(orp))
        #print("Inner: " + str(irp))

        p = QPainterPath()
        # Set to starting position: top center
        p.moveTo(orp['topCenter'])

        # Generate outer rim path
        p.lineTo(orp['topRight']['topSidePoint'])
        p.quadTo(orp['topRight']['controlPoint'], orp['topRight']['rightSidePoint'])
        p.lineTo(orp['bottomRight']['rightSidePoint'])
        p.quadTo(orp['bottomRight']['controlPoint'], orp['bottomRight']['bottomSidePoint'])
        p.lineTo(orp['bottomLeft']['bottomSidePoint'])
        p.quadTo(orp['bottomLeft']['controlPoint'], orp['bottomLeft']['leftSidePoint'])
        p.lineTo(orp['topLeft']['leftSidePoint'])
        p.quadTo(orp['topLeft']['controlPoint'], orp['topLeft']['topSidePoint'])
        p.lineTo(orp['topCenter'])

        # Connect to inner rim path
        p.lineTo(irp['topCenter'])

        # Generate inner rim path
        p.lineTo(irp['topLeft']['topSidePoint'])
        p.quadTo(irp['topLeft']['controlPoint'], irp['topLeft']['leftSidePoint'])
        p.lineTo(irp['bottomLeft']['leftSidePoint'])
        p.quadTo(irp['bottomLeft']['controlPoint'], irp['bottomLeft']['bottomSidePoint'])
        p.lineTo(irp['bottomRight']['bottomSidePoint'])
        p.quadTo(irp['bottomRight']['controlPoint'], irp['bottomRight']['rightSidePoint'])
        p.lineTo(irp['topRight']['rightSidePoint'])
        p.quadTo(irp['topRight']['controlPoint'], irp['topRight']['topSidePoint'])
        p.lineTo(irp['topCenter'])

        # Path 'should' be closed automatically, if not here is one final lineTo:
        # p.lineTo(orp['topCenter'])

        return p

    def updateRim(self, rimpercentage):
        self.rimpercentage = rimpercentage

    def getPath(self):
        return self.generatePath(self.generateRimPoints(0), self.generateRimPoints(self.rimpercentage))