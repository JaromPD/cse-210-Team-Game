from astroid.cast.HasLifeActor import HasLifeActor

class MotherShip(HasLifeActor):
    def __init__(self, path: str,
                health_bar_y_offset: int,
                health_bar_height: int = 5,
                
                width: int = 0, 
                height: int = 0, 
                
                x: float = 0, 
                y: float = 0, 
                
                vx: float = 0, 
                vy: float = 0, 
                
                rotation: float = 0, 
                rotation_vel: float = 0,
                
                max_hp: int = 100,
                show_text_health : bool = False):

        super().__init__(path,
                        health_bar_y_offset = health_bar_y_offset,
                        health_bar_height = health_bar_height,

                        width=width, 
                        height=height, 
                        
                        x=x, 
                        y=y, 
                        
                        vx=vx, 
                        vy=vy, 
                        
                        rotation=rotation, 
                        rotation_vel=rotation_vel,
                        
                        max_hp=max_hp,
                        show_text_health=show_text_health)
