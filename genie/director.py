from .cast.cast import Cast
from .script.script import Script
from .script.action import Action
from .clock import Clock
import time

class Director(Action.Callback):
    def __init__(self):
        """
            This is the soul of the framework.
                It holds the cast, the script, and direct the game loop.
        """
        self._cast = Cast()
        self._script = Script()
        self._clock = Clock()
        self._is_directing = True
    
    def direct_scene(self, cast : Cast, script : Script):
        """
            Direct a scene given a cast and a script
        """
        self._cast = cast
        self._script = script
        self._is_directing = True
        # time1 = time.time()
        # frame_counter = 0
        while self._is_directing:
            # frame_counter += 1
            self._do_inputs()
            self._do_updates()
            self._do_outputs()
            # frame_counter += 1
            # if time.time() - time1 >= 1:
            #     print(frame_counter)
            #     frame_counter = 0
            #     time1 = time.time()
                
    def on_stop(self):
        """
            What happens when the user exit the program?
        """
        # well, stop the game loop!
        self._is_directing = False
    
    def on_next(self, actors, actions):
        """
            This is not completed and needs more thought...
            But it's basically the place where you completely change the
                cast and the script to have a new scene of the game
        """
        self._cast = actors
        self._script = actions

    def _do_inputs(self):
        """
            Cues the input actions for the given cast and script. This method 
            also ticks the animation clock forward since it is the beginning of the 
            animation frame.
        """
        self._clock.tick()
        for action in self._script.get_actions("input"):
            action.execute(self._cast, self._script, self._clock, self)

    def _do_updates(self):
        """
            Cues the update actions for the given cast and script. This method 
            will execute the actions over and over until the animation time has 
            caught up with the real time.
        """
        while self._clock.is_lagging():
            for action in self._script.get_actions("update"):
                action.execute(self._cast, self._script, self._clock, self)
            self._clock.catch_up()
    
    def _do_outputs(self):
        """
            Cues the output actions for the given cast and script.
        """
        for action in self._script.get_actions("output"):
            action.execute(self._cast, self._script, self._clock, self)