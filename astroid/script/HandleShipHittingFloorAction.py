from genie.script.action import UpdateAction

class HandleShipHittingFloorAction(UpdateAction):
    def __init__(self, priority,  window_size):
        super().__init__(priority)
        self._window_size = window_size
        self._ship = None
        self._floor = None

    def execute(self, actors, actions, clock, callback):
        """
            Make sure the ship can't move into or under the mothership
        """
        # Find ship and mothership among the actors
        self._ship = actors.get_first_actor("ship")
        self._floor = actors.get_first_actor("floor")

        if (self._ship != None and self._floor != None):
        # Determine the line between ship an mothership:
            line = self._floor.get_top_left()[1] - self._ship.get_height()/2

            # Don't allow the ship to go into the mothership
            if (self._ship != None and self._ship.get_y() > line):
                self._ship.set_y(line)
            