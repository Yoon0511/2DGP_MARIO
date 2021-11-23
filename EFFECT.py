from pico2d import *
import GM
import game_framework

TIME_PER_ACTION = 0.4
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4

class Effect:
    img = None
    def __init__(self):
        if Effect.img == None:
            Effect.img = load_image('effect.png')
        self.x,self.y = 0,0
        self.frame = 0

    def set_pos(self,x,y):
        self.x,self.y = x,y

    def add_pos(self,x,y):
        self.x += x
        self.y += y

    def enter(self):
        pass

    def exit(self):
        pass

    def update(self):
        self.add_pos(-GM.OFFSET_GAP, 0)
        self.frame += (FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time)
        self.frame = self.frame % 4

        if self.frame >= 3:
            GM.remove_object(self)

    def draw(self):
        Effect.img.clip_draw(int(self.frame) * 50, 0, 50, 50, self.x, self.y)