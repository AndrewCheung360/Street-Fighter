import pygame as pg
from settings import *

class Stage:
    def __init__(self,name,image,x,y):
        self.name = name
        self.image = pg.transform.scale(pg.image.load(image).convert_alpha(), (WIDTH, HEIGHT))
        self.x = x
        self.y = y
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))