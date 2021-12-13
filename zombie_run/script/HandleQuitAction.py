from genie.script.action import InputAction

class HandleQuitAction(InputAction):
    def __init__(self, priority, keyboard_service):
        super().__init__(priority)
        self._keyboard_service = keyboard_service
        self._ship = None
    
    def execute(self, actors, actions, clock, callback):
        """
            This action handles the quit action
        """
        # If the user clicked the "X" symbol, end the game
        if self._keyboard_service.is_quit():
            callback.on_stop()