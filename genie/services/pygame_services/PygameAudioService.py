import pygame

class PygameAudioService:
    def __init__(self):
        """
            Everything that has to do with sound...
        """
        if not pygame.get_init():
            pygame.init()
        pygame.mixer.init()
        self._sound_cache = {}

    def _load_sound(self, path):
        """
            - Load in the sound
            - Store the sound to cache
            - return the sound
        """
        sound = pygame.mixer.Sound(path)
        self._sound_cache[path] = sound
        return sound

    def play_sound(self, path, volume : float = 1):
        """
            Play a sound given:
                - the path to the sound file 
                - the volume
        """
        try:
            # Load the sound if it's not in cache, otherwise pull from cache
            sound = self._load_sound(path) if path not in self._sound_cache.keys() \
                    else self._sound_cache[path]
            # Set volume
            sound.set_volume(volume)

            # Play!
            sound.play()
        except:
            print("Cannot find audio file: ", path)