import pygame as pg
from settings import *
from characters.Fighter import *
class Ken(Fighter):
    def __init__(self,mode, playerNum,x,y,direction,*groups):
        self.idleFrames = ([(6,18,43,81),(55,19,43,80),(105,18,43,81),(154,17,43,82)],[0.15,0.15,0.15,0.15])
        self.walkFrames = ([(205,24,43,75),(252,19,43,80),(301,18,43,81),(351,19,43,80),(401,19,43,80)],[0.1,0.1,0.1,0.1,0.1])
        self.jumpFrames = ([(452,24,43,75),(503,9,33,90),(545,17,29,78),(582,19,31,67),(619,17,29,78),(656,9,33,90),(696,24,43,75)],[0.02, 0.13, 0.2, 0.23, 0.2, 0.13, 0.02])
        self.sideJumpFrames = ([(747,24,43,75),(795,9,33,90),(835,40,61,37),(902,24,31,67),(942,36,72,39),(1021,25,43,74),(1071,9,33,90)],[0.05, 0.2, 0.15, 0.1, 0.15, 0.1, 0.32])
        self.crouchFrame = ([(1160, 44, 43, 55)],[0.2])
        self.frame_dict = {
                           "idle": self.idleFrames,
                           "walk": self.walkFrames,
                           "jump": self.jumpFrames,
                           "side_jump": self.sideJumpFrames,
                           "crouch": self.crouchFrame
                           }
        self.pushboxes = {
                            "default" :{
                                        "x-offset" : 0,
                                        "y-offset" : 0,
                                        "width" : 90,
                                        "height" : 324
                                        },
                            "crouch" : {
                                        "x-offset" : 0,
                                        "y-offset" : 0,
                                        "width" : 142,
                                        "height" : 220
                                        },
                          }
        super().__init__(mode, playerNum,'Ken','assets/graphics/characters/Ken/ken_spritesheet.png',"black",x,y,self.frame_dict, self.pushboxes,direction,*groups)
    