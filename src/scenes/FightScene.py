import pygame as pg
from settings import *
from characters.Ryu import Ryu
from characters.Ken import Ken
from stages.KenStage import KenStage
from HUD.StatusBar import StatusBar
from characters.HitSplash import LightHitSplash, MediumHitSplash, HeavyHitSplash

vec = pg.math.Vector2

#localKeyBoard, localLaptop, multiplayer (on same network)
mode = "localLaptop"
#set True to see hitboxes and hurtboxes
debug = True

class FightScene:
    def __init__(self, screen):
        self.screen = screen
        self.background = KenStage(0, 0)
        self.player1_sprites = pg.sprite.GroupSingle()
        self.player2_sprites = pg.sprite.GroupSingle()
        self.misc_sprites = pg.sprite.Group()
        if(mode == "localLaptop"):
            self.player1 = Ryu("localLaptop", "player1",200, STAGE_FLOOR, "right",self, self.player1_sprites)
            self.player2 = Ken("localLaptop", "player2",1080, STAGE_FLOOR, "left", self, self.player2_sprites)
            self.player1.opponent = self.player2
            self.player2.opponent = self.player1
            self.statusBar = StatusBar(self.player1, self.player2)
        elif(mode == "local"):
            self.player1 = Ryu("localKeyboard", "player1",200, STAGE_FLOOR, "right",self, self.player1_sprites)
            self.player2 = Ken("localKeyboard", "player2",1080, STAGE_FLOOR, "left", self, self.player2_sprites)
            self.player1.opponent = self.player2
            self.player2.opponent = self.player1
            self.statusBar = StatusBar(self.player1, self.player2)
        else:
            self.player1 = Ryu("multi", "player1",200, STAGE_FLOOR, "right",self.player1_sprites)
            self.player2 = Ryu("multi", "player2",1080, STAGE_FLOOR, "left" ,self.player2_sprites)
            self.player1.opponent = self.player2
            self.player2.opponent = self.player1
            self.statusBar = StatusBar(self.player1, self.player2)
    
    def handle_hit_splash(self, x, y, playerNum, hitType):
        if hitType == "light":
            self.splash = LightHitSplash(x, y, playerNum, self.misc_sprites)
        elif hitType == "medium":
            self.splash = MediumHitSplash(x, y, playerNum, self.misc_sprites)
        elif hitType == "heavy":
            self.splash = HeavyHitSplash(x, y, playerNum, self.misc_sprites)
           
    def update(self):
        self.player1_sprites.update()
        self.player2_sprites.update()
        self.misc_sprites.update()
        self.statusBar.update(1/FPS)
        
    def draw(self):
        self.background.draw(self.screen)
        if self.player1.is_attacking():
            self.player2_sprites.draw(self.screen)
            self.player1_sprites.draw(self.screen)
        else:
            self.player1_sprites.draw(self.screen)
            self.player2_sprites.draw(self.screen)
            
        self.misc_sprites.draw(self.screen)
        
        if debug:
            if self.player1.hurtboxes["head"] != None and self.player1.hurtboxes["body"] != None and self.player1.hurtboxes["legs"] != None:    
                pg.draw.rect(self.screen, "blue", self.player1.hurtboxes["head"], 2)
                pg.draw.rect(self.screen, "blue", self.player1.hurtboxes["body"], 2)
                pg.draw.rect(self.screen, "blue", self.player1.hurtboxes["legs"], 2)
            if self.player2.hurtboxes["head"] != None and self.player2.hurtboxes["body"] != None and self.player2.hurtboxes["legs"] != None:    
                pg.draw.rect(self.screen, "blue", self.player2.hurtboxes["head"], 2)
                pg.draw.rect(self.screen, "blue", self.player2.hurtboxes["body"], 2)
                pg.draw.rect(self.screen, "blue", self.player2.hurtboxes["legs"], 2)
                
            if self.player1.hitbox != None:
                pg.draw.rect(self.screen, "red", self.player1.hitbox, 2)
            if self.player2.hitbox != None:
                pg.draw.rect(self.screen, "red", self.player2.hitbox, 2)
        
        self.statusBar.draw(self.screen)
        pg.display.update()
        
            

