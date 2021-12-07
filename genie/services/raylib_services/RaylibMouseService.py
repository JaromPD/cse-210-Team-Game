from pyray import *
from .constants.mouse import mouse_map

class RaylibMouseService:
    def __init__(self):
        """
            This class deals with all the mouse click/scroll events
        """
        pass
    
    def is_button_down(self, button):
        """
            Check to see if a specific mouse button is being pressed down
            button: an integer found in constants.mouse that represents
                left, middle, right, or extra mouses.
        """
        return is_mouse_button_down(mouse_map[button])
    
    def is_button_up(self, button):
        """
            Check to see if a specific mouse button is NOT being pressed down
            button: an integer found in constants.mouse that represents
                left, middle, right, or extra mouses.
        """
        return is_mouse_button_up(mouse_map[button])

    def is_button_pressed(self, button):
        """
            Check to see if a specific mouse button is being pressed down ONCE
            Once this is checked, the next frame will return false eventhough the
                mouse button is still held down
            
            button: an integer found in constants.mouse that represents
                left, middle, right, or extra mouses.
        """
        return is_mouse_button_pressed(mouse_map[button])
        # mouse_buttons_state = pygame.mouse.get_pressed(num_buttons=5)
        # return mouse_buttons_state[button]
        

    def is_button_released(self, button):
        """
            Check to see if a specific mouse button is being pressed down ONCE
            
            button: an integer found in constants.mouse that represents
                left, middle, right, or extra mouses.
        """
        return is_mouse_button_released(mouse_map[button])
        # mouse_buttons_state = pygame.mouse.get_pressed(num_buttons=5)
        # return (mouse_buttons_state[button] + 1) % 2

    def has_mouse_moved(self):
        """
            Looks at the movement of the mouse compared to the last frame:
            If both x and y movements are 0, then the mouse has not moved.
            Otherwise, the mouse has moved. Return a bool.
        """
        mouse_delta = get_mouse_delta()
        return mouse_delta.x > 0 or mouse_delta.y > 0
    
    def get_mouse_wheel_move(self):
        """
            This deals with scrolling

            Return values:
                - positive number if scrolled up
                - 0 if not scrolling
                - negative number if scrolled down
        """
        return get_mouse_wheel_move()

    def get_current_coordinates(self):
        """
            Simply ask raylib for the position of the mouse and return it
            as a tuple.
        """
        return (get_mouse_x(), get_mouse_y())