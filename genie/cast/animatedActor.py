from .actor import Actor

class AnimatedActor(Actor):
    def __init__(self, paths: list, width: int, height: int,
                    animation_fps : int = 10, game_fps : int = 60,
                    event_triggered : bool = True,
                    x: float = 0, y: float = 0, 
                    vx: float = 0, vy: float = 0, 
                    rotation: float = 0, rotation_vel: float = 0,
                    flipped : bool = False):

        self._paths = paths
        self._animation_speed = float(animation_fps) / float(game_fps)
        self._is_animating = False if event_triggered else True
        self._event_triggered = event_triggered
        self._current_frame = 0
        super().__init__(paths[0], width, height, x=x, y=y, 
                            vx=vx, vy=vy, rotation=rotation, 
                            rotation_vel=rotation_vel, flipped = flipped)
    
    def get_paths(self):
        return self._paths
    
    def set_paths(self, paths):
        self._paths = paths
    
    def get_current_path(self):
        return self._paths[int(self._current_frame)]

    def get_animation_speed(self):
        return self._animation_speed
    
    def set_animation_speed(self, animation_speed : float):
        self._animation_speed = animation_speed
    
    def is_animating(self):
        return self._is_animating

    def set_animating(self, animating : bool):
        self._is_animating = animating
    
    def set_next_frame(self):
        if self._is_animating:
            self._current_frame += self._animation_speed
        
            if int(self._current_frame) >= len(self._paths):
                self._current_frame = 0
                if self._event_triggered:
                    self._is_animating = False
            
            self._path = self._paths[int(self._current_frame)]