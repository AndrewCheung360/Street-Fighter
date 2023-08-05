import pygame as pg
from animatedsprite import AnimatedSprite
from spritesheet import SpriteSheet, Animation
from settings import *

vec = pg.math.Vector2

class HitSplash(AnimatedSprite):
    def __init__(self, x, y, playerNum, frames, *groups):
        super().__init__(*groups)
        self.sheet = SpriteSheet('assets/graphics/misc/hitEffects.png',"black")
        self.playerNum = playerNum
        self.pos = vec(x,y)
        self.frames = frames
        
        #load animations during initialization
        self.load()
        
        #sprite image and animation
        self.image = self.active_anim.get_frame(0)
        self.rect = self.image.get_rect()
        
    def load(self):
        #player 1
        splash_p1 = self.sheet.get_animation(self.frames["player1"][0], self.frames["player1"][1], Animation.PlayMode.NORMAL, 3.25)
        self.store_animation("splash_player1", splash_p1)
        #player2
        splash_p2 = self.sheet.get_animation(self.frames["player2"][0], self.frames["player2"][1], Animation.PlayMode.NORMAL, 3.25)
        self.store_animation("splash_player2", splash_p2)
        
    def animate(self):
        if self.active_anim.is_animation_finished(self.elapsed_time):
            self.kill()
            return
        self.set_active_animation("splash_" + self.playerNum)
        self.image = self.active_anim.get_frame(self.elapsed_time)
        self.rect = self.image.get_rect()
        
    def update(self):
        super().update(1/FPS)
        self.animate()
        self.rect.center = self.pos
        
class LightHitSplash(HitSplash):
    def __init__(self, x, y, playerNum, *groups):
        self.frames = {
            "player1" : ([(14, 16, 9, 10),(34,15,13,11),(55,15,13,11),(75,10,20,19)],[0.0667, 0.0333, 0.0333, 0.0667]),
            "player2" : ([(160, 16, 9, 10),(178,15,13,11),(199,15,13,11),(219,10,20,19)],[0.0667, 0.0333, 0.0333, 0.0667]),
        }
        super().__init__(x, y, playerNum, self.frames, *groups)
        
class MediumHitSplash(HitSplash):
    def __init__(self, x, y, playerNum, *groups):
        self.frames = {
            "player1" : ([(13, 41, 14, 15),(34,39,21,19),(64,39,21,19),(90,35,27,25)],[0.0667, 0.0333, 0.0333, 0.0667]),
            "player2" : ([(159, 41, 14, 15),(182,39,21,19),(211,39,21,19),(239,35,27,25)],[0.0667, 0.0333, 0.0333, 0.0667]),
        }
        super().__init__(x, y, playerNum, self.frames, *groups)
        
class HeavyHitSplash(HitSplash):
    def __init__(self, x, y, playerNum, *groups):
        self.frames = {
            "player1" : ([(14, 68, 15, 21),(38,70,27,23),(73,70,27,23),(106,66,32,31)],[0.0667, 0.0333, 0.0333, 0.0667]),
            "player2" : ([(160, 68, 15, 21),(185,70,27,23),(222,70,27,23),(255,66,32,31)],[0.033, 0.0166, 0.0166, 0.033]),
        }
        super().__init__(x, y, playerNum, self.frames, *groups)