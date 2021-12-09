from genie.cast.animatedActor import AnimatedActor

class Astroid(AnimatedActor):
    def __init__(self, paths: list, width: int, height: int,
                    animation_fps : int = 10, game_fps : int = 60,
                    event_triggered : bool = False,
                    x: float = 0, y: float = 0, 
                    vx: float = 0, vy: float = 0, 
                    rotation: float = 0, rotation_vel: float = 0,
                    flipped : bool = False):
                    
        self._paths = paths
        self._animation_speed = float(animation_fps) / float(game_fps)
        self._is_animating = False if event_triggered else True
        self._event_triggered = event_triggered
        self._current_frame = 0

        super().__init__(paths, width, height, x=x, y=y, 
                            vx=vx, vy=vy, rotation=rotation, 
                            rotation_vel=rotation_vel, flipped = flipped)