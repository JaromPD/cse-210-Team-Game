"""
Copyright 2021, BYU-Idaho.
Author(s): Matt Manley, Jacob Oliphant
Version: 1.0
Date: 27-01-2021
"""
import time


class Clock:
    """The animation clock.
    
    The responsibility of Clock is to keep track of time in both the real 
    world and the animation world. See https://gameprogrammingpatterns.com/ for 
    a good explanation of how this works.

    Attributes:
        _lag (float): The amount of time the animation is behind the real world.
        _last (float): The previously marked time in the real world.
        _fps (float): The number of frames that happen every second.
        _frames (float): A running total of frames.
        _seconds (float): A running total of seconds.
        _updates (float): A running total of updates.
        _ups (float): The number of updates that happen every second.
    """

    TIME_STEP = 1/60
    """float: The fixed frame rate (about 16 ms)."""


    def __init__(self):
        """Initializes a new instance of Clock."""
        self._lag = 0.0
        self._previous = time.time()
        self._frames = 0
        self._seconds = 0.0
        self._updates = 0
        self._stats = {}
        
    def catch_up(self):
        """Catches animation time up by one fixed time step. This method should be called once at the end of each frame's update phase.
        """
        self._lag -= self.TIME_STEP
        self._updates += 1

    def get_stats(self):
        return self._stats

    def is_lagging(self):
        """Whether or not the animation time is lagging behind that of the real 
        world. 

        Returns:
            bool: True if lag is greater than the fixed time step; false if 
            otherwise.
        """
        return self._lag >= self.TIME_STEP

    def tick(self):
        """Marks the real world time so that we are able to measure lag. This 
        should be called once at the beginning of each frame.
        """
        current: float = time.time()
        elapsed: float = current - self._previous
        self._previous = current
        self._lag += elapsed
        self._frames += 1
        # self._calc_stats(elapsed)
        
