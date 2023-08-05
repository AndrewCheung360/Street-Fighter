import pygame as pg
from settings import *
from spritesheet import SpriteSheet, Animation
from animatedsprite import AnimatedSprite
from characters.MoveStates import *
from states.gameState import gameState

vec = pg.math.Vector2

class Fighter(AnimatedSprite):
    def __init__(self, mode, playerNum, name, sheet, bg, x, y, frame_dict, boxes, direction, fightScene,*groups):
        super().__init__(*groups)
        
        self.mode = mode
        self.playerNum = playerNum
        self.name = name
        self.direction = direction
        self.fightScene = fightScene
        #spritesheet
        self.sheet = sheet
        self.bg = bg
        self.statusPortraitFrame = frame_dict["status_portrait"]
        
        #animation frames
        self.idleFrames = frame_dict["idle"]
        self.walkFrames = frame_dict["walk"]
        self.jumpFrames = frame_dict["jump"]
        self.sideJumpFrames = frame_dict["side_jump"]
        self.crouchFrame = frame_dict["crouch"]
        self.lightPunchFrames = frame_dict["light_punch"]
        self.mediumPunchFrames = frame_dict["medium_punch"]
        self.heavyPunchFrames = frame_dict["heavy_punch"]
        self.lightKickFrames = frame_dict["light_kick"]
        self.mediumKickFrames = frame_dict["medium_kick"]
        self.heavyKickFrames = frame_dict["heavy_kick"]
        self.closeLightPunchFrames = frame_dict["close_light_punch"]
        self.closeMediumPunchFrames = frame_dict["close_medium_punch"]
        self.closeHeavyPunchFrames = frame_dict["close_heavy_punch"]
        self.closeLightKickFrames = frame_dict["close_light_kick"]
        self.closeMediumKickFrames = frame_dict["close_medium_kick"]
        self.closeHeavyKickFrames = frame_dict["close_heavy_kick"]
        self.crouchLightPunchFrames = frame_dict["crouch_light_punch"]
        self.crouchMediumPunchFrames = frame_dict["crouch_medium_punch"]
        self.crouchHeavyPunchFrames = frame_dict["crouch_heavy_punch"]
        self.crouchLightKickFrames = frame_dict["crouch_light_kick"]
        self.crouchMediumKickFrames = frame_dict["crouch_medium_kick"]
        self.crouchHeavyKickFrames = frame_dict["crouch_heavy_kick"]
        self.jumpLightPunchFrames = frame_dict["jump_light_punch"]
        self.jumpMediumPunchFrames = frame_dict["jump_medium_punch"]
        self.jumpHeavyPunchFrames = frame_dict["jump_heavy_punch"]
        self.jumpLightKickFrames = frame_dict["jump_light_kick"]
        self.jumpMediumKickFrames = frame_dict["jump_medium_kick"]
        self.jumpHeavyKickFrames = frame_dict["jump_heavy_kick"]
        self.diagonalJumpLightPunchFrames = frame_dict["diagonal_jump_light_punch"]
        self.diagonalJumpMediumPunchFrames = frame_dict["diagonal_jump_medium_punch"]
        self.diagonalJumpHeavyPunchFrames = frame_dict["diagonal_jump_heavy_punch"]
        self.diagonalJumpLightKickFrames = frame_dict["diagonal_jump_light_kick"]
        self.diagonalJumpMediumKickFrames = frame_dict["diagonal_jump_medium_kick"]
        self.diagonalJumpHeavyKickFrames = frame_dict["diagonal_jump_heavy_kick"]
        
        #initial state
        self.state = STATE_IDLE
        
        #opponent fighter reference
        self.opponent = None
        
        #load animations during initialization
        self.load()
        
        #sprite image and animation
        self.image = self.active_anim.get_frame(0)
        self.rect = self.image.get_rect()
  
        #movement and position
        self.pos = vec(x, y)
        self.vel = vec(0, 0)
        
        #collision props
        self.boxes = boxes
        
        self.pushbox_list = self.boxes["pushboxes"]
        self.default_pushbox = pg.Rect((self.pos.x - self.pushbox_list["default"]["width"] // 2) + self.pushbox_list["default"]["x-offset"], self.pos.y - self.pushbox_list["default"]["height"] + self.pushbox_list["default"]["y-offset"], self.pushbox_list["default"]["width"], self.pushbox_list["default"]["height"])
        self.pushbox = self.default_pushbox
        
        self.hurtbox_list = self.boxes["hurtboxes"]
        
        self.hurtboxes = {
            "head" : None,
            "body" : None,
            "legs" : None,
        }
        
        self.hitbox_list = self.boxes["hitboxes"]
        
        self.hitbox = None
        
        self.attackStruck = False
        
    #store animations from spritesheet
    def load(self):
        spritesheet = SpriteSheet(self.sheet, self.bg)
        
        #idle animation
        idle_animation = spritesheet.get_animation(self.idleFrames[0], self.idleFrames[1], Animation.PlayMode.LOOP, 4)
        self.store_animation("idle", idle_animation)
        idle_animationR = spritesheet.get_animation(self.idleFrames[0], self.idleFrames[1], Animation.PlayMode.LOOP, 4, True)
        self.store_animation("idleR", idle_animationR)
        
        #walk animation
        walk_animation = spritesheet.get_animation(self.walkFrames[0], self.walkFrames[1], Animation.PlayMode.LOOP, 4)
        self.store_animation("walk", walk_animation)
        walk_animationR = spritesheet.get_animation(self.walkFrames[0], self.walkFrames[1], Animation.PlayMode.LOOP, 4, True)
        self.store_animation("walkR", walk_animationR)
        
        #backwalk animation
        backwalk = list(self.walkFrames[0])  # Create a copy of the array
        backwalk.reverse()  # Reverse the copy
        backwalk_animation = spritesheet.get_animation(backwalk, self.walkFrames[1], Animation.PlayMode.LOOP, 4)
        self.store_animation("backwalk", backwalk_animation)
        backwalk_animationR = spritesheet.get_animation(backwalk, self.walkFrames[1], Animation.PlayMode.LOOP, 4, True)
        self.store_animation("backwalkR", backwalk_animationR)
        
        #jump animation
        jump_animation = spritesheet.get_animation(self.jumpFrames[0], self.jumpFrames[1], Animation.PlayMode.NORMAL, 4)
        self.store_animation("jump", jump_animation)
        jump_animationR = spritesheet.get_animation(self.jumpFrames[0], self.jumpFrames[1], Animation.PlayMode.NORMAL, 4, True)
        self.store_animation("jumpR", jump_animationR)
        
        #forward jump animation
        forward_jump_animation = spritesheet.get_animation(self.sideJumpFrames[0], self.sideJumpFrames[1], Animation.PlayMode.NORMAL, 4)
        self.store_animation("forward_jump", forward_jump_animation)
        forward_jump_animationR = spritesheet.get_animation(self.sideJumpFrames[0], self.sideJumpFrames[1], Animation.PlayMode.NORMAL, 4, True)
        self.store_animation("forward_jumpR", forward_jump_animationR)
        
        #backward jump animation
        backJump = [self.sideJumpFrames[0][0]] + self.sideJumpFrames[0][1:][::-1]
        backward_jump_animation = spritesheet.get_animation(backJump, self.sideJumpFrames[1], Animation.PlayMode.NORMAL, 4)
        self.store_animation("backward_jump", backward_jump_animation)
        backward_jump_animationR = spritesheet.get_animation(backJump, self.sideJumpFrames[1], Animation.PlayMode.NORMAL, 4, True)
        self.store_animation("backward_jumpR", backward_jump_animationR)
     
        #crouch animation
        crouch_animation = spritesheet.get_animation(self.crouchFrame[0], self.crouchFrame[1], Animation.PlayMode.LOOP, 4)
        self.store_animation("crouch", crouch_animation)
        crouch_animationR = spritesheet.get_animation(self.crouchFrame[0], self.crouchFrame[1], Animation.PlayMode.LOOP, 4, True)
        self.store_animation("crouchR", crouch_animationR)

        #light punch animation
        light_punch_animation = spritesheet.get_animation(self.lightPunchFrames[0], self.lightPunchFrames[1], Animation.PlayMode.NORMAL, 4)
        self.store_animation("light_punch", light_punch_animation)
        light_punch_animationR = spritesheet.get_animation(self.lightPunchFrames[0], self.lightPunchFrames[1], Animation.PlayMode.NORMAL, 4, True)
        self.store_animation("light_punchR", light_punch_animationR)

        #medium punch animation
        medium_punch_animation = spritesheet.get_animation(self.mediumPunchFrames[0], self.mediumPunchFrames[1], Animation.PlayMode.NORMAL, 4)
        self.store_animation("medium_punch", medium_punch_animation)
        medium_punch_animationR = spritesheet.get_animation(self.mediumPunchFrames[0], self.mediumPunchFrames[1], Animation.PlayMode.NORMAL, 4, True)
        self.store_animation("medium_punchR", medium_punch_animationR)
        
        #heavy punch animation
        heavy_punch_animation = spritesheet.get_animation(self.heavyPunchFrames[0], self.heavyPunchFrames[1], Animation.PlayMode.NORMAL, 4)
        self.store_animation("heavy_punch", heavy_punch_animation)
        heavy_punch_animationR = spritesheet.get_animation(self.heavyPunchFrames[0], self.heavyPunchFrames[1], Animation.PlayMode.NORMAL, 4, True)
        self.store_animation("heavy_punchR", heavy_punch_animationR)
        
        #light kick animation
        light_kick_animation = spritesheet.get_animation(self.lightKickFrames[0], self.lightKickFrames[1], Animation.PlayMode.NORMAL, 4)
        self.store_animation("light_kick", light_kick_animation)
        light_kick_animationR = spritesheet.get_animation(self.lightKickFrames[0], self.lightKickFrames[1], Animation.PlayMode.NORMAL, 4, True)
        self.store_animation("light_kickR", light_kick_animationR)
        
        #medium kick animation
        medium_kick_animation = spritesheet.get_animation(self.mediumKickFrames[0], self.mediumKickFrames[1], Animation.PlayMode.NORMAL, 4)
        self.store_animation("medium_kick", medium_kick_animation)
        medium_kick_animationR = spritesheet.get_animation(self.mediumKickFrames[0], self.mediumKickFrames[1], Animation.PlayMode.NORMAL, 4, True)
        self.store_animation("medium_kickR", medium_kick_animationR)
        
        #heavy kick animation
        heavy_kick_animation = spritesheet.get_animation(self.heavyKickFrames[0], self.heavyKickFrames[1], Animation.PlayMode.NORMAL, 4)
        self.store_animation("heavy_kick", heavy_kick_animation)
        heavy_kick_animationR = spritesheet.get_animation(self.heavyKickFrames[0], self.heavyKickFrames[1], Animation.PlayMode.NORMAL, 4, True)
        self.store_animation("heavy_kickR", heavy_kick_animationR)
        
        #close light punch animation
        close_light_punch_animation = spritesheet.get_animation(self.closeLightPunchFrames[0], self.closeLightPunchFrames[1], Animation.PlayMode.NORMAL, 4)
        self.store_animation("close_light_punch", close_light_punch_animation)
        close_light_punch_animationR = spritesheet.get_animation(self.closeLightPunchFrames[0], self.closeLightPunchFrames[1], Animation.PlayMode.NORMAL, 4, True)
        self.store_animation("close_light_punchR", close_light_punch_animationR)
        
        #close medium punch animation
        close_medium_punch_animation = spritesheet.get_animation(self.closeMediumPunchFrames[0], self.closeMediumPunchFrames[1], Animation.PlayMode.NORMAL, 4)
        self.store_animation("close_medium_punch", close_medium_punch_animation)
        close_medium_punch_animationR = spritesheet.get_animation(self.closeMediumPunchFrames[0], self.closeMediumPunchFrames[1], Animation.PlayMode.NORMAL, 4, True)
        self.store_animation("close_medium_punchR", close_medium_punch_animationR)
        
        #close heavy punch animation
        close_heavy_punch_animation = spritesheet.get_animation(self.closeHeavyPunchFrames[0], self.closeHeavyPunchFrames[1], Animation.PlayMode.NORMAL, 4)
        self.store_animation("close_heavy_punch", close_heavy_punch_animation)
        close_heavy_punch_animationR = spritesheet.get_animation(self.closeHeavyPunchFrames[0], self.closeHeavyPunchFrames[1], Animation.PlayMode.NORMAL, 4, True)
        self.store_animation("close_heavy_punchR", close_heavy_punch_animationR)
        
        #close light kick animation
        close_light_kick_animation = spritesheet.get_animation(self.closeLightKickFrames[0], self.closeLightKickFrames[1], Animation.PlayMode.NORMAL, 4)
        self.store_animation("close_light_kick", close_light_kick_animation)
        close_light_kick_animationR = spritesheet.get_animation(self.closeLightKickFrames[0], self.closeLightKickFrames[1], Animation.PlayMode.NORMAL, 4, True)
        self.store_animation("close_light_kickR", close_light_kick_animationR)
        
        #close medium kick animation
        close_medium_kick_animation = spritesheet.get_animation(self.closeMediumKickFrames[0], self.closeMediumKickFrames[1], Animation.PlayMode.NORMAL, 4)
        self.store_animation("close_medium_kick", close_medium_kick_animation)
        close_medium_kick_animationR = spritesheet.get_animation(self.closeMediumKickFrames[0], self.closeMediumKickFrames[1], Animation.PlayMode.NORMAL, 4, True)
        self.store_animation("close_medium_kickR", close_medium_kick_animationR)
        
        #close heavy kick animation
        close_heavy_kick_animation = spritesheet.get_animation(self.closeHeavyKickFrames[0], self.closeHeavyKickFrames[1], Animation.PlayMode.NORMAL, 4)
        self.store_animation("close_heavy_kick", close_heavy_kick_animation)
        close_heavy_kick_animationR = spritesheet.get_animation(self.closeHeavyKickFrames[0], self.closeHeavyKickFrames[1], Animation.PlayMode.NORMAL, 4, True)
        self.store_animation("close_heavy_kickR", close_heavy_kick_animationR)
        
        #crouch light punch animation
        crouch_light_punch_animation = spritesheet.get_animation(self.crouchLightPunchFrames[0], self.crouchLightPunchFrames[1], Animation.PlayMode.NORMAL, 4)
        self.store_animation("crouch_light_punch", crouch_light_punch_animation)
        crouch_light_punch_animationR = spritesheet.get_animation(self.crouchLightPunchFrames[0], self.crouchLightPunchFrames[1], Animation.PlayMode.NORMAL, 4, True)
        self.store_animation("crouch_light_punchR", crouch_light_punch_animationR)
        
        #crouch medium punch animation
        crouch_medium_punch_animation = spritesheet.get_animation(self.crouchMediumPunchFrames[0], self.crouchMediumPunchFrames[1], Animation.PlayMode.NORMAL, 4)
        self.store_animation("crouch_medium_punch", crouch_medium_punch_animation)
        crouch_medium_punch_animationR = spritesheet.get_animation(self.crouchMediumPunchFrames[0], self.crouchMediumPunchFrames[1], Animation.PlayMode.NORMAL, 4, True)
        self.store_animation("crouch_medium_punchR", crouch_medium_punch_animationR)
        
        #crouch heavy punch animation
        crouch_heavy_punch_animation = spritesheet.get_animation(self.crouchHeavyPunchFrames[0], self.crouchHeavyPunchFrames[1], Animation.PlayMode.NORMAL, 4)
        self.store_animation("crouch_heavy_punch", crouch_heavy_punch_animation)
        crouch_heavy_punch_animationR = spritesheet.get_animation(self.crouchHeavyPunchFrames[0], self.crouchHeavyPunchFrames[1], Animation.PlayMode.NORMAL, 4, True)
        self.store_animation("crouch_heavy_punchR", crouch_heavy_punch_animationR)
        
        #crouch light kick animation
        crouch_light_kick_animation = spritesheet.get_animation(self.crouchLightKickFrames[0], self.crouchLightKickFrames[1], Animation.PlayMode.NORMAL, 4)
        self.store_animation("crouch_light_kick", crouch_light_kick_animation)
        crouch_light_kick_animationR = spritesheet.get_animation(self.crouchLightKickFrames[0], self.crouchLightKickFrames[1], Animation.PlayMode.NORMAL, 4, True)
        self.store_animation("crouch_light_kickR", crouch_light_kick_animationR)
        
        #crouch medium kick animation
        crouch_medium_kick_animation = spritesheet.get_animation(self.crouchMediumKickFrames[0], self.crouchMediumKickFrames[1], Animation.PlayMode.NORMAL, 4)
        self.store_animation("crouch_medium_kick", crouch_medium_kick_animation)
        crouch_medium_kick_animationR = spritesheet.get_animation(self.crouchMediumKickFrames[0], self.crouchMediumKickFrames[1], Animation.PlayMode.NORMAL, 4, True)
        self.store_animation("crouch_medium_kickR", crouch_medium_kick_animationR)
        
        #crouch heavy kick animation
        crouch_heavy_kick_animation = spritesheet.get_animation(self.crouchHeavyKickFrames[0], self.crouchHeavyKickFrames[1], Animation.PlayMode.NORMAL, 4)
        self.store_animation("crouch_heavy_kick", crouch_heavy_kick_animation)
        crouch_heavy_kick_animationR = spritesheet.get_animation(self.crouchHeavyKickFrames[0], self.crouchHeavyKickFrames[1], Animation.PlayMode.NORMAL, 4, True)
        self.store_animation("crouch_heavy_kickR", crouch_heavy_kick_animationR)
        
        #jump light punch animation
        jump_light_punch_animation = spritesheet.get_animation(self.jumpLightPunchFrames[0], self.jumpLightPunchFrames[1], Animation.PlayMode.NORMAL, 4)
        self.store_animation("jump_light_punch", jump_light_punch_animation)
        jump_light_punch_animationR = spritesheet.get_animation(self.jumpLightPunchFrames[0], self.jumpLightPunchFrames[1], Animation.PlayMode.NORMAL, 4, True)
        self.store_animation("jump_light_punchR", jump_light_punch_animationR)
        
        #jump medium punch animation
        jump_medium_punch_animation = spritesheet.get_animation(self.jumpMediumPunchFrames[0], self.jumpMediumPunchFrames[1], Animation.PlayMode.NORMAL, 4)
        self.store_animation("jump_medium_punch", jump_medium_punch_animation)
        jump_medium_punch_animationR = spritesheet.get_animation(self.jumpMediumPunchFrames[0], self.jumpMediumPunchFrames[1], Animation.PlayMode.NORMAL, 4, True)
        self.store_animation("jump_medium_punchR", jump_medium_punch_animationR)
        
        #jump heavy punch animation
        jump_heavy_punch_animation = spritesheet.get_animation(self.jumpHeavyPunchFrames[0], self.jumpHeavyPunchFrames[1], Animation.PlayMode.NORMAL, 4)
        self.store_animation("jump_heavy_punch", jump_heavy_punch_animation)
        jump_heavy_punch_animationR = spritesheet.get_animation(self.jumpHeavyPunchFrames[0], self.jumpHeavyPunchFrames[1], Animation.PlayMode.NORMAL, 4, True)
        self.store_animation("jump_heavy_punchR", jump_heavy_punch_animationR)
        
        #jump light kick animation
        jump_light_kick_animation = spritesheet.get_animation(self.jumpLightKickFrames[0], self.jumpLightKickFrames[1], Animation.PlayMode.NORMAL, 4)
        self.store_animation("jump_light_kick", jump_light_kick_animation)
        jump_light_kick_animationR = spritesheet.get_animation(self.jumpLightKickFrames[0], self.jumpLightKickFrames[1], Animation.PlayMode.NORMAL, 4, True)
        self.store_animation("jump_light_kickR", jump_light_kick_animationR)
        
        #jump medium kick animation
        jump_medium_kick_animation = spritesheet.get_animation(self.jumpMediumKickFrames[0], self.jumpMediumKickFrames[1], Animation.PlayMode.NORMAL, 4)
        self.store_animation("jump_medium_kick", jump_medium_kick_animation)
        jump_medium_kick_animationR = spritesheet.get_animation(self.jumpMediumKickFrames[0], self.jumpMediumKickFrames[1], Animation.PlayMode.NORMAL, 4, True)
        self.store_animation("jump_medium_kickR", jump_medium_kick_animationR)
        
        #jump heavy kick animation
        jump_heavy_kick_animation = spritesheet.get_animation(self.jumpHeavyKickFrames[0], self.jumpHeavyKickFrames[1], Animation.PlayMode.NORMAL, 4)
        self.store_animation("jump_heavy_kick", jump_heavy_kick_animation)
        jump_heavy_kick_animationR = spritesheet.get_animation(self.jumpHeavyKickFrames[0], self.jumpHeavyKickFrames[1], Animation.PlayMode.NORMAL, 4, True)    
        self.store_animation("jump_heavy_kickR", jump_heavy_kick_animationR)
        
        #diagonal jump light punch animation
        diagonal_jump_light_punch_animation = spritesheet.get_animation(self.diagonalJumpLightPunchFrames[0], self.diagonalJumpLightPunchFrames[1], Animation.PlayMode.NORMAL, 4)
        self.store_animation("diagonal_jump_light_punch", diagonal_jump_light_punch_animation)
        diagonal_jump_light_punch_animationR = spritesheet.get_animation(self.diagonalJumpLightPunchFrames[0], self.diagonalJumpLightPunchFrames[1], Animation.PlayMode.NORMAL, 4, True)
        self.store_animation("diagonal_jump_light_punchR", diagonal_jump_light_punch_animationR)
        
        #diagonal jump medium punch animation
        diagonal_jump_medium_punch_animation = spritesheet.get_animation(self.diagonalJumpMediumPunchFrames[0], self.diagonalJumpMediumPunchFrames[1], Animation.PlayMode.NORMAL, 4)
        self.store_animation("diagonal_jump_medium_punch", diagonal_jump_medium_punch_animation)
        diagonal_jump_medium_punch_animationR = spritesheet.get_animation(self.diagonalJumpMediumPunchFrames[0], self.diagonalJumpMediumPunchFrames[1], Animation.PlayMode.NORMAL, 4, True)
        self.store_animation("diagonal_jump_medium_punchR", diagonal_jump_medium_punch_animationR)
        
        #diagonal jump heavy punch animation
        diagonal_jump_heavy_punch_animation = spritesheet.get_animation(self.diagonalJumpHeavyPunchFrames[0], self.diagonalJumpHeavyPunchFrames[1], Animation.PlayMode.NORMAL, 4)
        self.store_animation("diagonal_jump_heavy_punch", diagonal_jump_heavy_punch_animation)
        diagonal_jump_heavy_punch_animationR = spritesheet.get_animation(self.diagonalJumpHeavyPunchFrames[0], self.diagonalJumpHeavyPunchFrames[1], Animation.PlayMode.NORMAL, 4, True)
        self.store_animation("diagonal_jump_heavy_punchR", diagonal_jump_heavy_punch_animationR)
        
        #diagonal jump light kick animation
        diagonal_jump_light_kick_animation = spritesheet.get_animation(self.diagonalJumpLightKickFrames[0], self.diagonalJumpLightKickFrames[1], Animation.PlayMode.NORMAL, 4)
        self.store_animation("diagonal_jump_light_kick", diagonal_jump_light_kick_animation)
        diagonal_jump_light_kick_animationR = spritesheet.get_animation(self.diagonalJumpLightKickFrames[0], self.diagonalJumpLightKickFrames[1], Animation.PlayMode.NORMAL, 4, True)
        self.store_animation("diagonal_jump_light_kickR", diagonal_jump_light_kick_animationR)
        
        #diagonal jump medium kick animation
        diagonal_jump_medium_kick_animation = spritesheet.get_animation(self.diagonalJumpMediumKickFrames[0], self.diagonalJumpMediumKickFrames[1], Animation.PlayMode.NORMAL, 4)
        self.store_animation("diagonal_jump_medium_kick", diagonal_jump_medium_kick_animation)
        diagonal_jump_medium_kick_animationR = spritesheet.get_animation(self.diagonalJumpMediumKickFrames[0], self.diagonalJumpMediumKickFrames[1], Animation.PlayMode.NORMAL, 4, True)
        self.store_animation("diagonal_jump_medium_kickR", diagonal_jump_medium_kick_animationR)
        
        #diagonal jump heavy kick animation
        diagonal_jump_heavy_kick_animation = spritesheet.get_animation(self.diagonalJumpHeavyKickFrames[0], self.diagonalJumpHeavyKickFrames[1], Animation.PlayMode.NORMAL, 4)
        self.store_animation("diagonal_jump_heavy_kick", diagonal_jump_heavy_kick_animation)
        diagonal_jump_heavy_kick_animationR = spritesheet.get_animation(self.diagonalJumpHeavyKickFrames[0], self.diagonalJumpHeavyKickFrames[1], Animation.PlayMode.NORMAL, 4, True)    
        self.store_animation("diagonal_jump_heavy_kickR", diagonal_jump_heavy_kick_animationR)
        
    def directionUpdate(self):
        if self.pos.x > self.opponent.pos.x:
            self.direction = "left"
        else:
            self.direction = "right"

                                
    def apply_gravity(self):
        if not self.pos.y == STAGE_FLOOR:
            self.vel.y += GRAVITY
            self.vel.y = min(self.vel.y, MAX_FALL_SPEED)  
            
    def handle_states(self):
        keys = pg.key.get_pressed()
        current_state = update_state(self, keys, self.direction, self.playerNum, self.state, self.mode)
        if current_state == STATE_IDLE:
            self.state = STATE_IDLE
            state_idle(self, self.state)
            self.attackStruck = False
        elif "WAIT" in current_state:
            self.state = current_state
            state_wait(self, self.state)
        elif current_state == STATE_WALK or current_state == STATE_BACKWALK:
            self.state = current_state
            state_walk(self, self.state)
        elif current_state == STATE_JUMP or current_state == STATE_FORWARD_STRAFE or current_state == STATE_BACKWARD_STRAFE:
            self.state = current_state
            state_jump(self, self.state)
        elif current_state == STATE_FORWARD_JUMP or current_state == STATE_BACKWARD_JUMP:
            self.state = current_state
            state_directional_jump(self, self.state)
        elif current_state == STATE_CROUCH:
            self.state = STATE_CROUCH
            state_crouch(self, self.state)
            self.attackStruck = False
        elif "PUNCH" in current_state:
            self.state = current_state
            state_punch(self, self.state)
        elif "KICK" in current_state:
            self.state = current_state
            state_kick(self, self.state)
        else:
            pass
            
    def animate(self):
        self.image = self.active_anim.get_frame(self.elapsed_time)
        self.rect = self.image.get_rect()

    def updatePushboxPosition(self):
        if "CROUCH" in self.state:
            self.pushbox = pg.Rect((self.pos.x - self.pushbox_list["crouch"]["width"] // 2) + self.pushbox_list["crouch"]["x-offset"], self.pos.y - self.pushbox_list["crouch"]["height"] + self.pushbox_list["crouch"]["y-offset"], self.pushbox_list["crouch"]["width"], self.pushbox_list["crouch"]["height"])
        else:
            self.pushbox = pg.Rect((self.pos.x - self.pushbox_list["default"]["width"] // 2) + self.pushbox_list["default"]["x-offset"], self.pos.y - self.pushbox_list["default"]["height"] + self.pushbox_list["default"]["y-offset"], self.pushbox_list["default"]["width"], self.pushbox_list["default"]["height"])
    
    def handle_pushbox_collision(self):
        # Check for pushbox collisions with opponent's pushbox
        if self.opponent is not None:
            if self.pushbox.colliderect(self.opponent.pushbox):
                if self.direction == "right":
                    self.pos.x = self.opponent.pushbox.left - self.pushbox.width // 2
                else:
                    self.pos.x = self.opponent.pushbox.right + self.pushbox.width // 2
                    
    def updateHurtboxes(self):
        if "R" not in self.active_name:
            name = self.active_name
        else:
            name = self.active_name.replace("R","")
            
        index = self.active_anim.get_frame_index(self.elapsed_time)
        
        if name in self.hurtbox_list.keys():
            headRect = pg.Rect(0,0,self.hurtbox_list[name][index]["head"][2],self.hurtbox_list[name][index]["head"][3])
            bodyRect = pg.Rect(0,0,self.hurtbox_list[name][index]["body"][2],self.hurtbox_list[name][index]["body"][3])
            legsRect = pg.Rect(0,0,self.hurtbox_list[name][index]["legs"][2],self.hurtbox_list[name][index]["legs"][3])
            
            if self.direction == "right":
                headRect.topleft = self.rect.topleft + vec(self.hurtbox_list[name][index]["head"][0],self.hurtbox_list[name][index]["head"][1])
                bodyRect.topleft = self.rect.topleft + vec(self.hurtbox_list[name][index]["body"][0],self.hurtbox_list[name][index]["body"][1])
                legsRect.topleft = self.rect.topleft + vec(self.hurtbox_list[name][index]["legs"][0],self.hurtbox_list[name][index]["legs"][1])
            else:
                headRect.topright = self.rect.topright - vec(self.hurtbox_list[name][index]["head"][0],0) + vec(0,self.hurtbox_list[name][index]["head"][1])
                bodyRect.topright = self.rect.topright - vec(self.hurtbox_list[name][index]["body"][0],0) + vec(0,self.hurtbox_list[name][index]["body"][1])
                legsRect.topright = self.rect.topright - vec(self.hurtbox_list[name][index]["legs"][0],0) + vec(0,self.hurtbox_list[name][index]["legs"][1])
                
            self.hurtboxes["head"] = headRect
            self.hurtboxes["body"] = bodyRect
            self.hurtboxes["legs"] = legsRect
        
    def updateHitbox(self):
        if not self.is_attacking():
            self.hitbox = None
            return
        
        if "R" not in self.active_name:
            name = self.active_name
        else:
            name = self.active_name.replace("R","")
        
        index = self.active_anim.get_frame_index(self.elapsed_time)
        
        if name in self.hitbox_list.keys() and index in self.hitbox_list[name]:
            hitboxRect = pg.Rect(0,0,self.hitbox_list[name][index][2],self.hitbox_list[name][index][3])
            if self.direction == "right":
                hitboxRect.topleft = self.rect.topleft + vec(self.hitbox_list[name][index][0],self.hitbox_list[name][index][1])
            else:
                hitboxRect.topright = self.rect.topright - vec(self.hitbox_list[name][index][0],0) + vec(0,self.hitbox_list[name][index][1])
                
            self.hitbox = hitboxRect
        else:
            self.hitbox = None
            
    def attackBoxCollisionDetection(self):
        if not self.is_attacking() or self.hitbox is None or self.hurtboxes["head"] is None or self.hurtboxes["body"] is None or self.hurtboxes["legs"] is None or self.attackStruck:
            return

        if "R" not in self.active_name:
            name = self.active_name
        else:
            name = self.active_name.replace("R","")
            
        if name in self.hitbox_list.keys():
            points = self.hitbox_list[name]["points"]
            damage = self.hitbox_list[name]["damage"]
            if "light" in name:
                strength = "light"
            elif "medium" in name:
                strength = "medium"
            elif "heavy" in name:
                strength = "heavy"

        hurtbox_order = ["legs", "head", "body"]

        bodyPart = ""
        collided_hurtbox = None

        # Loop through the hurtboxes in the specified order
        for part in hurtbox_order:
            if self.hitbox.colliderect(self.opponent.hurtboxes[part]):
                bodyPart = part
                collided_hurtbox = self.opponent.hurtboxes[part]
                self.attackStruck = True
                break

        if collided_hurtbox is not None:
            gameState[self.playerNum]["score"] += points
            gameState[self.opponent.playerNum]["health"] -= damage
            x = (self.hitbox.centerx + collided_hurtbox.centerx) // 2
            y = (self.hitbox.centery + collided_hurtbox.centery) // 2
            self.fightScene.handle_hit_splash(x,y,self.playerNum, strength)
            print(self.name + " hit " + self.opponent.name + "'s " + bodyPart)
                  
    def is_attacking(self):
        if "PUNCH" in self.state or "KICK" in self.state:
            return True
        return False
        
    def update(self):
        super().update(1/FPS)
        self.directionUpdate()
        self.handle_states()
        self.animate()
        
        # apply gravity
        self.apply_gravity()
        
        # Update the sprite's position
        self.pos += self.vel

        # Check for collision with the left and right edges of the screen
        if self.pos.x - self.rect.width / 2 < 0:
            self.pos.x = self.rect.width / 2

        elif self.pos.x + self.rect.width / 2 > WIDTH:
            self.pos.x = WIDTH - self.rect.width / 2


        # Check for collision with the stage floor
        if self.pos.y >= STAGE_FLOOR:
            self.pos.y = STAGE_FLOOR
            self.vel.y = 0
          
        # Update the sprite's rect position
        self.rect.midbottom = self.pos
        
        #Update pushbox position
        self.updatePushboxPosition()
        
        #handle pushbox collision
        self.handle_pushbox_collision()
    