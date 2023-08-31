import pygame as pg
from settings import *

# state constants

#movement
STATE_IDLE = "IDLE"
STATE_WALK = "WALK"
STATE_BACKWALK = "BACKWALK"
STATE_JUMP = "JUMP"
STATE_FORWARD_STRAFE = "FORWARD_STRAFE"
STATE_BACKWARD_STRAFE = "BACKWARD_STRAFE"
STATE_FORWARD_JUMP = "FORWARD_JUMP"
STATE_BACKWARD_JUMP = "BACKWARD_JUMP"
STATE_CROUCH = "CROUCH"

#attacks
STATE_LIGHT_PUNCH = "LIGHT_PUNCH"
STATE_MEDIUM_PUNCH = "MEDIUM_PUNCH"
STATE_HEAVY_PUNCH = "HEAVY_PUNCH"
STATE_LIGHT_KICK = "LIGHT_KICK"
STATE_MEDIUM_KICK = "MEDIUM_KICK"
STATE_HEAVY_KICK = "HEAVY_KICK"

STATE_CLOSE_LIGHT_PUNCH = "CLOSE_LIGHT_PUNCH"
STATE_CLOSE_MEDIUM_PUNCH = "CLOSE_MEDIUM_PUNCH"
STATE_CLOSE_HEAVY_PUNCH = "CLOSE_HEAVY_PUNCH"
STATE_CLOSE_LIGHT_KICK = "CLOSE_LIGHT_KICK"
STATE_CLOSE_MEDIUM_KICK = "CLOSE_MEDIUM_KICK"
STATE_CLOSE_HEAVY_KICK = "CLOSE_HEAVY_KICK"

STATE_CROUCH_LIGHT_PUNCH = "CROUCH_LIGHT_PUNCH"
STATE_CROUCH_MEDIUM_PUNCH = "CROUCH_MEDIUM_PUNCH"
STATE_CROUCH_HEAVY_PUNCH = "CROUCH_HEAVY_PUNCH"
STATE_CROUCH_LIGHT_KICK = "CROUCH_LIGHT_KICK"
STATE_CROUCH_MEDIUM_KICK = "CROUCH_MEDIUM_KICK"
STATE_CROUCH_HEAVY_KICK = "CROUCH_HEAVY_KICK"

STATE_JUMP_LIGHT_PUNCH = "JUMP_LIGHT_PUNCH"
STATE_JUMP_MEDIUM_PUNCH = "JUMP_MEDIUM_PUNCH"
STATE_JUMP_HEAVY_PUNCH = "JUMP_HEAVY_PUNCH"
STATE_JUMP_LIGHT_KICK = "JUMP_LIGHT_KICK"
STATE_JUMP_MEDIUM_KICK = "JUMP_MEDIUM_KICK"
STATE_JUMP_HEAVY_KICK = "JUMP_HEAVY_KICK"

STATE_DIAGONAL_JUMP_LIGHT_PUNCH = "DIAGONAL_JUMP_LIGHT_PUNCH"
STATE_DIAGONAL_JUMP_MEDIUM_PUNCH = "DIAGONAL_JUMP_MEDIUM_PUNCH"
STATE_DIAGONAL_JUMP_HEAVY_PUNCH = "DIAGONAL_JUMP_HEAVY_PUNCH"
STATE_DIAGONAL_JUMP_LIGHT_KICK = "DIAGONAL_JUMP_LIGHT_KICK"
STATE_DIAGONAL_JUMP_MEDIUM_KICK = "DIAGONAL_JUMP_MEDIUM_KICK"
STATE_DIAGONAL_JUMP_HEAVY_KICK = "DIAGONAL_JUMP_HEAVY_KICK"

STATE_HURT_HEAD_LIGHT = "HURT_HEAD_LIGHT"
STATE_HURT_HEAD_MEDIUM = "HURT_HEAD_MEDIUM"
STATE_HURT_HEAD_HEAVY = "HURT_HEAD_HEAVY"
STATE_HURT_BODY_LIGHT = "HURT_HEAD_LIGHT"
STATE_HURT_BODY_MEDIUM = "HURT_HEAD_MEDIUM"
STATE_HURT_BODY_HEAVY = "HURT_HEAD_HEAVY"
STATE_HURT_CROUCH_LIGHT = "HURT_CROUCH_LIGHT"
STATE_HURT_CROUCH_MEDIUM = "HURT_CROUCH_MEDIUM"
STATE_HURT_CROUCH_HEAVY = "HURT_CROUCH_HEAVY"

STATE_WAIT = "WAIT"
STATE_CROUCH_WAIT = "CROUCH_WAIT"

