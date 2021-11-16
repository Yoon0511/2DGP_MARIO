from pico2d import *
import random
import game_framework
import GM
import Map

PIXEL_PER_METER = (10.0 / 0.5)  # 10 pixel 50 cm
MOVE_SPEED_KMPH = 15.0  # Km / Hour
MOVE_SPEED_MPM = (MOVE_SPEED_KMPH * 1000.0 / 60.0)
MOVE_SPEED_MPS = (MOVE_SPEED_MPM / 60.0)
MOVE_SPEED_PPS = (MOVE_SPEED_MPS * PIXEL_PER_METER)
#굼바, 거북이 클래스
class Enemy:
    def __init__(self):
        self.x,self.y = 0,0
        self.type = 'G'
        self.Gumbaimg = load_image('Gumba.png')
        self.Turtleimg = load_image('turtle.png')
        self.GDIE = load_image('G_DIE.png')
        #self.dir = random.randint(0,1)
        self.dir = 0
        self.movespeed = 100
        self.weith,self.height = 50,50
        self.drop = False
        self.dropSpeed = 0
        self.gravity = -12.8
        self.frametime = 0
        self.accel = 0
        self.state = 'LIVE'
        self.timer = 0

    def move(self):
        pass

    def set_state(self,state):
        self.state = state

    def get_pos(self):
        return self.x,self.y

    def add_pos(self,x,y):
        self.x += x
        self.y += y

    def set_pos(self,x,y,type):
        self.x = x
        self.y = y
        self.type = type

    def get_bb(self):
        return self.x - 25, self.y + 25, self.x + 25, self.y - 25

    def chage_dir(self,dir):
        self.dir = dir

    def update(self):
        self.add_pos(-GM.OFFSET_GAP, 0)
        if self.x <= -100:
            GM.remove_object(self)

        if self.x > GM.GAME_WIDTH: return

        if self.dir == 0:  # 왼쪽
            self.x -= MOVE_SPEED_PPS * game_framework.frame_time
        elif self.dir == 1:  # 오른쪽
            self.x += MOVE_SPEED_PPS * game_framework.frame_time

        if self.drop == True:
            self.dropSpeed += self.accel
            self.accel += self.gravity * game_framework.frame_time
            if self.accel <= -300:
                self.accel = -300

        self.y += self.dropSpeed * game_framework.frame_time

    def draw(self):
        if self.type == 'G':
            if self.state == 'LIVE':
                self.Gumbaimg.draw(self.x,self.y)
            elif self.state == 'DIE':
                self.Gumbaimg.clip_composite_draw(0, 0, 50, 50, 3.141592, '', self.x, self.y, 50, 50)
        if self.type == 'T':
            if self.state == 'LIVE':
                if self.dir == 0: # 왼쪽
                    self.Turtleimg.clip_draw(0,0,self.weith,self.height,self.x,self.y)
                elif self.dir == 1: # 오른쪽
                    self.Turtleimg.clip_draw(self.weith,0,self.weith,self.height,self.x,self.y)
            elif self.state == 'DIE':
                if self.dir == 0: # 왼쪽
                    self.Turtleimg.clip_composite_draw(0, 0, 50, 50, 3.141592, 'h', self.x, self.y, 50, 50)
                elif self.dir == 1: # 오른쪽
                    self.Turtleimg.clip_composite_draw(0, 0, 50, 50, 3.141592, '', self.x, self.y, 50, 50)

        #eleft, etop, eright, ebottom = self.get_bb()
        #draw_rectangle(*self.get_bb())
        #draw_rectangle(eleft - 50,ebottom - 50,eright + 50,etop + 50)

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