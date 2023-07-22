import pygame as pg
from settings import *
from characters.Fighter import *
class Ryu(Fighter):
    def __init__(self,mode, playerNum, x,y,direction,*groups):
        self.idleFrames = ([(6,18,43,81),(55,19,43,80),(105,18,43,81),(154,17,43,82)],[0.15,0.15,0.15,0.15])
        self.walkFrames = ([(205,24,43,75),(252,19,43,80),(301,18,43,81),(351,19,43,80),(401,19,43,80)],[0.1,0.1,0.1,0.1,0.1])
        self.jumpFrames = ([(452,24,43,75),(503,9,33,90),(545,17,29,78),(582,19,31,67),(619,17,29,78),(656,9,33,90),(696,24,43,75)],[0.02, 0.23, 0.3, 0.3, 0.3, 0.23, 0.02])
        super().__init__(mode, playerNum,'Ryu','assets/graphics/characters/Ryu/ryu_spritesheet.png',"black",x,y,self.idleFrames,self.walkFrames, self.jumpFrames, direction,*groups)
    