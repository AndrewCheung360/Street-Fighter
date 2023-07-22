import pygame as pg
from settings import *
from spritesheet import SpriteSheet, Animation
from animatedsprite import AnimatedSprite

vec = pg.math.Vector2

class Fighter(AnimatedSprite):
    def __init__(self, mode, playerNum, name, sheet, bg, x, y, idleFrames, walkFrames, jumpFrames, direction, *groups):
        super().__init__(*groups)
        
        self.mode = mode
        self.playerNum = playerNum
        self.name = name
        self.sheet = sheet
        self.idleFrames = idleFrames
        self.walkFrames = walkFrames
        self.jumpFrames = jumpFrames
        self.bg = bg
        self.direction = direction
        self.load()
        
        self.image = self.active_anim.get_frame(0)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
  
        self.pos = vec(x, y)
        self.vel = vec(0, 0)
        self.acceleration = 1.0  # Adjust the acceleration value as needed
        self.friction = 0.2  # Adjust the friction value as needed
        self.idle_threshold = 0.05  # Adjust the idle detection threshold as needed
        self.jump_speed = -27.0  # Adjust the jump speed as needed
        self.gravity = 1.0  # Adjust the gravity value as needed
        
    def load(self):
        spritesheet = SpriteSheet(self.sheet, self.bg)
        
        #idle animation
        idle_animation = spritesheet.get_animation(self.idleFrames, 0.15, Animation.PlayMode.LOOP, 4)
        self.store_animation("idle", idle_animation)
        idle_animationR = spritesheet.get_animation(self.idleFrames, 0.15, Animation.PlayMode.LOOP, 4, True)
        self.store_animation("idleR", idle_animationR)
        
        #walk animation
        walk_animation = spritesheet.get_animation(self.walkFrames, 0.1, Animation.PlayMode.LOOP, 4)
        self.store_animation("walk", walk_animation)
        walk_animationR = spritesheet.get_animation(self.walkFrames, 0.1, Animation.PlayMode.LOOP, 4, True)
        self.store_animation("walkR", walk_animationR)
        
        #backwalk animation
        backwalk = list(self.walkFrames)  # Create a copy of the array
        backwalk.reverse()  # Reverse the copy
        backwalk_animation = spritesheet.get_animation(backwalk, 0.1, Animation.PlayMode.LOOP, 4)
        self.store_animation("backwalk", backwalk_animation)
        backwalk_animationR = spritesheet.get_animation(backwalk, 0.1, Animation.PlayMode.LOOP, 4, True)
        self.store_animation("backwalkR", backwalk_animationR)
        
        #jump animation
        jump_animation = spritesheet.get_animation(self.jumpFrames, 0.12, Animation.PlayMode.NORMAL, 4)
        self.store_animation("jump", jump_animation)
        jump_animationR = spritesheet.get_animation(self.jumpFrames, 0.12, Animation.PlayMode.NORMAL, 4, True)
        self.store_animation("jumpR", jump_animationR)
        
    def handle_x_movement(self, keys):
        if (self.mode == "local" and self.playerNum == "player1") or self.mode == "multi":
            if keys[pg.K_d]:
                # Accelerate to the right
                self.vel.x += self.acceleration
            elif keys[pg.K_a]:
                # Accelerate to the left
                self.vel.x -= self.acceleration
            else:
                # Apply friction to slow down horizontally
                self.vel.x *= (1 - self.friction)
        elif self.mode == "local" and self.playerNum == "player2":
            if keys[pg.K_RIGHT]:
                # Accelerate to the right
                self.vel.x += self.acceleration
            elif keys[pg.K_LEFT]:
                # Accelerate to the left
                self.vel.x -= self.acceleration
            else:
                # Apply friction to slow down horizontally
                self.vel.x *= (1 - self.friction)
        # Limit maximum velocity to avoid overly fast movement
        max_velocity = 6
        self.vel.x = max(-max_velocity, min(self.vel.x, max_velocity))

        # Apply a small threshold for idle detection
        if abs(self.vel.x) < self.idle_threshold:
            self.vel.x = 0.0 
    
    def handle_jump(self, keys):
        if (self.mode == "local" and self.playerNum == "player1") or self.mode == "multi":
            if keys[pg.K_SPACE] and self.pos.y == STAGE_FLOOR:
                # Jump
                self.vel.y = self.jump_speed
                if self.direction == "right":
                    self.set_active_animation("jump")
                else:
                    self.set_active_animation("jumpR")  # Set the jump animation
        elif self.mode == "local" and self.playerNum == "player2":
            if keys[pg.K_KP0] and self.pos.y == STAGE_FLOOR:
                # Jump
                self.vel.y = self.jump_speed
                if self.direction == "right":
                    self.set_active_animation("jump")
                else:
                    self.set_active_animation("jumpR")  # Set the jump animation
    def apply_gravity(self):
        if not self.pos.y == STAGE_FLOOR:
            self.vel.y += self.gravity
            max_fall_speed = 20  # Adjust the maximum fall speed as needed
            self.vel.y = min(self.vel.y, max_fall_speed)    
    def get_keys(self):
        keys = pg.key.get_pressed()
        self.handle_x_movement(keys)
        self.handle_jump(keys)
        
    def flipDirection(self):
        if self.direction == "right":
            self.direction = "left"
        else:
            self.direction = "right"
            
    def handle_movement_animation(self):
        if abs(self.vel.x) > 0.05:
            # Character is moving, play the walking or backwards walking animation
            if self.vel.x > 0:
                if self.direction == "right":
                    self.set_active_animation("walk")
                else:
                    self.set_active_animation("backwalkR")
            else:
                if self.direction == "right":
                    self.set_active_animation("backwalk")
                else:
                    self.set_active_animation("walkR")
        else:
            # Character is not moving horizontally, play the idle animation
            if self.direction == "right":
                if self.vel.y == 0:
                    self.set_active_animation("idle")
            else:
                if self.vel.y == 0:
                    self.set_active_animation("idleR")
        
    
            
    def animate(self):
        self.handle_movement_animation()

        bottom = self.rect.bottom
        self.image = self.active_anim.get_frame(self.elapsed_time)
        self.rect = self.image.get_rect()
        self.rect.bottom = bottom

    def update(self):
        super().update(1/FPS)
        self.animate()
        self.get_keys()
        self.pos += self.vel
        
        # Apply gravity
        self.apply_gravity()

        # Check for collision with the stage floor
        if self.pos.y >= STAGE_FLOOR:
            self.pos.y = STAGE_FLOOR
            self.vel.y = 0
            
        # Update the sprite's rect position
        self.rect.midbottom = self.pos