vec = pg.math.Vector2

    # elif playerNum == "player2":
    #     # Player 2 key mapping
    #     if "HURT" in current_state:
    #         return current_state
    #     if keys[pg.K_KP4]:
    #         if current_state == STATE_IDLE or "WALK" in current_state or current_state == STATE_LIGHT_PUNCH or current_state == STATE_CLOSE_LIGHT_PUNCH:
    #             if "light_punch" in fighter.active_name and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == True:
    #                 return STATE_WAIT
    #             if abs(fighter.opponent.pos.x - fighter.pos.x) <= 116 and "punch" not in fighter.active_name:
    #                 return STATE_CLOSE_LIGHT_PUNCH
    #             return STATE_LIGHT_PUNCH
    #         elif current_state == STATE_CROUCH or current_state == STATE_CROUCH_LIGHT_PUNCH:
    #             if "crouch_light_punch" in fighter.active_name and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == True:
    #                 return STATE_CROUCH_WAIT
    #             return STATE_CROUCH_LIGHT_PUNCH
    #         elif current_state == STATE_JUMP or "STRAFE" in current_state or current_state == STATE_JUMP_LIGHT_PUNCH:
    #             return STATE_JUMP_LIGHT_PUNCH
    #         elif current_state == STATE_FORWARD_JUMP or current_state == STATE_DIAGONAL_JUMP_LIGHT_PUNCH:
    #             return STATE_DIAGONAL_JUMP_LIGHT_PUNCH
    #         elif current_state == STATE_WAIT:
    #             return STATE_WAIT
    #         elif current_state == STATE_CROUCH_WAIT:
    #             return STATE_CROUCH_WAIT
    #         else:
    #             return current_state
    #     elif keys[pg.K_KP5]:
    #         if current_state == STATE_IDLE or "WALK" in current_state or current_state == STATE_MEDIUM_PUNCH or current_state == STATE_CLOSE_MEDIUM_PUNCH:
    #             if "medium_punch" in fighter.active_name and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == True:
    #                 return STATE_WAIT
    #             if abs(fighter.opponent.pos.x - fighter.pos.x) <= 116 and "punch" not in fighter.active_name:
    #                 return STATE_CLOSE_MEDIUM_PUNCH
    #             return STATE_MEDIUM_PUNCH
    #         elif current_state == STATE_CROUCH or current_state == STATE_CROUCH_MEDIUM_PUNCH:
    #             if "crouch_medium_punch" in fighter.active_name and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == True:
    #                 return STATE_CROUCH_WAIT
    #             return STATE_CROUCH_MEDIUM_PUNCH
    #         elif current_state == STATE_JUMP or "STRAFE" in current_state or current_state == STATE_JUMP_MEDIUM_PUNCH:
    #             return STATE_JUMP_MEDIUM_PUNCH
    #         elif current_state == STATE_FORWARD_JUMP or current_state == STATE_DIAGONAL_JUMP_MEDIUM_PUNCH:
    #             return STATE_DIAGONAL_JUMP_MEDIUM_PUNCH
    #         elif current_state == STATE_WAIT:
    #             return STATE_WAIT  
    #         elif current_state == STATE_CROUCH_WAIT:
    #             return STATE_CROUCH_WAIT
    #         else:
    #             return current_state
    #     elif keys[pg.K_KP6]:
    #         if current_state == STATE_IDLE or "WALK" in current_state or current_state == STATE_HEAVY_PUNCH or current_state == STATE_CLOSE_HEAVY_PUNCH:
    #             if "heavy_punch" in fighter.active_name and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == True:
    #                 return STATE_WAIT
    #             if abs(fighter.opponent.pos.x - fighter.pos.x) <= 116 and "punch" not in fighter.active_name:
    #                 return STATE_CLOSE_HEAVY_PUNCH
    #             return STATE_HEAVY_PUNCH
    #         elif current_state == STATE_CROUCH or current_state == STATE_CROUCH_HEAVY_PUNCH:
    #             if "crouch_heavy_punch" in fighter.active_name and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == True:
    #                 return STATE_CROUCH_WAIT
    #             return STATE_CROUCH_HEAVY_PUNCH
    #         elif current_state == STATE_JUMP or "STRAFE" in current_state or current_state == STATE_JUMP_HEAVY_PUNCH:
    #             return STATE_JUMP_HEAVY_PUNCH
    #         elif current_state == STATE_FORWARD_JUMP or current_state == STATE_DIAGONAL_JUMP_HEAVY_PUNCH:
    #             return STATE_DIAGONAL_JUMP_HEAVY_PUNCH
    #         elif current_state == STATE_WAIT:
    #             return STATE_WAIT
    #         elif current_state == STATE_CROUCH_WAIT:
    #             return STATE_CROUCH_WAIT
    #         else:
    #             return current_state
    #     elif keys[pg.K_KP7]:
    #         if current_state == STATE_IDLE or "WALK" in current_state or current_state == STATE_LIGHT_KICK or current_state == STATE_CLOSE_LIGHT_KICK:
    #             if "light_kick" in fighter.active_name and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == True:
    #                 return STATE_WAIT
    #             if abs(fighter.opponent.pos.x - fighter.pos.x) <= 116 and "kick" not in fighter.active_name:
    #                 return STATE_CLOSE_LIGHT_KICK
    #             return STATE_LIGHT_KICK
    #         elif current_state == STATE_CROUCH or current_state == STATE_CROUCH_LIGHT_KICK:
    #             if "crouch_light_kick" in fighter.active_name and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == True:
    #                 return STATE_CROUCH_WAIT
    #             return STATE_CROUCH_LIGHT_KICK
    #         elif current_state == STATE_JUMP or "STRAFE" in current_state or current_state == STATE_JUMP_LIGHT_KICK:
    #             return STATE_JUMP_LIGHT_KICK
    #         elif current_state == STATE_FORWARD_JUMP or current_state == STATE_DIAGONAL_JUMP_LIGHT_KICK:
    #             return STATE_DIAGONAL_JUMP_LIGHT_KICK
    #         elif current_state == STATE_WAIT:
    #             return STATE_WAIT
    #         elif current_state == STATE_CROUCH_WAIT:
    #             return STATE_CROUCH_WAIT
    #         else:
    #             return current_state
    #     elif keys[pg.K_KP8]:
    #         if current_state == STATE_IDLE or "WALK" in current_state or current_state == STATE_MEDIUM_KICK or current_state == STATE_CLOSE_MEDIUM_KICK:
    #             if "medium_kick" in fighter.active_name and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == True:
    #                 return STATE_WAIT
    #             if abs(fighter.opponent.pos.x - fighter.pos.x) <= 116 and "kick" not in fighter.active_name:
    #                 return STATE_CLOSE_MEDIUM_KICK
    #             return STATE_MEDIUM_KICK
    #         elif current_state == STATE_CROUCH or current_state == STATE_CROUCH_MEDIUM_KICK:
    #             if "crouch_medium_kick" in fighter.active_name and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == True:
    #                 return STATE_CROUCH_WAIT
    #             return STATE_CROUCH_MEDIUM_KICK
    #         elif current_state == STATE_JUMP or "STRAFE" in current_state or current_state == STATE_JUMP_MEDIUM_KICK:
    #             return STATE_JUMP_MEDIUM_KICK
    #         elif current_state == STATE_FORWARD_JUMP or current_state == STATE_DIAGONAL_JUMP_MEDIUM_KICK:
    #             return STATE_DIAGONAL_JUMP_MEDIUM_KICK
    #         elif current_state == STATE_WAIT:
    #             return STATE_WAIT
    #         elif current_state == STATE_CROUCH_WAIT:
    #             return STATE_CROUCH_WAIT  
    #         else:
    #             return current_state
    #     elif keys[pg.K_KP9]:
    #         if current_state == STATE_IDLE or "WALK" in current_state or current_state == STATE_HEAVY_KICK or current_state == STATE_CLOSE_HEAVY_KICK:
    #             if "heavy_kick" in fighter.active_name and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == True:
    #                 return STATE_WAIT
    #             if abs(fighter.opponent.pos.x - fighter.pos.x) <= 116 and "kick" not in fighter.active_name:
    #                 return STATE_CLOSE_HEAVY_KICK
    #             return STATE_HEAVY_KICK
    #         elif current_state == STATE_CROUCH or current_state == STATE_CROUCH_HEAVY_KICK:
    #             if "crouch_heavy_kick" in fighter.active_name and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == True:
    #                 return STATE_CROUCH_WAIT
    #             return STATE_CROUCH_HEAVY_KICK
    #         elif current_state == STATE_JUMP or "STRAFE" in current_state or current_state == STATE_JUMP_HEAVY_KICK:
    #             return STATE_JUMP_HEAVY_KICK
    #         elif current_state == STATE_FORWARD_JUMP or current_state == STATE_DIAGONAL_JUMP_HEAVY_KICK:
    #             return STATE_DIAGONAL_JUMP_HEAVY_KICK
    #         elif current_state == STATE_WAIT:
    #             return STATE_WAIT
    #         elif current_state == STATE_CROUCH_WAIT:
    #             return STATE_CROUCH_WAIT
    #         else:
    #             return current_state
    #     elif keys[pg.K_LEFT]:
    #         if ("PUNCH" in current_state or "KICK" in current_state) and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == False:
    #             return current_state
    #         if direction == "left":
    #             if fighter.active_name == "jumpR" and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == False:
    #                 return STATE_FORWARD_STRAFE
    #             elif keys[pg.K_KP0]:
    #                 return STATE_FORWARD_JUMP
    #             elif current_state == STATE_FORWARD_JUMP:
    #                 return current_state
    #             return STATE_WALK
    #         else:
    #             if fighter.active_name == "jump" and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == False:
    #                 return STATE_BACKWARD_STRAFE
    #             elif keys[pg.K_KP0]:
    #                 return STATE_BACKWARD_JUMP
    #             elif current_state == STATE_BACKWARD_JUMP:
    #                 return current_state
    #             return STATE_BACKWALK
    #     elif keys[pg.K_RIGHT]:
    #         if ("PUNCH" in current_state or "KICK" in current_state) and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == False:
    #             return current_state
    #         if direction == "left":
    #             if fighter.active_name == "jumpR" and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == False:
    #                 return STATE_BACKWARD_STRAFE
    #             elif keys[pg.K_KP0]:
    #                 return STATE_BACKWARD_JUMP
    #             elif current_state == STATE_BACKWARD_JUMP:
    #                 return current_state
    #             return STATE_BACKWALK
    #         else:
    #             if fighter.active_name == "jump" and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == False:
    #                 return STATE_FORWARD_STRAFE
    #             elif keys[pg.K_KP0]:
    #                 return STATE_FORWARD_JUMP
    #             elif current_state == STATE_FORWARD_JUMP:
    #                 return current_state
    #             return STATE_WALK
    #     elif keys[pg.K_DOWN]:
    #         if ("PUNCH" in current_state or "KICK" in current_state) and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == False:
    #             return current_state
    #         return STATE_CROUCH
    #     elif keys[pg.K_KP0]:
    #         if ("PUNCH" in current_state or "KICK" in current_state) and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == False:
    #             return current_state
    #         elif current_state == STATE_FORWARD_JUMP or current_state == STATE_BACKWARD_JUMP:
    #             return current_state
    #         return STATE_JUMP
    #     elif "WALK" not in current_state and current_state is not STATE_CROUCH and STATE_WAIT not in current_state:
    #         return current_state
    #     return STATE_IDLE



