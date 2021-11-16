from pico2d import *
import GM
import game_framework

PIXEL_PER_METER = (10.0 / 0.5)  # 10 pixel 50 cm
COIN_MOVE_SPEED_KMPH = 30.0  # Km / Hour
COIN_MOVE_SPEED_MPM = (COIN_MOVE_SPEED_KMPH * 1000.0 / 60.0)
COIN_MOVE_SPEED_MPS = (COIN_MOVE_SPEED_MPM / 60.0)
COIN_MOVE_SPEED_PPS = (COIN_MOVE_SPEED_MPS * PIXEL_PER_METER)

MUSH_MOVE_SPEED_KMPH = 10.0  # Km / Hour
MUSH_MOVE_SPEED_MPM = (MUSH_MOVE_SPEED_KMPH * 1000.0 / 60.0)
MUSH_MOVE_SPEED_MPS = (MUSH_MOVE_SPEED_MPM / 60.0)
MUSH_MOVE_SPEED_PPS = (MUSH_MOVE_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.6
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4
class Coin:
    coin = None
    def __init__(self):
        if Coin.coin == None:
            Coin.coin = load_image('coin.png')
        self.x,self.y = 0,0
        self.frame = 0

    def add_pos(self,x,y):
        self.x += x
        self.y += y

    def set_pos(self,x,y):
        self.x,self.y = x,y

    def enter(self):
        pass

    def exit(self):
        pass

    def update(self):
        self.add_pos(-GM.OFFSET_GAP, 0)

        self.frame += (FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        self.y += COIN_MOVE_SPEED_PPS * game_framework.frame_time

        if self.frame >= 3:
            GM.remove_object(self)

    def draw(self):
        Coin.coin.clip_draw(int(self.frame) * 60, 0, 60, 60, self.x, self.y)

class Mush:
    image = None

    def __init__(self):
        if Mush.image == None:
            Mush.image = load_image('upmush.png')
        self.x,self.y = 0,0

    def add_pos(self,x,y):
        self.x += x
        self.y += y

    def set_pos(self,x,y):
        self.x,self.y = x,y

    def get_bb(self):
        return self.x - 25, self.y + 25, self.x + 25, self.y - 25

    def enter(self):
        pass

    def exit(self):
        pass

    def update(self):
        self.add_pos(-GM.OFFSET_GAP, 0)

        self.collision()

    def draw(self):
        Mush.image.clip_draw(0, 0, 50, 50, self.x, self.y)

    def collision(self):
        mleft, mtop, mright, mbottom = GM.my_mario.get_bb()
        ileft, itop, iright, ibottom = self.get_bb()

        if mleft > iright: return False
        if mright < ileft: return False
        if mtop < ibottom: return False
        if mbottom > itop: return False

        GM.remove_object(self)