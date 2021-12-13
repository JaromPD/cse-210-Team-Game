from genie.script.action import OutputAction
from genie.services import colors

class DrawGameOverAction(OutputAction):
    def __init__(self, priority, screen_service):
        super().__init__(priority)
        self._player = None
        self._screen_service = screen_service

    def get_priority(self):
        return super().get_priority()
    
    def set_priority(self, priority):
        return super().set_priority(priority)

    def execute(self, actors, actions, clock, callback):
        """
            - Look for the score actor in the actors list
            - Print the score on the screen
        """
    
        self._player = actors.get_first_actor("player")
            # for actor in actors:
            #     if isinstance(actor, PlayerScore):
            #         self._score = actor
            #         break
        if self._player == None:
            self._screen_service.draw_text("Game Over!", font_size=100, color=colors.RED, position= (200,250))