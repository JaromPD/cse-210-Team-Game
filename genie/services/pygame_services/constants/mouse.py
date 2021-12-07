import pygame
from genie.services.constants.mouse import *

"""
    This map maps the Genie consant id of each mouse button to its partner in the Pygame framework.
    Some of the constants defined above are not found in this map because Pygame does not support
    such mouse buttons.
"""
mouse_map = {
    LEFT : 0,      # index for Left mouse
    MIDDLE : 1,    # index for Middle mouse
    RIGHT : 2,     # index for Right mouse

    # If mouse has more than 3 buttons:
    # (there are only 2 more since Pygame only support 5)
    EXTRA1 : 3,
    EXTRA2 : 4
}