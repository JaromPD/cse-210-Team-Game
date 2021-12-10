from genie.script.action import InputAction
from genie.services import keys

import time

JUMP_INTERVAL = 0.2
VEL = 5

class HandleShipMovementAction(InputAction):
    def __init__(self, priority, keyboard_service):
        super().__init__(priority)
        self._keyboard_service = keyboard_service
        self._ship = None
        self._timer_started = False
        self._last_jump = 0
        self._is_jumping = False

    def execute(self, actors, actions, clock, callback):
        """
            This action handles the input of the player to make the ship move
        """

        # Start the timer
        if not self._timer_started:
            self._timer_started = True
            self._last_jump = time.time()     

        # Look for the ship among the actors if we haven't already known it
        self._ship = actors.get_first_actor("ship")
        
        # Don't worry about it if ship doesn't exist
        if (self._ship != None):
            
            # Check which keys are pressed and update the ship's velocity accordingly
            keys_state = self._keyboard_service.get_keys_state(keys.LEFT, keys.RIGHT, keys.DOWN, keys.UP)
            if keys_state[keys.LEFT]:
                self._ship.set_vx(-VEL)
            if keys_state[keys.RIGHT]:
                self._ship.set_vx(VEL)
            if keys_state[keys.DOWN]:
                self._ship.set_vy(VEL)
            if keys_state[keys.UP]:
                if self._jump_timer < 50:
                    self._jump_timer += 1
                    self._ship.set_vy(-10)
                elif self._jump_timer < 100 and self._jump_timer >= 50:
                    self._jump_timer += 1
                    self._ship.set_vy(10)
                
            if not keys_state[keys.UP]:
                if self._ship.get_y() < 400:
                    self._jump_timer += 100
                if self._ship.get_y() >= 400:
                    self._jump_timer = 0
                self._ship.set_vy(10)
            
            # If keys in either dirrection are not pressed, set velocity of that direction to 0
            if not keys_state[keys.LEFT] and not keys_state[keys.RIGHT]:
                self._ship.set_vx(0)
            if not keys_state[keys.UP] and not keys_state[keys.DOWN]:
                self._ship.set_vy(10)