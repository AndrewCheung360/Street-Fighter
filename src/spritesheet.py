import pygame as pg
from enum import Enum

class SpriteSheet:
    def __init__(self, filename, bg=None):
        self.spritesheet = pg.image.load(filename).convert_alpha()
        self.bg = bg
        
    def get_image(self, frame, scale = None, flip=False):
        x = frame[0]
        y = frame[1]
        width = frame[2]
        height = frame[3]
        
        image = pg.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        
        if scale is not None: 
            image = pg.transform.scale(image, (width*scale, height*scale))
        
        if self.bg is not None:
            image.set_colorkey(self.bg)
            
        if flip:
            image = pg.transform.flip(image, True, False)
            
        return image
    
    def get_animation(self, coords, frame_durations, mode, scale=None, flip=None):
		# extract images & create animation
        frames = [self.get_image(frame, scale, flip) for frame in coords]
        return Animation(frames, frame_durations, mode)

    
class Animation:
    class PlayMode(Enum):
            NORMAL = 1,
            LOOP = 2

    def __init__(self, frames, frame_durations, mode):
        if len(frames) != len(frame_durations):
            raise ValueError("Number of frames and frame_durations should be the same")
        # animation settings
        self.frames = frames
        self.frame_durations = frame_durations
        self.animation_duration = sum(frame_durations)
        self.mode = mode

    def get_frame(self, state_time):
        frame_number = self.get_frame_index(state_time)
        return self.frames[frame_number]

    
    def get_frame_index(self, state_time):
        if len(self.frames) == 1:
            return 0

        total_duration = 0
        for i, duration in enumerate(self.frame_durations):
            total_duration += duration
            if state_time < total_duration:
                return i

        if self.mode == self.PlayMode.NORMAL:
            return len(self.frames) - 1

        return int((state_time % self.animation_duration) / self.animation_duration * len(self.frames))

    def is_animation_finished(self, state_time):
        return state_time >= self.animation_duration