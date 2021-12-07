"""
Copyright 2021, BYU-Idaho.
Author(s): Matt Manley, Jacob Oliphant
Version: 1.0
Date: 27-01-2021
"""
from abc import ABC
from abc import abstractmethod


class Action(ABC):
    """A thing that is done in an animation.

    The responsibility of Action is to define the common methods for everything 
    that can happen in an animation. Actions are classified as one of three 
    types, INPUT, UPDATE, or OUTPUT. This allows a director to cue an action at 
    the appropriate time. Action is an an abstract base class that must be 
    subclassed for every concrete action of a specific animation or game.

    Attributes:
        _type: str, An action type, or one of INPUT, UPDATE or OUTPUT.
    """           
        
    class Callback(ABC):
        """An action callback.

        The responsibility of Callback is to provide a means for an action to 
        let the triggering object know its time to make a transition. 
        """  
    
        @abstractmethod
        def on_next(self, actors, actions):
            """This method should be called when an animation or game needs to 
            transition to the next scene.
            
            Attributes:
                actors
                actions
            """
            pass

        @abstractmethod
        def on_stop(self):
            """This method should be called when an animation or game is over 
            or has finished."""
            pass

    def __init__(self, priority):
        self._priority = priority
        
    @abstractmethod
    def execute(self, actors, actions, clock, callback):
        """Executes the action using the given cast. This could be detecting 
        input, moving actors, drawing actors, playing sounds or something else. 
        A callback is provided as an argument in case the Action needs to 
        transition to the next scene or signal that the animation or game is 
        over.

        Args:
            cast (Cast): The cast to execute the action for.
            callback (Callback): The callback to notify.
        """
        pass

    def get_priority(self):
        return self._priority

    def set_priority(self, priority):
        self._priority = priority

class InputAction(Action):
    pass

class UpdateAction(Action):
    pass

class OutputAction(Action):
    pass