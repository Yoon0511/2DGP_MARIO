from pico2d import *
import GM
import game_framework

PIXEL_PER_METER = (10.0 / 0.5)  # 10 pixel 30 cm
MOVE_SPEED_KMPH = 30.0  # Km / Hour
MOVE_SPEED_MPM = (MOVE_SPEED_KMPH * 1000.0 / 60.0)
MOVE_SPEED_MPS = (MOVE_SPEED_MPM / 60.0)
MOVE_SPEED_PPS = (MOVE_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.6
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4
class Item:
    coin = None
    def __init__(self):
        if Item.coin == None:
            Item.coin = load_image('coin.png')
        self.x,self.y = 0,0
        self.frame = 0

    def set_pos(self,x,y):
        self.x,self.y = x,y

    def enter(self):
        pass

    def exit(self):
        pass

    def update(self):
        self.frame += (FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        self.y += MOVE_SPEED_PPS * game_framework.frame_time

        if self.frame >= 3:
            GM.remove_object(self)
    def draw(self):
        Item.coin.clip_draw(int(self.frame) * 60, 0, 60, 60, self.x, self.y)