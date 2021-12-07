import pygame
from .constants.keys import keys_map

class PygameKeyboardService():
    def __init__(self):
        """
            Everything that has to do with keyboard events
        """
        if not pygame.get_init():
            pygame.init()

    def is_quit(self):
        """
            tell the user whether the X button on the top right is pressed
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False

    def get_keys_state(self, *keys):
        """
            keys: a tuple of keys that whoever calls this function
                wants to check whether is pressed.
                Each key is represented by an integer stored in genie.constants.keys
            
            Return Value:
                The function will return a DICT that maps the key to either 1 or 0,
                    with 1 meaning the key is pressed and 0 meaning it's not pressed.
            
            Note: There is a chance that some keys might not get detected if multiple
                keys are pressed at the same time
        """
        pygame.event.pump()
        keys_pressed = {}
        keys_state = pygame.key.get_pressed()
        for key in keys:
            keys_pressed[key] = keys_state[keys_map[key]]
        
        return keys_pressed

    def is_key_down(self, key):
        """
            check to see if a key is pressed. Returns True for pressed and False for released
        """
        keys_state_dict = self.get_keys_state(key)
        return keys_state_dict[key]
    
    def is_key_up(self, key):
        """
            Similar to is_key_pressed, but returns True for released and False for pressed
        """
        keys_state_dict = self.get_keys_state(key)
        return keys_state_dict[key] ^ 1