def update_state(fighter, keys, direction, playerNum, current_state = STATE_IDLE, mode="localLaptop"):
    right = keys[pg.K_d]
    left = keys[pg.K_a]
    down = keys[pg.K_s]
    jump = keys[pg.K_SPACE]
    lightPunch = keys[pg.K_h]
    mediumPunch = keys[pg.K_j]
    heavyPunch = keys[pg.K_k]
    lightKick = keys[pg.K_y]
    mediumKick = keys[pg.K_u]
    heavyKick = keys[pg.K_i]
    if "local" in mode:
        if playerNum == "player1":
            if "Laptop" in mode:
                lightPunch = keys[pg.K_f]
                mediumPunch = keys[pg.K_g]
                heavyPunch = keys[pg.K_h]
                lightKick = keys[pg.K_r]
                mediumKick = keys[pg.K_t]
                heavyKick = keys[pg.K_y]
            else:
                lightPunch = keys[pg.K_g]
                mediumPunch = keys[pg.K_h]
                heavyPunch = keys[pg.K_j]
                lightKick = keys[pg.K_t]
                mediumKick = keys[pg.K_y]
                heavyKick = keys[pg.K_u]
        else:
            if "Laptop" in mode:
                right = keys[pg.K_RIGHT]
                left = keys[pg.K_LEFT]
                down = keys[pg.K_DOWN]
                jump = keys[pg.K_RCTRL]
                lightPunch = keys[pg.K_l]
                mediumPunch = keys[pg.K_k]
                heavyPunch = keys[pg.K_j]
                lightKick = keys[pg.K_o]
                mediumKick = keys[pg.K_i]
                heavyKick = keys[pg.K_u]
            else:
                right = keys[pg.K_RIGHT]
                left = keys[pg.K_LEFT]
                down = keys[pg.K_DOWN]
                jump = keys[pg.K_KP0]
                lightPunch = keys[pg.K_KP4]
                mediumPunch = keys[pg.K_KP5]
                heavyPunch = keys[pg.K_KP6]
                lightKick = keys[pg.K_KP7]
                mediumKick = keys[pg.K_KP8]
                heavyKick = keys[pg.K_KP9]
    if "HURT" in current_state:
        return current_state
    if lightPunch:
        if current_state == STATE_IDLE or "WALK" in current_state or current_state == STATE_LIGHT_PUNCH or current_state == STATE_CLOSE_LIGHT_PUNCH:
            if "light_punch" in fighter.active_name and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == True:
                return STATE_WAIT
            if abs(fighter.opponent.pos.x - fighter.pos.x) <= 116 and "punch" not in fighter.active_name:
                return STATE_CLOSE_LIGHT_PUNCH
            return STATE_LIGHT_PUNCH
        elif current_state == STATE_CROUCH or current_state == STATE_CROUCH_LIGHT_PUNCH:
            if "crouch_light_punch" in fighter.active_name and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == True:
                return STATE_CROUCH_WAIT
            return STATE_CROUCH_LIGHT_PUNCH
        elif current_state == STATE_JUMP or "STRAFE" in current_state or current_state == STATE_JUMP_LIGHT_PUNCH:
            return STATE_JUMP_LIGHT_PUNCH
        elif current_state == STATE_FORWARD_JUMP or current_state == STATE_DIAGONAL_JUMP_LIGHT_PUNCH:
            return STATE_DIAGONAL_JUMP_LIGHT_PUNCH
        elif current_state == STATE_WAIT:
            return STATE_WAIT
        elif current_state == STATE_CROUCH_WAIT:
            return STATE_CROUCH_WAIT
        else:
            return current_state
    elif mediumPunch:
        if current_state == STATE_IDLE or "WALK" in current_state or current_state == STATE_MEDIUM_PUNCH or current_state == STATE_CLOSE_MEDIUM_PUNCH:
            if "medium_punch" in fighter.active_name and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == True:
                return STATE_WAIT
            if abs(fighter.opponent.pos.x - fighter.pos.x) <= 116 and "punch" not in fighter.active_name:
                return STATE_CLOSE_MEDIUM_PUNCH
            return STATE_MEDIUM_PUNCH
        elif current_state == STATE_CROUCH or current_state == STATE_CROUCH_MEDIUM_PUNCH:
            if "crouch_medium_punch" in fighter.active_name and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == True:
                return STATE_CROUCH_WAIT
            return STATE_CROUCH_MEDIUM_PUNCH
        elif current_state == STATE_JUMP or "STRAFE" in current_state or current_state == STATE_JUMP_MEDIUM_PUNCH:
            return STATE_JUMP_MEDIUM_PUNCH
        elif current_state == STATE_FORWARD_JUMP or current_state == STATE_DIAGONAL_JUMP_MEDIUM_PUNCH:
            return STATE_DIAGONAL_JUMP_MEDIUM_PUNCH
        elif current_state == STATE_WAIT:
            return STATE_WAIT  
        elif current_state == STATE_CROUCH_WAIT:
            return STATE_CROUCH_WAIT
        else:
            return current_state
    elif heavyPunch:
        if current_state == STATE_IDLE or "WALK" in current_state or current_state == STATE_HEAVY_PUNCH or current_state == STATE_CLOSE_HEAVY_PUNCH:
            if "heavy_punch" in fighter.active_name and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == True:
                return STATE_WAIT
            if abs(fighter.opponent.pos.x - fighter.pos.x) <= 116 and "punch" not in fighter.active_name:
                return STATE_CLOSE_HEAVY_PUNCH
            return STATE_HEAVY_PUNCH
        elif current_state == STATE_CROUCH or current_state == STATE_CROUCH_HEAVY_PUNCH:
            if "crouch_heavy_punch" in fighter.active_name and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == True:
                return STATE_CROUCH_WAIT
            return STATE_CROUCH_HEAVY_PUNCH
        elif current_state == STATE_JUMP or "STRAFE" in current_state or current_state == STATE_JUMP_HEAVY_PUNCH:
            return STATE_JUMP_HEAVY_PUNCH
        elif current_state == STATE_FORWARD_JUMP or current_state == STATE_DIAGONAL_JUMP_HEAVY_PUNCH:
            return STATE_DIAGONAL_JUMP_HEAVY_PUNCH
        elif current_state == STATE_WAIT:
            return STATE_WAIT
        elif current_state == STATE_CROUCH_WAIT:
            return STATE_CROUCH_WAIT
        else:
            return current_state
    elif lightKick:
        if current_state == STATE_IDLE or "WALK" in current_state or current_state == STATE_LIGHT_KICK or current_state == STATE_CLOSE_LIGHT_KICK:
            if "light_kick" in fighter.active_name and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == True:
                return STATE_WAIT
            if abs(fighter.opponent.pos.x - fighter.pos.x) <= 116 and "kick" not in fighter.active_name:
                return STATE_CLOSE_LIGHT_KICK
            return STATE_LIGHT_KICK
        elif current_state == STATE_CROUCH or current_state == STATE_CROUCH_LIGHT_KICK:
            if "crouch_light_kick" in fighter.active_name and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == True:
                return STATE_CROUCH_WAIT
            return STATE_CROUCH_LIGHT_KICK
        elif current_state == STATE_JUMP or "STRAFE" in current_state or current_state == STATE_JUMP_LIGHT_KICK:
            return STATE_JUMP_LIGHT_KICK
        elif current_state == STATE_FORWARD_JUMP or current_state == STATE_DIAGONAL_JUMP_LIGHT_KICK:
            return STATE_DIAGONAL_JUMP_LIGHT_KICK
        elif current_state == STATE_WAIT:
            return STATE_WAIT
        elif current_state == STATE_CROUCH_WAIT:
            return STATE_CROUCH_WAIT
        else:
            return current_state
    elif mediumKick:
        if current_state == STATE_IDLE or "WALK" in current_state or current_state == STATE_MEDIUM_KICK or current_state == STATE_CLOSE_MEDIUM_KICK:
            if "medium_kick" in fighter.active_name and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == True:
                return STATE_WAIT
            if abs(fighter.opponent.pos.x - fighter.pos.x) <= 116 and "kick" not in fighter.active_name:
                return STATE_CLOSE_MEDIUM_KICK
            return STATE_MEDIUM_KICK
        elif current_state == STATE_CROUCH or current_state == STATE_CROUCH_MEDIUM_KICK:
            if "crouch_medium_kick" in fighter.active_name and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == True:
                return STATE_CROUCH_WAIT
            return STATE_CROUCH_MEDIUM_KICK
        elif current_state == STATE_JUMP or "STRAFE" in current_state or current_state == STATE_JUMP_MEDIUM_KICK:
            return STATE_JUMP_MEDIUM_KICK
        elif current_state == STATE_FORWARD_JUMP or current_state == STATE_DIAGONAL_JUMP_MEDIUM_KICK:
            return STATE_DIAGONAL_JUMP_MEDIUM_KICK
        elif current_state == STATE_WAIT:
            return STATE_WAIT
        elif current_state == STATE_CROUCH_WAIT:
            return STATE_CROUCH_WAIT  
        else:
            return current_state
    elif heavyKick:
        if current_state == STATE_IDLE or "WALK" in current_state or current_state == STATE_HEAVY_KICK or current_state == STATE_CLOSE_HEAVY_KICK:
            if "heavy_kick" in fighter.active_name and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == True:
                return STATE_WAIT
            if abs(fighter.opponent.pos.x - fighter.pos.x) <= 116 and "kick" not in fighter.active_name:
                return STATE_CLOSE_HEAVY_KICK
            return STATE_HEAVY_KICK
        elif current_state == STATE_CROUCH or current_state == STATE_CROUCH_HEAVY_KICK:
            if "crouch_heavy_kick" in fighter.active_name and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == True:
                return STATE_CROUCH_WAIT
            return STATE_CROUCH_HEAVY_KICK
        elif current_state == STATE_JUMP or "STRAFE" in current_state or current_state == STATE_JUMP_HEAVY_KICK:
            return STATE_JUMP_HEAVY_KICK
        elif current_state == STATE_FORWARD_JUMP or current_state == STATE_DIAGONAL_JUMP_HEAVY_KICK:
            return STATE_DIAGONAL_JUMP_HEAVY_KICK
        elif current_state == STATE_WAIT:
            return STATE_WAIT
        elif current_state == STATE_CROUCH_WAIT:
            return STATE_CROUCH_WAIT
        else:
            return current_state
    elif right:
        if ("PUNCH" in current_state or "KICK" in current_state) and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == False:
            return current_state
        if direction == "right":
            if fighter.active_name == "jump" and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == False:
                return STATE_FORWARD_STRAFE
            elif jump:
                return STATE_FORWARD_JUMP
            elif current_state == STATE_FORWARD_JUMP:
                return current_state
            return STATE_WALK
        else:
            if fighter.active_name == "jumpR" and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == False:
                return STATE_BACKWARD_STRAFE
            elif jump:
                return STATE_BACKWARD_JUMP
            elif current_state == STATE_BACKWARD_JUMP:
                return current_state
            return STATE_BACKWALK
    elif left:
        if ("PUNCH" in current_state or "KICK" in current_state) and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == False:
            return current_state
        if direction == "right":
            if fighter.active_name == "jump" and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == False:
                return STATE_BACKWARD_STRAFE
            elif jump:
                return STATE_BACKWARD_JUMP
            elif current_state == STATE_BACKWARD_JUMP:
                return current_state
            return STATE_BACKWALK
        else:
            if fighter.active_name == "jumpR" and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == False:
                return STATE_FORWARD_STRAFE
            elif jump:
                return STATE_FORWARD_JUMP
            elif current_state == STATE_FORWARD_JUMP:
                return current_state
            return STATE_WALK
    elif down:
        if ("PUNCH" in current_state or "KICK" in current_state) and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == False:
            return current_state
        return STATE_CROUCH
    elif jump:
        if ("PUNCH" in current_state or "KICK" in current_state) and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == False:
            return current_state
        elif current_state == STATE_FORWARD_JUMP or current_state == STATE_BACKWARD_JUMP:
            return current_state
        return STATE_JUMP
    
    elif "WALK" not in current_state and current_state is not STATE_CROUCH and STATE_WAIT not in current_state:
        return current_state
    return STATE_IDLE

    
    
