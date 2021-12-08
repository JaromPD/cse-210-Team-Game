from genie.script.action import OutputAction
from genie.services import colors

from asteroid.cast.ship import Ship

class DrawActorsAction(OutputAction):
    def __init__(self, priority, screen_service):
        super().__init__(priority)
        self._screen_service = screen_service

    def get_priority(self):
        return super().get_priority()
    
    def set_priority(self, priority):
        return super().set_priority(priority)

    def execute(self, actors, actions, clock, callback):
        """
            Loop through the actors and draw a rectangle for each actor
        """
        self._screen_service.fill_screen(colors.WHITE)
        # self._screen_service.draw_actors(actors)
        for actor in actors.get_all_actors():
            # Black for astroids, blue for ship
            color = (0,0,255,255) if isinstance(actor, Ship) else (0,0,0,255)
            self._screen_service.draw_rectangle(actor.get_position(), actor.get_width(), actor.get_height(), color, border_width = 5)