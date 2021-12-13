
from genie.script.action import UpdateAction

class HandleOffscreenAction(UpdateAction):
    def __init__(self, priority,  window_size):
        super().__init__(priority)
        self._window_size = window_size
        self._player = None
        self._mother_ship = None

    def execute(self, actors, actions, clock, callback):
        """
            Handle all actors' behavior when they're about to
            go off the screen
        """
        # Look for the ship
        self._player = actors.get_first_actor("player")
        
        # Don't allow the ship to go off the screen
        if (self._player != None):
            if self._player.get_top_right()[0] >= self._window_size[0]:
                self._player.set_x(int(self._window_size[0] - self._player.get_width()/2))
            if self._player.get_top_left()[0] <= 0:
                self._player.set_x(int(self._player.get_width()/2))
            if self._player.get_bottom_left()[1] >= self._window_size[1]:
                self._player.set_y(int(self._window_size[1] - self._player.get_height()/2))
            if self._player.get_top_left()[1] <= 0:
                self._player.set_y(int(self._player.get_height()/2))
        
        # If it's a bullet or astroid goin off the screen, just remove it.
        for actor in actors.get_actors("monsters"):
            # if isinstance(actor, Astroid) or isinstance(actor, Bullet):
            if (actor.get_x() > self._window_size[0]
                or actor.get_x() < 0
                or actor.get_y() > self._window_size[1]
                or actor.get_y() < 0):
                actors.remove_actor("monsters", actor)