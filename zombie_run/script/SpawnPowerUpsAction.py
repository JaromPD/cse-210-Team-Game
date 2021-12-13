from genie.script.action import UpdateAction
from zombie_run.cast.astroid import Astroid
from genie.cast.animatedActor import Actor

import random
import time

SPAWN_INTERVAL = 5.0         # seconds
LARGE_SIZE = (175, 175)
MEDIUM_SIZE = (100, 100)
SMALL_SIZE = (40, 40)

LARGE = 1
MEDIUM = 2
SMALL = 3

class SpawnPowerUpsAction(UpdateAction):
    def __init__(self, priority, window_size):
        super().__init__(priority)
        self._timer_started = False
        self._last_spawn = 0 # seconds
        self._window_size = window_size
        self._astroid_spawn = False

    def _create_power(self, type: int, x: int, y:int):
        """
            This is a helper function that creates an astroid based on
            the input "type" and the initial position
        """
        if type == LARGE:
            vel_x = -2 if x > self._window_size[0] / 2 else 1
            vel_y = 0
            return Actor("zombie_run/assets/power-ups/38.png",
                            width =50, 
                            height=50,
                            x=x, y=y, 
                            vx=vel_x, vy=vel_y, rotation=0, 
                            rotation_vel=0, flipped = False
                            )

        elif type == MEDIUM:
            vel_x = -2 if x > self._window_size[0] / 2 else 2
            vel_y = 0
            return Actor("zombie_run/assets/power-ups/37.png",
                            width = 50, 
                            height= 50,
                            x=x, y=y, 
                            vx=vel_x, vy=vel_y, rotation=0, 
                            rotation_vel=0, flipped = False
                            )
  

        if type == SMALL:
            vel_x = -2 if x > self._window_size[0] / 2 else 3
            vel_y = 0
            return Actor("zombie_run/assets/power-ups/13.png",
                            width =50, 
                            height=50,                        
                            x=x, y=y, 
                            vx=vel_x, vy=vel_y, rotation=0, 
                            rotation_vel=0, flipped = False
                            )

    def execute(self, actors, actions, clock, callback):
        """
            - Check to see if it's time to spawn another astroid
            - Randomly pick Small, Medium, or Large
            - Pick and initial position for the astroid
            - Create the astroid by calling self._create_astroid_by_type
            - Add the astroid to the cast
            - Record the most recent spawn
        """
        player = actors.get_first_actor("player")
        if not self._timer_started:
            self._timer_started = True
            self._last_spawn = time.time()

        
        if time.time() - self._last_spawn >= SPAWN_INTERVAL and player != None:
            # Pick a random type of astroid: Small, Medium, Large
            power_type = random.randint(1,3)

            # Generate a random position on top of the screen,
            #  limit the spawn range from 1/8 of the screen to 7/8 of the screen
            lower_x_bound = int(self._window_size[0] / 8)
            upper_x_bound = int(self._window_size[0] - lower_x_bound)

            if power_type == 3:
                start_pos_x = random.randint(300,900)
                start_pos_y = 415
                power_up = self._create_power(power_type, start_pos_x, start_pos_y)
                actors.add_actor("add_power_up", power_up)
            elif power_type == 2:
                start_pos_x = random.randint(300,900)
                start_pos_y = 415
                power_up = self._create_power(power_type, start_pos_x, start_pos_y)
                actors.add_actor("multiply_power_up", power_up)
            else:
                start_pos_x = random.randint(300,900)
                start_pos_y = 415
                power_up = self._create_power(power_type, start_pos_x, start_pos_y)
                actors.add_actor("divide_power_up", power_up)


          

            # set last_spawn to current frame
            self._last_spawn = time.time()