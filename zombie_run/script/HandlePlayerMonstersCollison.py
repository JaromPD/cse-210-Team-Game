from genie.script.action import UpdateAction

class HandlePlayerMonstersCollision(UpdateAction):
    def __init__(self, priority, physics_service, audio_service):
        self._priority = priority
        self._player = None
        self._score = None
        self._physics_service = physics_service
        self._audio_service = audio_service
        self._death_paths = []
        for i in range(9):
            self._death_paths.append(f"zombie_run/assets/zombie/dead/__Zombie01_Dead_00{i}.png")

    def execute(self, actors, actions, clock, callback):
        """
            This action handles all collisions between the SHIP and the ASTROIDS
        """
        # First look for the player
        self._player = actors.get_first_actor("player")
        heart = actors.get_first_actor("hearts")
        hearts = actors.get_actors("hearts")
        self._score = actors.get_first_actor("score")
        # Only worry about collision if the player actually exists
        if self._player != None:
            # Look through all the monsters, see if any collides with ship
            for actor in actors.get_actors("monsters"):
                if self._physics_service.check_collision(self._player, actor):
                    if heart == None:
                        pass
                    elif len(hearts) == 1:
                        self._score.penalize(100)
                        #self._player.set_paths(self._death_paths)
                        actors.remove_actor("player", self._player)
                        actors.remove_actor("hearts", heart)
                        self._audio_service.play_sound("zombie_run/assets/sound/squish.wav", 1)
                        self._audio_service.play_sound("zombie_run/assets/sound/death.wav", 3)
                    else:
                        self._score.penalize(100)
                        actors.remove_actor("hearts", heart)
                        actors.remove_actor("monsters", actor)
                        self._audio_service.play_sound("zombie_run/assets/sound/squish.wav", 1)
                        self._audio_service.play_sound("zombie_run/assets/sound/pain.wav", 1)
                        self._player = None
                        print(hearts)
                    break