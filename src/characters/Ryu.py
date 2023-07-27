import pygame as pg
from settings import *
from characters.Fighter import *
class Ryu(Fighter):
    def __init__(self,mode, playerNum, x,y,direction,*groups):
        self.name = "Ryu"
        self.sheet = 'assets/graphics/characters/Ryu/ryu_spritesheet.png'
        self.statusPortraitFrame = (1135,905,21,32)
        self.idleFrames = ([(6,18,43,81),(55,19,43,80),(105,18,43,81),(154,17,43,82)],[0.15,0.15,0.15,0.15])
        self.walkFrames = ([(205,24,43,75),(252,19,43,80),(301,18,43,81),(351,19,43,80),(401,19,43,80)],[0.1,0.1,0.1,0.1,0.1])
        self.jumpFrames = ([(452,24,43,75),(503,9,33,90),(545,17,29,78),(582,19,31,67),(619,17,29,78),(656,9,33,90),(696,24,43,75)],[0.02, 0.13, 0.2, 0.23, 0.2, 0.13, 0.02])
        self.sideJumpFrames = ([(747,24,43,75),(795,9,33,90),(835,40,61,37),(902,24,31,67),(942,36,72,39),(1021,25,43,74),(1071,9,33,90)],[0.05, 0.2, 0.15, 0.1, 0.15, 0.1, 0.32])
        self.crouchFrame = ([(1160, 44, 43, 55)],[0.2])
        self.lightPunchFrames = ([(3, 134, 43, 81),(52, 134, 57, 81),(117, 134, 43, 81)],[0.05,0.0667,0.0833])
        self.mediumPunchFrames = ([(170, 134, 43, 81),(218, 130, 51, 85),(274, 130, 72, 85),(353,130,51,85),(411,134,43,81)],[0.0333,0.0333,0.0667,0.1,0.0166])
        self.heavyPunchFrames = ([(170, 134, 43, 81),(218, 130, 51, 85),(274, 130, 72, 85),(353,130,51,85),(411,134,43,81)],[0.0667,0.0333,0.1,0.166,0.216])
        self.lightKickFrames = ([(6, 261, 49, 85),(62, 259, 67, 87),(135, 261, 49, 85)],[0.116,0.133,0.0833])
        self.mediumKickFrames = ([(6, 261, 49, 85),(62, 261, 67, 85),(135, 261, 49, 85)],[0.2,0.2,0.116])
        self.heavyKickFrames = ([(195, 265, 43, 81),(245, 262, 55, 84),(306, 262, 69, 84),(382,276,58,70),(448,273,43,73)],[0.05,0.0667,0.133,0.166,0.116])
        self.closeLightPunchFrames = ([(464, 134, 43, 81),(512, 127, 47, 88),(565, 134, 43, 81)],[0.05,0.0667,0.0833])
        self.closeMediumPunchFrames = ([(616, 134, 43, 81),(666, 130, 49, 85),(719, 130, 61, 85),(786,131,47,84),(839,130,61,85),(906,130,49,85),(961,134,43,81)],[0.0166,0.05,0.0333,0.1,0.0833,0.05,0.0833])
        self.closeHeavyPunchFrames = ([(1012, 130, 41, 85),(1060, 129, 60, 86),(1125, 112, 57, 103),(1187,129,60,86),(1253,134,43,81)],[0.0667,0.0333,0.1,0.166,0.216])
        self.closeLightKickFrames = ([(498, 262, 47, 84),(551, 264, 71, 82),(628, 262, 47, 84)],[0.1,0.1,0.0667])
        self.closeMediumKickFrames = ([(685, 265, 50, 81),(740, 263, 50, 83),(795, 254, 55, 92),(855,263,50,83),(910,265,50,81)],[0.05,0.0166,0.1,0.0667,0.0833])
        self.closeHeavyKickFrames = ([(969, 262, 47, 84),(1023, 248, 79, 98),(1107, 237, 53, 109),(1166,248,79,98),(1251,262,47,84)],[0.0667,0.0667,0.133,0.0667,0.183])
        self.crouchLightPunchFrames = ([(9, 419, 47, 55),(61, 419, 62, 55),(127, 419, 47, 55)],[0.05,0.0667,0.0833])
        self.crouchMediumPunchFrames = ([(181, 419, 45, 55),(232, 418, 61, 56),(298, 419, 45, 55),(348,419,45,55)],[0.0667,0.0667,0.05,0.0667])
        self.crouchHeavyPunchFrames = ([(401, 409, 43, 65),(450, 393, 49, 81),(505, 362, 44, 112),(555,393,49,81),(610,409,43,65)],[0.0667,0.05,0.133,0.166,0.216])
        self.crouchLightKickFrames = ([(660, 418, 49, 56),(714, 417, 71, 57),(790, 418, 49, 56)],[0.05,0.0667,0.0833])
        self.crouchMediumKickFrames = ([(846, 418, 49, 56),(900, 426, 89, 48),(993, 418, 49, 56)],[0.0667,0.1,0.15])
        self.crouchHeavyKickFrames = ([(1049, 420, 47, 54),(1104, 421, 70, 53),(1179, 422, 51, 52),(1235,421,47,53),(1286,419,43,55)],[0.0667,0.1,0.1,0.133,0.183])
        
        self.jumpLightPunchFrames = ([(385, 547, 31, 67),(421, 554, 39, 53),(109, 547, 31, 67)],[0.0333,0.2, 0.133])
        self.jumpMediumPunchFrames = ([(7, 547, 40, 67),(52, 552, 51, 55),(109, 547, 31, 67)],[0.0667,0.2,0.133])
        self.jumpHeavyPunchFrames = ([(7, 547, 40, 67),(52, 552, 51, 55),(109, 547, 31, 67)],[0.0833,0.2,0.133])
        self.jumpLightKickFrames = ([(149, 532, 45, 82),(203, 540, 31, 67)],[0.166,0.2])
        self.jumpMediumKickFrames = ([(149, 532, 45, 82),(203, 540, 31, 67)],[0.216,0.1])
        self.jumpHeavyKickFrames = ([(247, 532, 32, 82),(283, 525, 53, 89),(341,531,34,83),(619,17,29,78),(656,9,33,90)],[0.1,0.0667,0.116,0.0667,0.0667])
        
        self.diagonalJumpLightPunchFrames = ([(385, 547, 31, 67),(421, 554, 39, 53),(109, 547, 31, 67)],[0.0333,0.2,0.133])
        self.diagonalJumpMediumPunchFrames = ([(7, 547, 40, 67),(52, 552, 51, 55),(109, 547, 31, 67)],[0.0667,0.2,0.133])
        self.diagonalJumpHeavyPunchFrames = ([(7, 547, 40, 67),(52, 552, 51, 55),(109, 547, 31, 67)],[0.0833,0.2,0.133])
        self.diagonalJumpLightKickFrames = ([(385, 547, 31, 67),(421, 554, 39, 53),(109, 547, 31, 67)],[0.0333,0.2,0.133])
        
        self.diagonalJumpMediumKickFrames = ([(468, 551, 37, 63),(510, 554, 63, 54),(577, 551, 37, 63),(656,9,33,90)],[0.0667,0.2,0.1,0.0667])
        self.diagonalJumpHeavyKickFrames = ([(468, 551, 37, 63),(510, 554, 63, 54),(577, 551, 37, 63),(656,9,33,90)],[0.1,0.2,0.1,0.0667])
        
        self.frame_dict = {
                           "status_portrait" : self.statusPortraitFrame,
                           "idle": self.idleFrames,
                           "walk": self.walkFrames,
                           "jump": self.jumpFrames,
                           "side_jump": self.sideJumpFrames,
                           "crouch": self.crouchFrame,
                           "light_punch": self.lightPunchFrames,
                           "medium_punch": self.mediumPunchFrames,
                           "heavy_punch": self.heavyPunchFrames,
                           "light_kick": self.lightKickFrames,
                           "medium_kick": self.mediumKickFrames,
                           "heavy_kick": self.heavyKickFrames,
                           "close_light_punch": self.closeLightPunchFrames,
                           "close_medium_punch": self.closeMediumPunchFrames,
                           "close_heavy_punch": self.closeHeavyPunchFrames,
                           "close_light_kick": self.closeLightKickFrames,
                           "close_medium_kick": self.closeMediumKickFrames,
                           "close_heavy_kick": self.closeHeavyKickFrames,
                           "crouch_light_punch": self.crouchLightPunchFrames,
                           "crouch_medium_punch": self.crouchMediumPunchFrames,
                           "crouch_heavy_punch": self.crouchHeavyPunchFrames,
                           "crouch_light_kick": self.crouchLightKickFrames,
                           "crouch_medium_kick": self.crouchMediumKickFrames,
                           "crouch_heavy_kick": self.crouchHeavyKickFrames,
                           "jump_light_punch": self.jumpLightPunchFrames,
                           "jump_medium_punch": self.jumpMediumPunchFrames,
                           "jump_heavy_punch": self.jumpHeavyPunchFrames,
                           "jump_light_kick": self.jumpLightKickFrames,
                           "jump_medium_kick": self.jumpMediumKickFrames,
                           "jump_heavy_kick": self.jumpHeavyKickFrames,
                           "diagonal_jump_light_punch": self.diagonalJumpLightPunchFrames,
                           "diagonal_jump_medium_punch": self.diagonalJumpMediumPunchFrames,
                           "diagonal_jump_heavy_punch": self.diagonalJumpHeavyPunchFrames,
                           "diagonal_jump_light_kick": self.diagonalJumpLightKickFrames,
                           "diagonal_jump_medium_kick": self.diagonalJumpMediumKickFrames,
                           "diagonal_jump_heavy_kick": self.diagonalJumpHeavyKickFrames,
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
                                        "width" : 130,
                                        "height" : 220
                                        },
                          }
        super().__init__(mode, playerNum,self.name,self.sheet,"black",x,y,self.frame_dict,self.pushboxes,direction,*groups)
    
    def update(self):
        super().update()
        if self.state == STATE_LIGHT_PUNCH or self.state == STATE_MEDIUM_PUNCH or self.state == STATE_HEAVY_PUNCH or self.state == STATE_CROUCH_LIGHT_PUNCH or self.state == STATE_CROUCH_MEDIUM_PUNCH:
            if self.direction == "right":
                self.rect.bottomleft = self.pos - vec(self.idleFrames[0][0][2] * 4 // 2,0)
            else:
                self.rect.bottomright = self.pos + vec(self.idleFrames[0][0][2] * 4 // 2,0)