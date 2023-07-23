import pygame as pg
from settings import *

# state constants
STATE_IDLE = "IDLE"
STATE_WALK = "WALK"
STATE_BACKWALK = "BACKWALK"
STATE_JUMP = "JUMP"
STATE_FORWARD_STRAFE = "FORWARD_STRAFE"
STATE_BACKWARD_STRAFE = "BACKWARD_STRAFE"
STATE_FORWARD_JUMP = "FORWARD_JUMP"
STATE_BACKWARD_JUMP = "BACKWARD_JUMP"
STATE_CROUCH = "CROUCH"

vec = pg.math.Vector2

def update_state(fighter, keys, direction, playerNum, current_state = STATE_IDLE, mode="local"):
    if mode == "local":
        if playerNum == "player1":
            # Player 1 key mapping 
            if keys[pg.K_d]:
                if direction == "right":
                    if fighter.active_name == "jump" and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == False:
                        return STATE_FORWARD_STRAFE
                    elif keys[pg.K_SPACE]:
                        return STATE_FORWARD_JUMP
                    return STATE_WALK
                else:
                    if fighter.active_name == "jumpR" and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == False:
                        return STATE_BACKWARD_STRAFE
                    elif keys[pg.K_SPACE]:
                        return STATE_BACKWARD_JUMP
                    return STATE_BACKWALK
            elif keys[pg.K_a]:
                if direction == "right":
                    if fighter.active_name == "jump" and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == False:
                        return STATE_BACKWARD_STRAFE
                    elif keys[pg.K_SPACE]:
                        return STATE_BACKWARD_JUMP
                    return STATE_BACKWALK
                else:
                    if fighter.active_name == "jumpR" and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == False:
                        return STATE_FORWARD_STRAFE
                    elif keys[pg.K_SPACE]:
                        return STATE_FORWARD_JUMP
                    return STATE_WALK
            elif keys[pg.K_s]:
                return STATE_CROUCH
            elif keys[pg.K_SPACE]:
                return STATE_JUMP
            return STATE_IDLE
        elif playerNum == "player2":
            # Player 2 key mapping
            if keys[pg.K_LEFT]:
                if direction == "left":
                    if fighter.active_name == "jumpR" and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == False:
                        return STATE_FORWARD_STRAFE
                    elif keys[pg.K_KP0]:
                        return STATE_FORWARD_JUMP
                    return STATE_WALK
                else:
                    if fighter.active_name == "jump" and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == False:
                        return STATE_BACKWARD_STRAFE
                    elif keys[pg.K_KP0]:
                        return STATE_BACKWARD_JUMP
                    return STATE_BACKWALK
            elif keys[pg.K_RIGHT]:
                if direction == "left":
                    if fighter.active_name == "jumpR" and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == False:
                        return STATE_BACKWARD_STRAFE
                    elif keys[pg.K_KP0]:
                        return STATE_BACKWARD_JUMP
                    return STATE_BACKWALK
                else:
                    if fighter.active_name == "jump" and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == False:
                        return STATE_FORWARD_STRAFE
                    elif keys[pg.K_KP0]:
                        return STATE_FORWARD_JUMP
                    return STATE_WALK
            elif keys[pg.K_DOWN]:
                return STATE_CROUCH
            elif keys[pg.K_KP0]:
                return STATE_JUMP
            return STATE_IDLE
    else:
        pass
    
def state_idle(fighter, state):
    if state == STATE_IDLE and fighter.pos.y == STAGE_FLOOR:
            fighter.vel = vec(0, 0)
            if fighter.direction == "right":
                fighter.set_active_animation("idle")
            else:
                fighter.set_active_animation("idleR")

def state_walk(fighter, state):
    if state == STATE_WALK and fighter.pos.y == STAGE_FLOOR:
        if fighter.direction == "right":
            fighter.vel.x = min(fighter.vel.x + ACCELERATION, MAX_X_VELOCITY)
            fighter.set_active_animation("walk")
        else:
            fighter.vel.x = max(fighter.vel.x - ACCELERATION, -MAX_X_VELOCITY)
            fighter.set_active_animation("walkR")
    elif state == STATE_BACKWALK and fighter.pos.y == STAGE_FLOOR:
        if fighter.direction == "right":
            fighter.vel.x = max(fighter.vel.x - ACCELERATION, -MAX_X_VELOCITY)
            fighter.set_active_animation("backwalk")
        else:
            fighter.vel.x = min(fighter.vel.x + ACCELERATION, MAX_X_VELOCITY)
            fighter.set_active_animation("backwalkR")
    
def state_jump(fighter, state):
    if state == STATE_JUMP and fighter.pos.y == STAGE_FLOOR:
            if fighter.direction == "right":
                fighter.set_active_animation("jump")
            else:
                fighter.set_active_animation("jumpR")
                
            fighter.vel.y = JUMP_SPEED
    elif state == STATE_FORWARD_STRAFE and fighter.pos.y < STAGE_FLOOR:
        if fighter.direction == "right":
            fighter.vel.x = min(fighter.vel.x + AIR_ACCELERATION, MAX_X_VELOCITY)
        else:
            fighter.vel.x = max(fighter.vel.x - AIR_ACCELERATION, -MAX_X_VELOCITY)
    elif state == STATE_BACKWARD_STRAFE and fighter.pos.y < STAGE_FLOOR:
        if fighter.direction == "right":
            fighter.vel.x = max(fighter.vel.x - AIR_ACCELERATION, -MAX_X_VELOCITY)
        else:
            fighter.vel.x = min(fighter.vel.x + AIR_ACCELERATION, MAX_X_VELOCITY)
        
    
def state_directional_jump(fighter,state):
    if state == STATE_FORWARD_JUMP and fighter.pos.y == STAGE_FLOOR:
        if fighter.direction == "right":
            fighter.set_active_animation("forward_jump")
            fighter.vel.y = JUMP_SPEED
            fighter.vel.x = 8
        else:
            fighter.set_active_animation("forward_jumpR")
            fighter.vel.y = JUMP_SPEED
            fighter.vel.x = -8
    elif state == STATE_BACKWARD_JUMP and fighter.pos.y == STAGE_FLOOR:
        if fighter.direction == "right":
            fighter.set_active_animation("backward_jump")
            fighter.vel.y = JUMP_SPEED
            fighter.vel.x = -8
        else:
            fighter.set_active_animation("backward_jumpR")
            fighter.vel.y = JUMP_SPEED
            fighter.vel.x = 8

def state_crouch(fighter, state):
    if state == STATE_CROUCH and fighter.pos.y == STAGE_FLOOR:
            fighter.vel = vec(0, 0)
            if fighter.direction == "right":
                fighter.set_active_animation("crouch")
            else:
                fighter.set_active_animation("crouchR")