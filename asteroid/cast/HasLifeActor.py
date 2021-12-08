from genie.cast.actor import Actor

class HasLifeActor(Actor):
    def __init__(self, path: str,
                
                health_bar_y_offset : int,
                health_bar_height : int = 5,

                width: int = 0, 
                height: int = 0, 
                
                x: float = 0, 
                y: float = 0, 
                
                vx: float = 0, 
                vy: float = 0, 
                
                rotation: float = 0, 
                rotation_vel: float = 0,
                
                max_hp: int = 0,
                show_text_health : bool = False):
        """
        This class is inherited by any actor that wants to have HP.
        It also holds a few attributes to assist with drawing the health bar
        such as:
            - health_bar_y_offset: how far (vertically) from the center of the actor
                                    the health bar should be
            - health_bar_height: the height of the health bar, default to 5 pixels
        """

        super().__init__(path, 
                        width=width, 
                        height=height, 
                        
                        x=x, 
                        y=y, 
                        
                        vx=vx, 
                        vy=vy, 
                        
                        rotation=rotation, 
                        rotation_vel=rotation_vel)
        self._max_hp = max_hp
        self._current_hp = max_hp
        self._health_bar_y_offset = health_bar_y_offset
        self._health_bar_height = health_bar_height
        self._show_text_health = show_text_health
        # self._health_bar = HealthBar(height = health_bar_height)
        # self._health_bar.on_created(self)

    def set_hp(self, hp):
        self._current_hp = hp
        # self._health_bar.on_update(self)

    def get_hp(self):
        return self._current_hp
    
    def set_max_hp(self, hp):
        self._max_hp = hp
        # self._health_bar.on_update(self)
    
    def get_max_hp(self):
        return self._max_hp
    
    def get_hp_percent(self):
        return self._current_hp / self._max_hp
    
    # def set_health_bar(self, health_bar):
    #     self._health_bar = health_bar

    # def get_health_bar(self):
    #     return self._health_bar
    
    def set_health_bar_y_offset(self, offset):
        self._health_bar_y_offset = offset
    
    def get_health_bar_y_offset(self):
        return self._health_bar_y_offset
    
    def set_health_bar_height(self, height):
        self._health_bar_height = height

    def get_health_bar_height(self):
        return self._health_bar_height
    
    def show_text_health(self):
        return self._show_text_health
    
    def set_show_text_health(self, value):
        self._show_text_health = value

    def take_damage(self, damage):
        self._current_hp -= damage
        # self._health_bar.on_update(self)
    
    def heal(self, heal_amount: int):
        self._current_hp += heal_amount
        if self._current_hp > self._max_hp:
            self._current_hp = self._max_hp
        # self._health_bar.on_update(self)
    
    # def move_with_vel(self):
    #     super().move_with_vel()
    #     self._health_bar.on_update(self)