def state_idle(fighter, state):
    if state == STATE_IDLE and fighter.pos.y == STAGE_FLOOR:
            fighter.vel = vec(0, 0)
            if fighter.direction == "right":
                fighter.set_active_animation("idle")
            else:
                fighter.set_active_animation("idleR")
                
def state_wait(fighter,state):
    if state == STATE_WAIT and fighter.pos.y == STAGE_FLOOR:
        if fighter.direction == "right":
            fighter.set_active_animation("idle")
        else:
            fighter.set_active_animation("idleR")
    elif state == STATE_CROUCH_WAIT and fighter.pos.y == STAGE_FLOOR:
        if fighter.direction == "right":
            fighter.set_active_animation("crouch")
        else:
            fighter.set_active_animation("crouchR")
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
    if "jump" in fighter.active_name and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == True:
        fighter.state = STATE_IDLE
        if fighter.direction == "right":
            fighter.set_active_animation("idle")
        else:
            fighter.set_active_animation("idleR")
        return
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
    if "jump" in fighter.active_name and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == True and fighter.pos.y == STAGE_FLOOR:
        fighter.state = STATE_IDLE
        if fighter.direction == "right":
            fighter.set_active_animation("idle")
        else:
            fighter.set_active_animation("idleR")
        return
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

def state_hurt(fighter, state):
    if "hurt" in fighter.active_name and "crouch" not in fighter.active_name and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == True:
        if fighter.direction == "right":
            fighter.set_active_animation("idle")
        else:
            fighter.set_active_animation("idleR")
        fighter.state = STATE_IDLE
        return
    
    if "hurt" in fighter.active_name and "crouch" in fighter.active_name and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == True:
        if fighter.direction == "right":
            fighter.set_active_animation("crouch")
        else:
            fighter.set_active_animation("crouchR")
        fighter.state = STATE_CROUCH
        return
    
    if "HURT" in state and fighter.pos.y == STAGE_FLOOR:
        if "LIGHT" in state:
            velx = 4
        elif "MEDIUM" in state:
            velx = 6
        elif "HEAVY" in state:
            velx = 8
            
        friction = 0.5
        
        if fighter.direction == "right":
            fighter.vel.x = -velx
        else:
            fighter.vel.x = velx
        
         # Apply friction to the sliding motion
        if fighter.vel.x > 0:  # If moving right (positive velocity), apply friction to slow down
            fighter.vel.x -= friction
            if fighter.vel.x < 0:  # Clamp the velocity to prevent overshooting
                fighter.vel.x = 0
        elif fighter.vel.x < 0:  # If moving left (negative velocity), apply friction to slow down
            fighter.vel.x += friction
            if fighter.vel.x > 0:  # Clamp the velocity to prevent overshooting
                fighter.vel.x = 0
  
