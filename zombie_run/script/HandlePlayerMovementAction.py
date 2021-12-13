from genie.script.action import InputAction
from genie.services import keys

import time

JUMP_INTERVAL = 0.2
VEL = 5

class HandlePlayerMovementAction(InputAction):
    def __init__(self, priority, keyboard_service):
        super().__init__(priority)
        self._keyboard_service = keyboard_service
        self._player = None
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
        self._player = actors.get_first_actor("player")
        
        # Don't worry about it if ship doesn't exist
        if (self._player != None):
            
            # Check which keys are pressed and update the ship's velocity accordingly
            keys_state = self._keyboard_service.get_keys_state(keys.LEFT, keys.RIGHT, keys.DOWN, keys.UP)
            if keys_state[keys.LEFT]:
                self._player.set_vx(-VEL)
            if keys_state[keys.RIGHT]:
                self._player.set_vx(VEL)
            if keys_state[keys.DOWN]:
                self._player.set_vy(VEL)
            if keys_state[keys.UP]:
                if self._jump_timer < 20:
                    self._jump_timer += 1
                    self._player.set_vy(-8)
                elif self._jump_timer < 40 and self._jump_timer >= 20:
                    self._jump_timer += 1
                    self._player.set_vy(8)
                
            if not keys_state[keys.UP]:
                if self._player.get_y() < 400:
                    self._jump_timer += 100
                if self._player.get_y() >= 400:
                    self._jump_timer = 0
                self._player.set_vy(8)
            
            # If keys in either dirrection are not pressed, set velocity of that direction to 0
            if not keys_state[keys.LEFT] and not keys_state[keys.RIGHT]:
                self._player.set_vx(0)
            if not keys_state[keys.UP] and not keys_state[keys.DOWN]:
                self._player.set_vy(10)