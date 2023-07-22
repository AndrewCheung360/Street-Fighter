import pygame as pg
from settings import *

# state constants
STATE_IDLE = "IDLE"
STATE_WALK = "WALK"
STATE_BACKWALK = "BACKWALK"
STATE_JUMP = "JUMP"
STATE_FORWARD_JUMP = "FORWARD_JUMP"
STATE_BACKWARD_JUMP = "BACKWARD_JUMP"
STATE_CROUCH = "CROUCH"

def update_state(keys, direction, playerNum, current_state = STATE_IDLE, mode="local"):
    if mode == "local":
        if playerNum == "player1":
            # Player 1 key mapping (e.g., WASD)
            if keys[pg.K_d]:
                if direction == "right":
                    return STATE_WALK
                else:
                    return STATE_BACKWALK
            elif keys[pg.K_a]:
                if direction == "right":
                    return STATE_BACKWALK
                else:
                    return STATE_WALK
            elif keys[pg.K_SPACE]:
                return STATE_JUMP
            return STATE_IDLE
        elif playerNum == "player2":
            # Player 2 key mapping (e.g., Arrow keys)
            if keys[pg.K_LEFT]:
                if direction == "left":
                    return STATE_WALK
                else:
                    return STATE_BACKWALK
            elif keys[pg.K_RIGHT]:
                if direction == "left":
                    return STATE_BACKWALK
                else:
                    return STATE_WALK
            elif keys[pg.K_KP0]:
                return STATE_JUMP
            return STATE_IDLE
    else:
        pass

def state_idle(fighter, state):
    fighter.handle_idle(state)

def state_walk(fighter, state):
    fighter.handle_x_movement(state)
    
def state_jump(fighter, state):
    fighter.handle_jump(state)