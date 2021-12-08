from genie.script.action import OutputAction
from genie.services import colors

class DrawScoreAction(OutputAction):
    def __init__(self, priority, screen_service):
        super().__init__(priority)
        self._score = None
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
        if (self._score == None):
            self._score = actors.get_first_actor("score")
            # for actor in actors:
            #     if isinstance(actor, PlayerScore):
            #         self._score = actor
            #         break
        if self._score != None:
            self._screen_service.draw_text("Score: " + str(self._score.get_score()), font_size=48, color=colors.RED, position= (20,20))