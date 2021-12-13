from genie.script.action import OutputAction

class PlayBackgroundMusicAction(OutputAction):
    def __init__(self, priority, path, audio_service):
        super().__init__(priority)
        self._audio_service = audio_service
        self._background_playing = False
        self._path = path
       
    
    def execute(self, actors, actions, clock, callback):
        """
            If the background music is not already playing, play it
        """
        if not self._background_playing:
            self._audio_service.play_sound(self._path, 1)
            self._background_playing = True