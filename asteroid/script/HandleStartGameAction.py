from genie.script.action import InputAction
from genie.services import mouse

class HandleStartGameAction(InputAction):
    def __init__(self, priority, mouse_service, physics_service, actions):
        """
            This action adds a bunch of other actions onto the script when
                the Start Game button is clicked

            actions: a dictionary of the form {"input": [action1, action2,...], "update": [], "output": []}
                    This is a bunch of actions the must be added to the script once the game starts
        """
        super().__init__(priority)
        self._mouse_service = mouse_service
        self._physics_service = physics_service
        self._actions = actions

    def execute(self, actors, actions, clock, callback):
        """
            When left mouse is clicked:
                - check to see if the mouse coordinate collides with the start game button
                - if the mouse collides with the button:
                    + remove the button (or switch it to the "clicked" state)
                    + add all actions in self._actions to the script
        """
        start_button = actors.get_first_actor("start_button")
        mouse_pos = self._mouse_service.get_current_coordinates()

        if start_button != None \
            and self._mouse_service.is_button_down(mouse.LEFT) \
            and self._physics_service.check_collision_point(start_button, mouse_pos):
                actors.remove_actor("start_button", start_button)
                actions.remove_action("input", self)
                for action in self._actions["input"]:
                    actions.add_action("input", action)
                for action in self._actions["update"]:
                    actions.add_action("update", action)
                for action in self._actions["output"]:
                    actions.add_action("output", action)