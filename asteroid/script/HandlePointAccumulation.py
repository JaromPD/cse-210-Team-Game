from genie.script.action import UpdateAction

import time

SCORE_INTERVAL = 2.0

class HandlePointAccumulation(UpdateAction):
    def __init__(self, priority, window_size):
        super().__init__(priority)
        self._score = None
        self._timer_started = False
        self._last_score = 0 # seconds

    def execute(self, actors, actions, clock, callback):
        """
            - Check to see if it's time to spawn another astroid
            - Randomly pick Small, Medium, or Large
            - Pick and initial position for the astroid
            - Create the astroid by calling self._create_astroid_by_type
            - Add the astroid to the cast
            - Record the most recent spawn
        """
        ship = actors.get_first_actor("ship")
        if ship != None:
            if not self._timer_started:
                self._timer_started = True
                self._last_score = time.time()
            
            if time.time() - self._last_score >= SCORE_INTERVAL:
                # get the score actor
                self._score = actors.get_first_actor("score")
    
                # spawn an astroid
                self._score.add_score(50)
    
                # set last_spawn to current frame
                self._last_score = time.time()