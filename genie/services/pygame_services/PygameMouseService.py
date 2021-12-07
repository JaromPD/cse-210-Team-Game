import pygame
from .constants.mouse import mouse_map

class PygameMouseService:
    def __init__(self):
        """
            Everything that has to do with mouse events
        """
        if not pygame.get_init():
            pygame.init()

    def is_button_down(self, button):
        """
            buttons: a tuple of mouse buttons that whoever calls this function
                wants to check whether is pressed.
                Each key is represented by an integer stored in genie.constants.mouse
            
            Return Value:
                The function will return a DICT that maps the key to either True or False,
                    indicating whether the mouse button is pressed or not
        """
        mouse_buttons_state = pygame.mouse.get_pressed(num_buttons=5)
        return mouse_buttons_state[mouse_map[button]]
        

    def is_button_up(self, button):
        """
            Similar to is_button_pressed() but give the opposite result
        """
        mouse_buttons_state = pygame.mouse.get_pressed(num_buttons=5)
        return (mouse_buttons_state[mouse_map[button]] + 1) % 2

    def has_mouse_moved(self):
        """
            Looks at the movement of the mouse compared to the last frame:
            If both x and y movements are 0, then the mouse has not moved.
            Otherwise, the mouse has moved. Return a bool.
        """
        movement = pygame.mouse.get_rel()
        if movement[0] == 0 and movement[1] == 0:
            return False
        else:
            return True

    def get_current_coordinates(self):
        """
            Simply ask pygame for the position of the mouse and return it
            as a tuple.
        """
        return pygame.mouse.get_pos()