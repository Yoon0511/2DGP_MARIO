from pico2d import *
import GM
import game_framework

PIXEL_PER_METER = (10.0 / 0.5)  # 10 pixel 50 cm
COIN_MOVE_SPEED_KMPH = 30.0  # Km / Hour
COIN_MOVE_SPEED_MPM = (COIN_MOVE_SPEED_KMPH * 1000.0 / 60.0)
COIN_MOVE_SPEED_MPS = (COIN_MOVE_SPEED_MPM / 60.0)
COIN_MOVE_SPEED_PPS = (COIN_MOVE_SPEED_MPS * PIXEL_PER_METER)

MUSH_MOVE_SPEED_KMPH = 20.0  # Km / Hour
MUSH_MOVE_SPEED_MPM = (MUSH_MOVE_SPEED_KMPH * 1000.0 / 60.0)
MUSH_MOVE_SPEED_MPS = (MUSH_MOVE_SPEED_MPM / 60.0)
MUSH_MOVE_SPEED_PPS = (MUSH_MOVE_SPEED_MPS * PIXEL_PER_METER)

COIN_TIME_PER_ACTION = 0.6
COIN_ACTION_PER_TIME = 1.0 / COIN_TIME_PER_ACTION
COIN_FRAMES_PER_ACTION = 4

FLOWER_TIME_PER_ACTION = 0.9
FLOWER_ACTION_PER_TIME = 1.0 / FLOWER_TIME_PER_ACTION
FLOWER_FRAMES_PER_ACTION = 4

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

        self.frame += (COIN_FRAMES_PER_ACTION * COIN_ACTION_PER_TIME * game_framework.frame_time) % 4
        self.y += COIN_MOVE_SPEED_PPS * game_framework.frame_time

        if self.frame >= 3:
            GM.remove_object(self)

    def draw(self):
        Coin.coin.clip_draw(int(self.frame) * 60, 0, 60, 60, self.x, self.y)

class Flower:
    flower = None
    def __init__(self):
        if Flower.flower == None:
            Flower.flower = load_image('flower.png')
        self.x,self.y = 0,0
        self.frame = 0

    def get_bb(self):
        return self.x - 25, self.y + 25, self.x + 25, self.y - 25

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
        self.frame += (FLOWER_FRAMES_PER_ACTION * FLOWER_ACTION_PER_TIME * game_framework.frame_time)
        self.frame = self.frame % 4

        self.to_mario_collision()

    def draw(self):
        Flower.flower.clip_draw(int(self.frame) * 50, 0, 50, 50, self.x, self.y)

    def to_mario_collision(self):
        mleft, mtop, mright, mbottom = GM.my_mario.get_bb()
        ileft, itop, iright, ibottom = self.get_bb()

        if mleft > iright: return False
        if mright < ileft: return False
        if mtop < ibottom: return False
        if mbottom > itop: return False

        GM.SCORE += 50
        GM.remove_object(self)
        if GM.my_mario.level < 2:
            GM.sound.play_level_up_bgm(30)
            GM.my_mario.level = 2
            GM.my_mario.set_addpos(0,50)
            GM.my_mario.height = 70

class Mush:
    image = None

    def __init__(self):
        if Mush.image == None:
            Mush.image = load_image('upmush.png')
        self.x,self.y = 0,0
        self.drop = False
        self.dropSpeed = 0
        self.gravity = -12.8
        self.accel = 0
        self.dir = 0

    def add_pos(self,x,y):
        self.x += x
        self.y += y

    def set_pos(self,x,y):
        self.x,self.y = x,y

    def get_bb(self):
        return self.x - 25, self.y + 25, self.x + 25, self.y - 25

    def get_pos(self):
        return self.x,self.y

    def chage_dir(self,dir):
        self.dir = dir

    def enter(self):
        pass

    def exit(self):
        pass

    def update(self):
        self.add_pos(-GM.OFFSET_GAP, 0)

        if self.dir == 0:  # 왼쪽
            self.x -= MUSH_MOVE_SPEED_PPS * game_framework.frame_time
        elif self.dir == 1:  # 오른쪽
            self.x += MUSH_MOVE_SPEED_PPS * game_framework.frame_time

        if self.drop == True:
            self.dropSpeed += self.accel
            self.accel += self.gravity * game_framework.frame_time
            if self.accel <= -300:
                self.accel = -300

        self.y += self.dropSpeed * game_framework.frame_time

        self.to_mario_collision()

    def draw(self):
        Mush.image.clip_draw(0, 0, 50, 50, self.x, self.y)

    def to_mario_collision(self):
        mleft, mtop, mright, mbottom = GM.my_mario.get_bb()
        ileft, itop, iright, ibottom = self.get_bb()

        if mleft > iright: return False
        if mright < ileft: return False
        if mtop < ibottom: return False
        if mbottom > itop: return False

        GM.SCORE += 100
        GM.remove_object(self)
        if GM.my_mario.level == 0:
            GM.sound.play_level_up_bgm(30)
            GM.my_mario.level = 1
            GM.my_mario.set_addpos(0,20)
            GM.my_mario.height = 70


    def Collsion_block(self,block):
        eleft, etop, eright, ebottom = self.get_bb()
        bleft, btop, bright, bbottom = block.get_bb()

        if ebottom - 50 > btop:
            self.drop = True
            return
        if eleft - 50 > bright : return
        if eright + 50 < bleft: return
        if etop + 50 < bbottom: return


        if ebottom > btop:
            self.drop = True
            return
        if eleft > bright: return
        if eright < bleft: return
        if etop < bbottom: return


        mx, my = self.get_pos()
        bx, by = block.get_pos()
        l, r, b, t = False, False, False, False

        gapx, gapy = 0, 0
        # enemy 기준충돌위치
        if mx >= bx:  # 왼쪽충돌 +
            gapx = bright - eleft
            l = True
        elif mx <= bx:  # 오른쪽충돌 -
            gapx = eright - bleft
            r = True
        if my >= by:  # 아래 충돌 +
            gapy = btop - ebottom
            b = True
        elif my <= by:  # 위 충돌 -
            gapy = etop - bbottom
            t = True

        if gapx > gapy:
            if b == True:
                # mario.set_addpos(0,gapy + 0.01)
                if self.drop == True:
                    self.add_pos(0, gapy)
                    self.dropSpeed = 0
                    self.accel = 0
                    self.drop = False
        else:
            if not block.get_type() == '1':
                if l == True:
                    self.add_pos(gapx + 0.01, 0)
                    self.chage_dir(1)
                if r == True:
                    self.add_pos(-gapx - 0.01, 0)
                    self.chage_dir(0)