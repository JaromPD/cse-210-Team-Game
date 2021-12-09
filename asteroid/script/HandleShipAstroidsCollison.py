from genie.script.action import UpdateAction

class HandleShipAstroidsCollision(UpdateAction):
    def __init__(self, priority, physics_service, audio_service):
        self._priority = priority
        self._ship = None
        self._score = None
        self._physics_service = physics_service
        self._audio_service = audio_service

    def execute(self, actors, actions, clock, callback):
        """
            This action handles all collisions between the SHIP and the ASTROIDS
        """
        # First look for the ship
        self._ship = actors.get_first_actor("ship")
        heart = actors.get_first_actor("hearts")
        hearts = actors.get_actors("hearts")
        self._score = actors.get_first_actor("score")
        # Only worry about collision if the ship actually exists
        if self._ship != None:
            # Look through all the astroids, see if any collides with ship
            for actor in actors.get_actors("astroids"):
                if self._physics_service.check_collision(self._ship, actor):
                    if heart == None:
                        pass
                    elif len(hearts) == 1:
                        self._score.penalize(100)
                        actors.remove_actor("ship", self._ship)
                        actors.remove_actor("hearts", heart)
                        self._audio_service.play_sound("asteroid/assets/sound/squish.wav", 1)
                        self._audio_service.play_sound("asteroid/assets/sound/death.wav", 1)
                    else:
                        self._score.penalize(100)
                        actors.remove_actor("hearts", heart)
                        actors.remove_actor("astroids", actor)
                        self._audio_service.play_sound("asteroid/assets/sound/squish.wav", 1)
                        self._audio_service.play_sound("asteroid/assets/sound/pain.wav", 1)
                        self._ship = None
                        print(hearts)
                    break