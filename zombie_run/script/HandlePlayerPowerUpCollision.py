from genie.script.action import UpdateAction
from zombie_run.cast.hearts import Heart

class HandlePlayerPowerUpCollision(UpdateAction):
    def __init__(self, priority, physics_service, audio_service):
        self._priority = priority
        self._player = None
        self._score = None
        self._physics_service = physics_service
        self._audio_service = audio_service
        self._extra_life_path = "zombie_run/assets/power-ups/30.png"

    def execute(self, actors, actions, clock, callback):
        """
            This action handles all collisions between the SHIP and the ASTROIDS
        """
        # First look for the player
        self._player = actors.get_first_actor("player")
        self._score = actors.get_first_actor("score")
        # Only worry about collision if the player actually exists
        if self._player != None:
            # Look through all the monsters, see if any collides with ship
            for actor in actors.get_actors("multiply_power_up"):
                if self._physics_service.check_collision(self._player, actor):                
                        self._score.mult_score(2)
                        actors.remove_actor("multiply_power_up", actor)
            for actor in actors.get_actors("add_power_up"):
                if self._physics_service.check_collision(self._player, actor):                
                        self._score.add_score(500)
                        actors.remove_actor("add_power_up", actor)
            for actor in actors.get_actors("divide_power_up"):
                if self._physics_service.check_collision(self._player, actor):                
                        self._score.div_score(2)
                        actors.remove_actor("divide_power_up", actor)
 