import pygame as pg
from settings import *
from spritesheet import SpriteSheet, Animation
from animatedsprite import AnimatedSprite
from characters.MoveStates import *

vec = pg.math.Vector2

class Fighter(AnimatedSprite):
    def __init__(self, mode, playerNum, name, sheet, bg, x, y, idleFrames, walkFrames, jumpFrames, direction, *groups):
        super().__init__(*groups)
        
        self.mode = mode
        self.playerNum = playerNum
        self.name = name
        self.direction = direction
        
        #spritesheet
        self.sheet = sheet
        self.bg = bg
        
        #animation frames
        self.idleFrames = idleFrames
        self.walkFrames = walkFrames
        self.jumpFrames = jumpFrames
        
        #initial state
        self.state = STATE_IDLE
        
        #load animations during initialization
        self.load()
        
        #sprite image and animation
        self.image = self.active_anim.get_frame(0)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
  
        #movement and position
        self.pos = vec(x, y)
        self.vel = vec(0, 0)
        
    #store animations from spritesheet
    def load(self):
        spritesheet = SpriteSheet(self.sheet, self.bg)
        
        #idle animation
        idle_animation = spritesheet.get_animation(self.idleFrames[0], self.idleFrames[1], Animation.PlayMode.LOOP, 4)
        self.store_animation("idle", idle_animation)
        idle_animationR = spritesheet.get_animation(self.idleFrames[0], self.idleFrames[1], Animation.PlayMode.LOOP, 4, True)
        self.store_animation("idleR", idle_animationR)
        
        #walk animation
        walk_animation = spritesheet.get_animation(self.walkFrames[0], self.walkFrames[1], Animation.PlayMode.LOOP, 4)
        self.store_animation("walk", walk_animation)
        walk_animationR = spritesheet.get_animation(self.walkFrames[0], self.walkFrames[1], Animation.PlayMode.LOOP, 4, True)
        self.store_animation("walkR", walk_animationR)
        
        #backwalk animation
        backwalk = list(self.walkFrames[0])  # Create a copy of the array
        backwalk.reverse()  # Reverse the copy
        backwalk_animation = spritesheet.get_animation(backwalk, self.walkFrames[1], Animation.PlayMode.LOOP, 4)
        self.store_animation("backwalk", backwalk_animation)
        backwalk_animationR = spritesheet.get_animation(backwalk, self.walkFrames[1], Animation.PlayMode.LOOP, 4, True)
        self.store_animation("backwalkR", backwalk_animationR)
        
        #jump animation
        jump_animation = spritesheet.get_animation(self.jumpFrames[0], self.jumpFrames[1], Animation.PlayMode.NORMAL, 4)
        self.store_animation("jump", jump_animation)
        jump_animationR = spritesheet.get_animation(self.jumpFrames[0], self.jumpFrames[1], Animation.PlayMode.NORMAL, 4, True)
        self.store_animation("jumpR", jump_animationR)
     
    def flipDirection(self):
        if self.direction == "right":
            self.direction = "left"
        else:
            self.direction = "right"
                                
    def apply_gravity(self):
        if not self.pos.y == STAGE_FLOOR:
            self.vel.y += GRAVITY
            self.vel.y = min(self.vel.y, MAX_FALL_SPEED)  
    
    def handle_idle(self, state):
        if state == STATE_IDLE and self.pos.y == STAGE_FLOOR:
            self.vel = vec(0, 0)
            if self.direction == "right":
                self.set_active_animation("idle")
            else:
                self.set_active_animation("idleR")
    
    def handle_x_movement(self, state):    
        if state == STATE_WALK:
            if self.direction == "right":
                self.vel.x = min(self.vel.x + ACCELERATION, MAX_X_VELOCITY)
                self.set_active_animation("walk")
            else:
                self.vel.x = max(self.vel.x - ACCELERATION, -MAX_X_VELOCITY)
                self.set_active_animation("walkR")
        elif state == STATE_BACKWALK:
            if self.direction == "right":
                self.vel.x = max(self.vel.x - ACCELERATION, -MAX_X_VELOCITY)
                self.set_active_animation("backwalk")
            else:
                self.vel.x = min(self.vel.x + ACCELERATION, MAX_X_VELOCITY)
                self.set_active_animation("backwalkR")
            
        # self.pos.x += self.vel.x
    
    def handle_jump(self, state):
        if state == STATE_JUMP and self.pos.y == STAGE_FLOOR:
            if self.direction == "right":
                self.set_active_animation("jump")
            else:
                self.set_active_animation("jumpR")
            self.vel.y = JUMP_SPEED
            
            # self.pos.y += self.vel.y
    
    def handle_states(self):
        keys = pg.key.get_pressed()
        current_state = update_state(keys, self.direction, self.playerNum, self.state, self.mode)
        if current_state == STATE_IDLE:
            self.state = STATE_IDLE
            state_idle(self, self.state)
        elif current_state == STATE_WALK or current_state == STATE_BACKWALK:
            self.state = current_state
            state_walk(self, self.state)
        elif current_state == STATE_JUMP:
            self.state = STATE_JUMP
            state_jump(self, self.state)
            
    def animate(self):
        bottom = self.rect.bottom
        self.image = self.active_anim.get_frame(self.elapsed_time)
        self.rect = self.image.get_rect()
        self.rect.bottom = bottom

    def update(self):
        super().update(1/FPS)
        self.handle_states()
        self.animate()
        
        # apply gravity
        self.apply_gravity()
        
        # Update the sprite's position
        self.pos += self.vel

        # Check for collision with the stage floor
        if self.pos.y >= STAGE_FLOOR:
            self.pos.y = STAGE_FLOOR
            self.vel.y = 0
          
        # Update the sprite's rect position
        self.rect.midbottom = self.pos
