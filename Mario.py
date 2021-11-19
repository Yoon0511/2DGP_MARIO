from pico2d import *
import GM
import game_framework
# 마리오 클래스 점프관련 수정필요
class mario :
    TIME_PER_ACTION = 0.1
    ACTION_PER_TIME = 0.3 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4
    total_frames = 0.0

    def __init__(self):
        self.x,self.y = 100,125
        self.state = {'IDLE':True,'WALK':False,'JUMP':False}
        self.presskey = {'LEFT':False,'RIGHT':False}
        self.speed = 250
        self.frame = 0
        #self.img = load_image('mario.png')
        self.img = load_image('m1.png')
        self.img_man = load_image('mario_man.png')
        self.level = 0
        self.walk_frame = 0
        self.idle_frame = 0
        self.jump = True
        self.dropSpeed = 0
        self.dir = 0
        self.weith,self.height = 50,50
        self.jump_power,self.gravity = 500,-12.8
        self.accel = 0
        self.jump_time = 1.5
        self.prev_collision = False
        self.now_collision = False

    def get_pos(self):
        return self.x,self.y

    def get_bb(self):
        if self.level == 0:
            return self.x - 25,self.y + 25,self.x + 25,self.y - 25
        else:
            return self.x - 25, self.y + 35, self.x + 25, self.y - 35

    def get_foot_bb(self):
        if self.level == 0:
            return self.x - 20,self.y-24,self.x+20,self.y-25
        else:
            return self.x - 20, self.y - 34, self.x + 20, self.y - 34

    def set_addpos(self,x,y):
        self.x += x
        self.y += y

    def set_pos(self,x,y):
        self.x,self.y = x,y

    def get_check_state(self,state):
        return self.state[state]

    def draw_walk(self):
        if self.level == 0:
            if self.dir == 0:
                self.img.clip_draw(self.walk_frame * self.weith,0,self.weith,self.height,self.x,self.y)
            elif self.dir == 1:
                self.img.clip_draw(self.walk_frame * self.weith,self.height,self.weith,self.height,self.x,self.y)
        if self.level == 1:
            if self.dir == 0:
                self.img_man.clip_draw(self.walk_frame * self.weith,0,self.weith,self.height + 20,self.x,self.y)
            elif self.dir == 1:
                self.img_man.clip_draw(self.walk_frame * self.weith,self.height + 20,self.weith,self.height + 20,self.x,self.y)

    def draw_idle(self):
        if self.level == 0:
            if self.dir == 0:
                self.img.clip_draw(0,0,self.weith,self.height,self.x,self.y)
            elif self.dir == 1:
                self.img.clip_draw(0,self.height,self.weith,self.height,self.x,self.y)
        if self.level == 1:
            if self.dir == 0:
                self.img_man.clip_draw(0,0,self.weith,self.height + 20,self.x,self.y)
            elif self.dir == 1:
                self.img_man.clip_draw(0,self.height + 20,self.weith,self.height + 20,self.x,self.y)

    def draw_jump(self):
        if self.level == 0:
            if self.dir == 0:
                self.img.clip_draw(50, 0, 50, 50, self.x, self.y)
            elif self.dir == 1:
                self.img.clip_draw(50, 50, 50, 50, self.x, self.y)
        if self.level == 1:
            if self.dir == 0:
                self.img_man.clip_draw(50,0,self.weith,self.height + 20,self.x,self.y)
            elif self.dir == 1:
                self.img_man.clip_draw(50,self.height + 20,self.weith,self.height + 20,self.x,self.y)

    def handle_events(self,get_events):
        events = get_events
        for event in events:
            if event.type == SDL_QUIT:
               GM.running = False
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
               GM.running = False

            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_d:
                    self.dir = 0
                    self.presskey['RIGHT'] = True
                elif event.key == SDLK_a:
                    self.dir = 1
                    self.presskey['LEFT'] = True
                elif event.key == SDLK_w:
                    if self.jump == True:
                        self.set_state(False,False,True)
                        self.dropSpeed = self.jump_power
                        #self.accel = 5
                        self.jump = False

            elif event.type == SDL_KEYUP:
                if event.key == SDLK_d:
                    self.presskey['RIGHT'] = False
                elif event.key == SDLK_a:
                    self.presskey['LEFT'] = False

    def set_state(self,idle,walk,jump):
        self.state['IDLE'] = idle
        self.state['WALK'] = walk
        self.state['JUMP'] = jump

    def enter(self):
        pass

    def exit(self):
        pass

    def update(self):
        self.total_frames += mario.FRAMES_PER_ACTION * mario.ACTION_PER_TIME * game_framework.frame_time
        #self.handle_events()

        for key,value in self.state.items():
            if key == 'WALK' and value == True:
                self.walk_frame = int(self.total_frames) % 4

        if self.presskey['RIGHT']:
            self.x += self.speed * game_framework.frame_time
            self.state['WALK'] = True
        elif self.presskey['LEFT']:
            self.x -= self.speed * game_framework.frame_time
            self.state['WALK'] = True
        else:
            if not self.state['JUMP']:
                self.set_state(True,False,False)

        #점프
        if self.jump == False:
            pass
            #hegiht = (self.jump_time * self.jump_time * (self.gravity) / 2) + (self.jump_time * 10)
            #self.set_addpos(0,hegiht)
            #self.jump_time += frame_time
            #print(self.jump_time)
            self.dropSpeed += self.accel
            self.accel += self.gravity * game_framework.frame_time
            if self.accel <= -300:
                self.accel = -300
        #중력
        # self.dropSpeed += self.accel
        # self.accel += self.gravity * game_framework.frame_time
        # if self.accel <= -150:
        #     self.accel = -150

        self.y += self.dropSpeed * game_framework.frame_time

        offsetx = GM.GAME_WIDTH / 2
        if self.x >= offsetx:
            gap = self.x - offsetx
            GM.OFFSET_GAP = gap
            self.set_addpos(-gap, 0)
        else:
            GM.OFFSET_GAP = 0

    def draw(self):
        if self.state['JUMP']:
            self.draw_jump()
        elif self.state['WALK']:
            self.draw_walk()
        elif self.state['IDLE']:
            self.draw_idle()

        draw_rectangle(*self.get_bb())
        #draw_rectangle(*self.get_foot_bb())

    def Collision_block(self,block):
        mleft, mtop, mright, mbottom = self.get_bb()
        bleft, btop, bright, bbottom = block.get_bb()

        if mleft > bright: return False
        if mright < bleft: return False
        if mtop < bbottom: return False
        if mbottom > btop: return False

        #if mleft <= bright and mtop >= bbottom and mright > bleft and mbottom < btop:
        mx, my = self.get_pos()
        bx, by = block.get_pos()
        l, r, b, t = False, False, False, False

        gapx, gapy = 0, 0
        # 마리오 기준충돌위치
        if mx > bx:  # 왼쪽충돌 +
            gapx = bright - mleft
            l = True
        elif mx < bx:  # 오른쪽충돌 -
            gapx = mright - bleft
            r = True
        if my >= by:  # 아래 충돌 +
            gapy = btop - mbottom
            b = True
        elif my <= by:  # 위 충돌 -
            gapy = mtop - bbottom
            t = True

        if gapx > gapy:
            if b == True:
                # mario.set_addpos(0,gapy + 0.01)
                if self.jump == False:
                    if self.level == 0:
                        self.set_addpos(0, gapy - 0.1)
                    else:
                        self.set_addpos(0, gapy - 1.0)

                    self.jump = True
                    self.accel = 0
                    self.dropSpeed = 0
                    print('1')
                    #self.jump_time = 1.5
                    if self.state['IDLE'] == False:
                        self.set_state(True, False, False)
            if t == True:
                block.collision_event()
                print('2')
                self.dropSpeed = 0
                self.jump = False
                self.set_addpos(0, -gapy - 0.01)
        else:
            if not block.get_type() == '1':
                if l == True:
                    self.set_addpos(gapx + 0.01, 0)
                if r == True:
                    self.set_addpos(-gapx - 0.01, 0)
        return True

    def down_mario(self):
        if self.state['JUMP']: return

        self.accel = -20
        self.jump = False

    def kill_enemy(self):
        self.dropSpeed = 0
        self.accel = -5
        self.dropSpeed = 200
        GM.SCORE += 300