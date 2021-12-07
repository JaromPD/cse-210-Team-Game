from genie.script.action import UpdateAction

class MoveActorsAction(UpdateAction):
    def __init__(self, priority, physics_service):
        super().__init__(priority=priority)
        self._physics_service = physics_service

    def execute(self, actors, actions, clock, callback):
        """
            This action:
                - Moves all the actors according to its velocity (including the ship)
                - Rotates all the actors based on its rotational velocity
        """
        self._physics_service.move_actors(actors.get_all_actors())
        self._physics_service.rotate_actors(actors.get_all_actors())