def state_punch(fighter,state):
    if "punch" in fighter.active_name and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == True and fighter.pos.y == STAGE_FLOOR:
        if "crouch" in fighter.active_name:
            fighter.state = STATE_CROUCH
            if fighter.direction == "right":
                fighter.set_active_animation("crouch")
            else:
                fighter.set_active_animation("crouchR")
        else:
            fighter.state = STATE_IDLE
            if fighter.direction == "right":
                fighter.set_active_animation("idle")
            else:
                fighter.set_active_animation("idleR")
        return

    if state == STATE_LIGHT_PUNCH and fighter.pos.y == STAGE_FLOOR and "light_punch" not in fighter.active_name:
        fighter.vel = vec(0, 0)
        if fighter.direction == "right":
            fighter.set_active_animation("light_punch")
        else:
            fighter.set_active_animation("light_punchR")
    elif state == STATE_MEDIUM_PUNCH and fighter.pos.y == STAGE_FLOOR and "medium_punch" not in fighter.active_name:
        fighter.vel = vec(0, 0)
        if fighter.direction == "right":
            fighter.set_active_animation("medium_punch")
        else:
            fighter.set_active_animation("medium_punchR")
    elif state == STATE_HEAVY_PUNCH and fighter.pos.y == STAGE_FLOOR and "heavy_punch" not in fighter.active_name:
        fighter.vel = vec(0, 0)
        if fighter.direction == "right":
            fighter.set_active_animation("heavy_punch")
        else:
            fighter.set_active_animation("heavy_punchR")
    elif state == STATE_CLOSE_LIGHT_PUNCH and fighter.pos.y == STAGE_FLOOR and "close_light_punch" not in fighter.active_name:
        fighter.vel = vec(0, 0)
        if fighter.direction == "right":
            fighter.set_active_animation("close_light_punch")
        else:
            fighter.set_active_animation("close_light_punchR")
    elif state == STATE_CLOSE_MEDIUM_PUNCH and fighter.pos.y == STAGE_FLOOR and "close_medium_punch" not in fighter.active_name:
        fighter.vel = vec(0, 0)
        if fighter.direction == "right":
            fighter.set_active_animation("close_medium_punch")
        else:
            fighter.set_active_animation("close_medium_punchR")
    elif state == STATE_CLOSE_HEAVY_PUNCH and fighter.pos.y == STAGE_FLOOR and "close_heavy_punch" not in fighter.active_name:
        fighter.vel = vec(0, 0)
        if fighter.direction == "right":
            fighter.set_active_animation("close_heavy_punch")
        else:
            fighter.set_active_animation("close_heavy_punchR")
    elif state == STATE_CROUCH_LIGHT_PUNCH and fighter.pos.y == STAGE_FLOOR and "crouch_light_punch" not in fighter.active_name:
        fighter.vel = vec(0, 0)
        if fighter.direction == "right":
            fighter.set_active_animation("crouch_light_punch")
        else:
            fighter.set_active_animation("crouch_light_punchR")
    elif state == STATE_CROUCH_MEDIUM_PUNCH and fighter.pos.y == STAGE_FLOOR and "crouch_medium_punch" not in fighter.active_name:
        fighter.vel = vec(0, 0)
        if fighter.direction == "right":
            fighter.set_active_animation("crouch_medium_punch")
        else:
            fighter.set_active_animation("crouch_medium_punchR")    
    elif state == STATE_CROUCH_HEAVY_PUNCH and fighter.pos.y == STAGE_FLOOR and "crouch_heavy_punch" not in fighter.active_name:
        fighter.vel = vec(0, 0)
        if fighter.direction == "right":
            fighter.set_active_animation("crouch_heavy_punch")
        else:
            fighter.set_active_animation("crouch_heavy_punchR")
    elif state == STATE_JUMP_LIGHT_PUNCH and fighter.pos.y <= 600 and "punch" not in fighter.active_name and "kick" not in fighter.active_name:
        if fighter.direction == "right":
            fighter.set_active_animation("jump_light_punch")
        else:
            fighter.set_active_animation("jump_light_punchR")
    elif state == STATE_JUMP_MEDIUM_PUNCH and fighter.pos.y <= 600 and "punch" not in fighter.active_name and "kick" not in fighter.active_name:
        if fighter.direction == "right":
            fighter.set_active_animation("jump_medium_punch")
        else:
            fighter.set_active_animation("jump_medium_punchR")
    elif state == STATE_JUMP_HEAVY_PUNCH and fighter.pos.y <= 600 and "punch" not in fighter.active_name and "kick" not in fighter.active_name:
        if fighter.direction == "right":
            fighter.set_active_animation("jump_heavy_punch")
        else:
            fighter.set_active_animation("jump_heavy_punchR")
    elif state == STATE_DIAGONAL_JUMP_LIGHT_PUNCH and fighter.pos.y <= 600 and "forward_jump" in fighter.active_name:
        if fighter.direction == "right":
            fighter.set_active_animation("diagonal_jump_light_punch")
        else:
            fighter.set_active_animation("diagonal_jump_light_punchR")
    elif state == STATE_DIAGONAL_JUMP_MEDIUM_PUNCH and fighter.pos.y <= 600 and "forward_jump" in fighter.active_name:
        if fighter.direction == "right":
            fighter.set_active_animation("diagonal_jump_medium_punch")
        else:
            fighter.set_active_animation("diagonal_jump_medium_punchR")
    elif state == STATE_DIAGONAL_JUMP_HEAVY_PUNCH and fighter.pos.y <= 600 and "forward_jump" in fighter.active_name:
        if fighter.direction == "right":
            fighter.set_active_animation("diagonal_jump_heavy_punch")
        else:
            fighter.set_active_animation("diagonal_jump_heavy_punchR")
