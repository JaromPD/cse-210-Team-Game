from genie.script.action import UpdateAction

import time
import random

SCORE_INTERVAL = 30.0

class HandleBackgroundChange(UpdateAction):
    def __init__(self, priority, window_size):
        super().__init__(priority)
        self._score = None
        self._timer_started = False
        self._last_score = 0 # seconds
        self._bg_1 = "zombie_run/assets/1_game_background.png"
        self._bg_2 = "zombie_run/assets/2_game_background.png"
        self._bg_3 = "zombie_run/assets/3_game_background.png"
        self._bg_choice = "zombie_run/assets/3_game_background.png"
        self._bg_choices_1 = ["zombie_run/assets/1_game_background.png","zombie_run/assets/2_game_background.png"]
        self._bg_choices_2 = ["zombie_run/assets/3_game_background.png","zombie_run/assets/1_game_background.png"]
        self._bg_choices_3 = ["zombie_run/assets/3_game_background.png","zombie_run/assets/2_game_background.png"]

    def execute(self, actors, actions, clock, callback):
        """
            - Check to see if it's time to spawn another astroid
            - Randomly pick Small, Medium, or Large
            - Pick and initial position for the astroid
            - Create the astroid by calling self._create_astroid_by_type
            - Add the astroid to the cast
            - Record the most recent spawn
        """
        self._score = actors.get_first_actor("score")
        background = actors.get_first_actor("background_image")
        if not self._timer_started:
            self._timer_started = True
            self._last_score = time.time()
       
        if background.get_path() == self._bg_1:
            bg_choice = random.choice(self._bg_choices_3)

        if background.get_path() == self._bg_2:
            bg_choice = random.choice(self._bg_choices_2)
        
        if background.get_path() == self._bg_3:
            bg_choice = random.choice(self._bg_choices_1)

        if time.time() - self._last_score >= SCORE_INTERVAL:                   
            background.set_path(bg_choice)

            
            self._last_score = time.time()