from genie.script.action import UpdateAction

class HandlePlayerHittingFloorAction(UpdateAction):
    def __init__(self, priority,  window_size):
        super().__init__(priority)
        self._window_size = window_size
        self._player = None
        self._floor = None

    def execute(self, actors, actions, clock, callback):
        """
            Make sure the ship can't move into or under the mothership
        """
        # Find ship and mothership among the actors
        self._player = actors.get_first_actor("player")
        self._floor = actors.get_first_actor("floor")

        if (self._player != None and self._floor != None):
        # Determine the line between ship an mothership:
            line = self._floor.get_top_left()[1] - self._player.get_height()/2

            # Don't allow the ship to go into the mothership
            if (self._player != None and self._player.get_y() > 400):
                self._player.set_y(400)
            # Push the player back when the try to jump too high
            if (self._player != None and self._player.get_y() < 100):
                self._player.set_y(100)          
            