def state_kick(fighter,state):
    if "kick" in fighter.active_name and fighter.active_anim.is_animation_finished(fighter.elapsed_time) == True and fighter.pos.y == STAGE_FLOOR:
        if "crouch" in fighter.active_name:
            fighter.state = STATE_CROUCH
            if fighter.direction == "right":
                fighter.set_active_animation("crouch")
            else:
                fighter.set_active_animation("crouchR")
        else:
            fighter.state = STATE_IDLE
            if fighter.direction == "right":
                fighter.set_active_animation("idle")
            else:
                fighter.set_active_animation("idleR")
        return
    if state == STATE_LIGHT_KICK and fighter.pos.y == STAGE_FLOOR and "light_kick" not in fighter.active_name:
        fighter.vel = vec(0, 0)
        if fighter.direction == "right":
            fighter.set_active_animation("light_kick")
        else:
            fighter.set_active_animation("light_kickR")
    elif state == STATE_MEDIUM_KICK and fighter.pos.y == STAGE_FLOOR and "medium_kick" not in fighter.active_name:
        fighter.vel = vec(0, 0)
        if fighter.direction == "right":
            fighter.set_active_animation("medium_kick")
        else:
            fighter.set_active_animation("medium_kickR")
    elif state == STATE_HEAVY_KICK and fighter.pos.y == STAGE_FLOOR and "heavy_kick" not in fighter.active_name:
        fighter.vel = vec(0, 0)
        if fighter.direction == "right":
            fighter.set_active_animation("heavy_kick")
        else:
            fighter.set_active_animation("heavy_kickR")
    elif state == STATE_CLOSE_LIGHT_KICK and fighter.pos.y == STAGE_FLOOR and "close_light_kick" not in fighter.active_name:
        fighter.vel = vec(0, 0)
        if fighter.direction == "right":
            fighter.set_active_animation("close_light_kick")
        else:
            fighter.set_active_animation("close_light_kickR")
    elif state == STATE_CLOSE_MEDIUM_KICK and fighter.pos.y == STAGE_FLOOR and "close_medium_kick" not in fighter.active_name:
        fighter.vel = vec(0, 0)
        if fighter.direction == "right":
            fighter.set_active_animation("close_medium_kick")
        else:
            fighter.set_active_animation("close_medium_kickR")
    elif state == STATE_CLOSE_HEAVY_KICK and fighter.pos.y == STAGE_FLOOR and "close_heavy_kick" not in fighter.active_name:
        fighter.vel = vec(0, 0)
        if fighter.direction == "right":
            fighter.set_active_animation("close_heavy_kick")
        else:
            fighter.set_active_animation("close_heavy_kickR")
    elif state == STATE_CROUCH_LIGHT_KICK and fighter.pos.y == STAGE_FLOOR and "crouch_light_kick" not in fighter.active_name:
        fighter.vel = vec(0, 0)
        if fighter.direction == "right":
            fighter.set_active_animation("crouch_light_kick")
        else:
            fighter.set_active_animation("crouch_light_kickR")
    elif state == STATE_CROUCH_MEDIUM_KICK and fighter.pos.y == STAGE_FLOOR and "crouch_medium_kick" not in fighter.active_name:
        fighter.vel = vec(0, 0)
        if fighter.direction == "right":
            fighter.set_active_animation("crouch_medium_kick")
        else:
            fighter.set_active_animation("crouch_medium_kickR")    
    elif state == STATE_CROUCH_HEAVY_KICK and fighter.pos.y == STAGE_FLOOR and "crouch_heavy_kick" not in fighter.active_name:
        fighter.vel = vec(0, 0)
        if fighter.direction == "right":
            fighter.set_active_animation("crouch_heavy_kick")
        else:
            fighter.set_active_animation("crouch_heavy_kickR")   
    elif state == STATE_JUMP_LIGHT_KICK and fighter.pos.y <= 550 and "punch" not in fighter.active_name and "kick" not in fighter.active_name:
        if fighter.direction == "right":
            fighter.set_active_animation("jump_light_kick")
        else:
            fighter.set_active_animation("jump_light_kickR")
    elif state == STATE_JUMP_MEDIUM_KICK and fighter.pos.y <= 550 and "punch" not in fighter.active_name and "kick" not in fighter.active_name:
        if fighter.direction == "right":
            fighter.set_active_animation("jump_medium_kick")
        else:
            fighter.set_active_animation("jump_medium_kickR")
    elif state == STATE_JUMP_HEAVY_KICK and fighter.pos.y <= 550 and "punch" not in fighter.active_name and "kick" not in fighter.active_name:
        if fighter.direction == "right":
            fighter.set_active_animation("jump_heavy_kick")
        else:
            fighter.set_active_animation("jump_heavy_kickR")
    elif state == STATE_DIAGONAL_JUMP_LIGHT_KICK:
        if fighter.pos.y <= 550 and "forward_jump" in fighter.active_name:
            if fighter.direction == "right":
                fighter.set_active_animation("diagonal_jump_light_kick")
            else:
                fighter.set_active_animation("diagonal_jump_light_kickR")
        elif fighter.pos.y == STAGE_FLOOR:
            fighter.vel = vec(0, 0)
            fighter.state = STATE_IDLE
            if fighter.direction == "right":
                fighter.set_active_animation("idle")
            else:
                fighter.set_active_animation("idleR")
    elif state == STATE_DIAGONAL_JUMP_MEDIUM_KICK:
        if fighter.pos.y <= 420 and "forward_jump" in fighter.active_name:
            if fighter.direction == "right":
                fighter.set_active_animation("diagonal_jump_medium_kick")
            else:
                fighter.set_active_animation("diagonal_jump_medium_kickR")
        elif fighter.pos.y == STAGE_FLOOR:
            fighter.vel = vec(0, 0)
            fighter.state = STATE_IDLE
            if fighter.direction == "right":
                fighter.set_active_animation("idle")
            else:
                fighter.set_active_animation("idleR")
    elif state == STATE_DIAGONAL_JUMP_HEAVY_KICK:
        if fighter.pos.y <= 420 and "forward_jump" in fighter.active_name:
            if fighter.direction == "right":
                fighter.set_active_animation("diagonal_jump_heavy_kick")
            else:
                fighter.set_active_animation("diagonal_jump_heavy_kickR")
        elif fighter.pos.y == STAGE_FLOOR:
            fighter.vel = vec(0, 0)
            fighter.state = STATE_IDLE
            if fighter.direction == "right":
                fighter.set_active_animation("idle")
            else:
                fighter.set_active_animation("idleR")