from pico2d import *
#굼바, 거북이 클래스
class Enemy:
    def __init__(self):
        self.x,self.y = 0,0
        self.type = 'G'
        self.Gumbaimg = load_image('Gumba.png')
        self.Turtleimg = load_image('turtle.png')
        self.dir = 0
        self.movespeed = 100
        self.weith,self.height = 50,50
        self.drop = False
        self.dropSpeed = 0
        self.gravity = -8.8
        self.frametime = 0

    def move(self):
        pass


    def get_pos(self):
        return self.x,self.y

    def set_addpos(self,x,y):
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

    def update(self,frame_time):
        if self.dir == 0:  # 왼쪽
            self.x -= self.movespeed * frame_time
        elif self.dir == 1:  # 오른쪽
            self.x += self.movespeed * frame_time

        if self.drop == True:
            self.dropSpeed += self.gravity

        self.y += self.dropSpeed * frame_time

    def draw(self):
        if self.type == 'G':
            self.Gumbaimg.draw(self.x,self.y)
        if self.type == 'T':
            if self.dir == 0: # 왼쪽
                self.Turtleimg.clip_draw(0,0,self.weith,self.height,self.x,self.y)
            elif self.dir == 1: # 오른쪽
                self.Turtleimg.clip_draw(self.weith,0,self.weith,self.height,self.x,self.y)

    def Collsion_block(self,block):
        eleft, etop, eright, ebottom = self.get_bb()
        isskyblock = True
        bleft, btop, bright, bbottom = block.get_bb()
        if eleft <= bright and etop >= bbottom and eright >= bleft and ebottom <= btop:
            mx, my = self.get_pos()
            bx, by = block.get_pos()
            l, r, b, t = False, False, False, False

            gapx, gapy = 0, 0
            # 마리오 기준충돌위치
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
                if not block.get_type() == '0':  # 하늘이 아닌 모든 블록
                    isskyblock = False
                    if b == True:
                        # mario.set_addpos(0,gapy + 0.01)
                        if self.drop == True:
                            self.set_addpos(0, gapy)
                            self.dropSpeed = 0
                            self.drop = False
                    if t == True:
                        self.dropSpeed = 0
                        self.drop = False
                        self.set_addpos(0, -gapy)
                if block.get_type() == '0' and isskyblock == True:  # 하늘블록처리 enemy 발밑이 하늘블록일때
                    if b == True:
                        self.drop = True
            else:
                if not block.get_type() == '0' and not block.get_type() == '1':
                    if l == True:
                        self.set_addpos(gapx + 0.01, 0)
                        self.chage_dir(1)
                    if r == True:
                        self.set_addpos(-gapx - 0.01, 0)
                        self.chage_dir(0)