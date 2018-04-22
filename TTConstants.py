# Class containing all the Enums and constants

from enum import Enum

# Constants
ICON_SIZE = 20

# In percentages
ICON_RIM_SIZE = 40
ICON_RADIUS = 25

ANIMATION_STEPS = 10

# Enums
class GeometryAnchor(Enum):
    CENTER = 1
    TOP_LEFT = 2
    TOP_CENTER = 3
    TOP_RIGHT = 4
    RIGHT_CENTER = 5
    LEFT_CENTER = 6
    BOTTOM_LEFT = 7
    BOTTOM_CENTER = 8
    BOTTOM_RIGHT = 9


# TodoItem Enums
class TodoItemState(Enum):
    TODO = 1
    DONE = 2
    PARENTDONE = 3

