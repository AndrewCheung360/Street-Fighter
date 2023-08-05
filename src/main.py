import pygame as pg
from settings import *
from scenes.FightScene import FightScene


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption('Street Fighter')
        self.clock = pg.time.Clock()
        self.scene = FightScene(self.screen)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        
    def draw_scene(self):
        self.scene.update()
        self.scene.draw()
        
    def run(self):
        while True:
            self.handle_events()
            self.clock.tick(FPS)
            self.draw_scene()
            
           
            

if __name__ == '__main__':
    game = Game()
    game.run()
