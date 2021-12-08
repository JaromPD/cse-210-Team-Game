from genie.cast.actor import Actor

class PlayerScore(Actor):
    def __init__(self, path: str,
                width: int = 0, 
                height: int = 0, 
                
                x: float = 0, 
                y: float = 0, 
                
                vx: float = 0, 
                vy: float = 0, 
                
                rotation: float = 0, 
                rotation_vel: float = 0,
                
                score : int = 0):

        super().__init__(path, 
                        width=width, 
                        height=height, 
                        
                        x=x, 
                        y=y, 
                        
                        vx=vx, 
                        vy=vy, 
                        
                        rotation=rotation, 
                        rotation_vel=rotation_vel)
        
        self._score = score

    def get_score(self):
        return self._score
    
    def set_score(self, score):
        self._score = score
    
    def add_score(self, points):
        self._score += points
    
    def penalize(self, points):
        self._score -= points