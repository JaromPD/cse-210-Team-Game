from genie.script.action import UpdateAction
from asteroid.cast.astroid import Astroid
from genie.cast.animatedActor import AnimatedActor

import random
import time

SPAWN_INTERVAL = 2.0          # seconds
LARGE_SIZE = (175, 175)
MEDIUM_SIZE = (100, 100)
SMALL_SIZE = (40, 40)

LARGE = 1
MEDIUM = 2
SMALL = 3

class SpawnAstroidsAction(UpdateAction):
    def __init__(self, priority, window_size):
        super().__init__(priority)
        self._timer_started = False
        self._last_spawn = 0 # seconds
        self._window_size = window_size
        self._astroid_spawn = False
        self._small_paths = []
        for i in range(7):
            self._small_paths.append(f"asteroid/assets/goblin/walk/__Goblin01_Walk_00{i}.png")
        self._bats_path = []
        for i in range(7):
            self._bats_path.append(f"asteroid/assets/bats/flying/__Bat01_Fly_00{i}.png")
        self._reaper_path = []
        for i in range(7):
            self._reaper_path.append(f"asteroid/assets/Reaper/attack/__Grim_Attack_00{i}.png")

    def _create_astroid(self, type: int, x: int, y:int):
        """
            This is a helper function that creates an astroid based on
            the input "type" and the initial position
        """
        if type == LARGE:
            vel_x = -10 if x > self._window_size[0] / 2 else 1
            vel_y = 0
            return AnimatedActor(self._reaper_path,
                            width =100, 
                            height=100,
                            animation_fps=7,
                            game_fps=60,
                            event_triggered=False,
                            x=x, y=y, 
                            vx=vel_x, vy=vel_y, rotation=0, 
                            rotation_vel=0, flipped = False
                            )

        elif type == MEDIUM:
            vel_x = -8 if x > self._window_size[0] / 2 else 2
            vel_y = 0
            return AnimatedActor(self._bats_path,
                            width =100, 
                            height=100,
                            animation_fps=7,
                            game_fps=60,
                            event_triggered=False,
                            x=x, y=y, 
                            vx=vel_x, vy=vel_y, rotation=0, 
                            rotation_vel=0, flipped = False
                            )
  

        if type == SMALL:
            vel_x = -2 if x > self._window_size[0] / 2 else 3
            vel_y = 0
            return AnimatedActor(self._small_paths,
                            width =100, 
                            height=100,
                            animation_fps=7,
                            game_fps=60,
                            event_triggered=False,
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
        if not self._timer_started:
            self._timer_started = True
            self._last_spawn = time.time()
        
        if time.time() - self._last_spawn >= SPAWN_INTERVAL:
            # Pick a random type of astroid: Small, Medium, Large
            astroid_type = random.randint(1,3)

            # Generate a random position on top of the screen,
            #  limit the spawn range from 1/8 of the screen to 7/8 of the screen
            lower_x_bound = int(self._window_size[0] / 8)
            upper_x_bound = int(self._window_size[0] - lower_x_bound)

            if astroid_type == 3:
                start_pos_x = 990
                start_pos_y = 415
            elif astroid_type == 2:
                start_pos_x = 990
                start_pos_y = 200
            else:
                start_pos_x = 990
                start_pos_y = 350


            # spawn an astroid
            astroid = self._create_astroid(astroid_type, start_pos_x, start_pos_y)
            #astroid.set_animating(True)
            actors.add_actor("astroids", astroid)

            # set last_spawn to current frame
            self._last_spawn = time.time()