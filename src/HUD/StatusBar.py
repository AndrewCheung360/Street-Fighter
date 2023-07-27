import pygame as pg
from settings import *
from spritesheet import SpriteSheet

class StatusBar():
    def __init__(self, fighter1, fighter2):
        
        #sheet containing HUD elements
        self.sheet = SpriteSheet('assets/graphics/misc/misc.png',"black")
        
        #ko-white
        self.koWhite = pg.transform.scale_by(pg.image.load('assets/graphics/misc/ko-white.png').convert_alpha(),3.5)
        
        #countdown states
        self.time = 99
        self.timerTime = 0
        
        #player 1 and player 2
        self.fighter1 = fighter1
        self.fighter2 = fighter2
        
        #player sprite sheets and portraits
        self.fighter1Sheet = SpriteSheet(fighter1.sheet,"black")
        self.fighter2Sheet = SpriteSheet(fighter2.sheet,"black")
        self.fighter1Portrait = self.fighter1Sheet.get_image(fighter1.frame_dict["status_portrait"])
        self.fighter2Portrait = self.fighter2Sheet.get_image(fighter2.frame_dict["status_portrait"])
        
        #frame dictionary
        self.frame_dict = {
            "health-bar" : (16,18,145,11),
            
            #time
            "0" : (16, 32, 12, 14),
            "1" : (34, 32, 9, 14),
            "2" : (48, 32, 13, 14),
            "3" : (64, 32, 13, 14),
            "4" : (80, 32, 13, 14),
            "5" : (96, 32, 13, 14),
            "6" : (112, 32, 12, 14),
            "7" : (128, 32, 13, 14),
            "8" : (144, 32, 12, 14),
            "9" : (160, 32, 12, 14),
            
            #score nums
            "score-0" : (17,101,10,10),
            "score-1" : (29,101,10,10),
            "score-2" : (41,101,10,10),
            "score-3" : (53,101,10,10),
            "score-4" : (65,101,10,10),
            "score-5" : (77,101,10,10),
            "score-6" : (89,101,10,10),
            "score-7" : (101,101,10,10),
            "score-8" : (113,101,10,10),
            "score-9" : (125,101,10,10),
            
            
            #score letters
            "score-@" : (17,113,10,10),
            "score-A" : (29,113,10,10),
            "score-B" : (41,113,10,10),
            "score-C" : (53,113,10,10),
            "score-D" : (65,113,10,10),
            "score-E" : (77,113,10,10),
            "score-F" : (89,113,10,10),
            "score-G" : (101,113,10,10),
            "score-H" : (113,113,10,10),
            "score-I" : (125,113,10,10),
            "score-J" : (137,113,10,10),
            "score-K" : (149,113,10,10),
            "score-L" : (161,113,10,10),
            "score-M" : (173,113,10,10),
            "score-N" : (185,113,10,10),
            "score-O" : (197,113,10,10),
            "score-P" : (17,125,10,10),
            "score-Q" : (29,125,10,10),
            "score-R" : (41,125,10,10),
            "score-S" : (53,125,10,10),
            "score-T" : (65,125,10,10),
            "score-U" : (77,125,10,10),
            "score-V" : (89,125,10,10),
            "score-W" : (101,125,10,10),
            "score-X" : (113,125,10,10),
            "score-Y" : (125,125,10,10),
            "score-Z" : (137,125,10,10),
            
            #name tags
            "tag-ryu" : (16,56, 28, 9),
            "tag-ken" : (128, 56, 30, 9),
        }
        
        
        
    def update(self,dt):
         # Calculate the elapsed time
        self.timerTime += dt
        
        # Check if 1 second has elapsed
        if self.timerTime >= 1.0:
            # Decrease the time by 1 second
            self.time -= 1
            # Reset the elapsed time
            self.timerTime = 0.0
        
        # Ensure the time doesn't go below 0
        if self.time < 0:
            self.time = 0
    
        
    def draw_frame(self, screen, frame, x, y, scale = 1, flip=False):
        image = self.sheet.get_image(frame, scale, flip)
        screen.blit(image, (x,y))
    
    def draw_score(self, screen, score, x):
        scoreString = str(score)
        num_digits = min(len(scoreString), 6)

        # Calculate the starting x position based on the last digit
        start_x = x - (num_digits - 1) * 36

        for i in range(num_digits):
            self.draw_frame(screen, self.frame_dict["score-" + scoreString[i]], start_x + (i * 36), 20, 3.25)
        
    def draw_score_name(self, screen, name, x):
        for i in range(len(name)):
            self.draw_frame(screen, self.frame_dict["score-" + name[i]], x + (i * 36), 20, 3.25)
            
    def draw_scores(self, screen):
        #P1
        self.draw_score_name(screen, "1P", 20)
        #P2
        self.draw_score_name(screen, "2P", ((WIDTH - self.koWhite.get_width()) // 2 + self.koWhite.get_width()) + 203)

        #score name
        self.draw_score_name(screen,"ANDREW", 400)
        
        #p1 score
        self.draw_score(screen, 1, 330)
        #default high score
        self.draw_score(screen, 50000, ((WIDTH - self.koWhite.get_width()) // 2 + self.koWhite.get_width()) + 100)
        #p2 score
        self.draw_score(screen, 1, ((WIDTH - self.koWhite.get_width()) // 2 + self.koWhite.get_width()) + 515)
     
    def draw_portraits(self, screen):
        fighter1PortraitScaled = pg.transform.scale(self.fighter1Portrait, (self.fighter1Portrait.get_width() * 4.5, self.fighter1Portrait.get_height() * 3)) 
        fighter2PortraitScaled = pg.transform.scale(self.fighter2Portrait, (self.fighter1Portrait.get_width() * 4.5, self.fighter1Portrait.get_height() * 3))
        screen.blit(fighter1PortraitScaled, (10,110))
        screen.blit(fighter2PortraitScaled, (1180,110))       
        
        
    def draw_name_tags(self, screen, fighter1, fighter2):
        fighter1Name = fighter1.name.lower()
        fighter2Name = fighter2.name.lower()
        
        fighter1_tag_x = ((WIDTH - self.koWhite.get_width()) // 2) - (self.frame_dict["health-bar"][2] * 3.25)
        self.draw_frame(screen, self.frame_dict["tag-" + fighter1Name], fighter1_tag_x, 115, 3.5)
        
        fighter2_tag_x = ((WIDTH - self.koWhite.get_width()) // 2 + self.koWhite.get_width()) + (self.frame_dict["health-bar"][2] * 3.25) - self.frame_dict["tag-" + fighter2Name][2] * 3.5
        self.draw_frame(screen, self.frame_dict["tag-" + fighter2Name], fighter2_tag_x, 115, 3.5)
        
    def draw_health_bars(self, screen):
        self.draw_frame(screen, self.frame_dict["health-bar"], ((WIDTH - self.koWhite.get_width()) // 2) - (self.frame_dict["health-bar"][2] * 3.25), 70, 3.25)
        screen.blit(self.koWhite, ((WIDTH - self.koWhite.get_width()) // 2,65))
        self.draw_frame(screen, self.frame_dict["health-bar"], ((WIDTH - self.koWhite.get_width()) // 2 + self.koWhite.get_width()), 70, 3.25, True)
        
    def draw_countdown(self, screen):
        timeString = str(self.time).zfill(2)
        self.draw_frame(screen, self.frame_dict[timeString[0]], ((WIDTH - self.koWhite.get_width()) // 2) + 15 , 120, 3.25)
        self.draw_frame(screen, self.frame_dict[timeString[1]], ((WIDTH - self.koWhite.get_width()) // 2) + 59 , 120, 3.25)
        
    
    def draw(self, screen):
        
        #score
        self.draw_scores(screen)
        
        #portraits
        self.draw_portraits(screen)
        
        #name tags
        self.draw_name_tags(screen, self.fighter1, self.fighter2)
        
        #health bars and ko-white
        self.draw_health_bars(screen)
        
        #timer
        self.draw_countdown(screen)
        
        