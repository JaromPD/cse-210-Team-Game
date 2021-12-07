from pyray import *

class RaylibAudioService:
    def __init__(self):
        """
            Everything that has to do with sound...
        """
        init_audio_device()
        self._sound_cache = {}

    def _load_sound(self, path):
        """
            - Load in the sound
            - Store the sound to cache
            - return the sound
        """
        sound = load_sound(path)
        self._sound_cache[path] = sound
        return sound

    def play_sound(self, path, volume : float = 1):
        """
            Play a sound given:
                - the path to the sound file (a string)
                - the volume: goes from 0 to 1
        """
        try:
            # Load the sound if it's not in cache, otherwise pull from cache
            sound = self._load_sound(path) if path not in self._sound_cache.keys() \
                    else self._sound_cache[path]
            # Set volume
            set_sound_volume(sound, volume)

            # Play!
            play_sound(sound)
        except:
            print("Cannot find audio file: ", path)