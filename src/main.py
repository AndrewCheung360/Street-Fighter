import pygame as pg
from settings import *
from characters.Ryu import Ryu
from characters.Ken import Ken
from stages.KenStage import KenStage
import time

mode = "local"

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption('Street Fighter')
        self.clock = pg.time.Clock()
        self.background = KenStage(0, 0)
        self.player1_sprites = pg.sprite.GroupSingle()
        self.player2_sprites = pg.sprite.GroupSingle()
        if(mode == "local"):
            self.player1 = Ryu("local", "player1",200, STAGE_FLOOR, "right",self.player1_sprites)
            self.player2 = Ken("local", "player2",600, STAGE_FLOOR, "left" ,self.player2_sprites)
        else:
            self.player1 = Ryu("multi", "player1",200, STAGE_FLOOR, "right",self.player1_sprites)
            self.player2 = Ryu("multi", "player2",600, STAGE_FLOOR, "left" ,self.player2_sprites)
        

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

    def draw(self):
        self.background.draw(self.screen)
        self.player1_sprites.draw(self.screen)
        self.player2_sprites.draw(self.screen)
        pg.display.update()
        
    def directionUpdate(self):
        if self.player1.pos.x > self.player2.pos.x:
            self.player1.direction = "left"
            self.player2.direction = "right"
        elif self.player1.pos.x < self.player2.pos.x:
            self.player1.direction = "right"
            self.player2.direction = "left"
    def run(self):
        while True:
            self.handle_events()
            self.directionUpdate()
            self.player1_sprites.update()
            self.player2_sprites.update()
            self.draw()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
