from pyray import *
from .constants.keys import keys_map

class RaylibKeyboardService():
    def __init__(self):
        """
            This class contains the tools you need to check for
                keyboard events
        """
        pass

    def is_quit(self):
        """
            tell the user whether the X button on the top right is pressed
        """
        return window_should_close()

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
        keys_state = {}
        for key in keys:
            keys_state[key] = is_key_down(keys_map[key])
        
        return keys_state

    def is_key_pressed(self, key):
        """
            check to see if a key is pressed. Returns True for pressed and False for released
        """
        return is_key_pressed(keys_map[key])
        # keys_state_dict = self.get_keys_state(key)
        # return keys_state_dict[key]
    
    def is_key_released(self, key):
        """
            Similar to is_key_pressed, but returns True for released and False for pressed
        """
        return is_key_released(keys_map[key])
        # keys_state_dict = self.get_keys_state(key)
        # return keys_state_dict[key] ^ 1
    
    def is_key_down(self, key):
        return is_key_down(keys_map[key])
    
    def is_key_up(self, key):
        return is_key_up(keys_map[key])