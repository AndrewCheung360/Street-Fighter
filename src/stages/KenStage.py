import pygame as pg
from settings import *
from stages.Stage import *

class KenStage(Stage):
    def __init__(self,x,y):
        super().__init__('KenStage','assets/graphics/stages/Ken-SF2-Stage.webp',x,y)