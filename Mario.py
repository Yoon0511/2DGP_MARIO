from pico2d import *

import GM
from GM import running

class Mario :
    TIME_PER_ACTION = 0.01
    ACTION_PER_TIME = 0.1 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4
    total_frames = 0.0

    def __init__(self):
        self.x,self.y = 100,125
        self.state = {'IDLE':True,'WALK':False,'JUMP':False}
        self.presskey = {'LEFT':False,'RIGHT':False}
        self.speed = 3
        self.frame = 0
        #self.img = load_image('mario.png')
        self.img = load_image('m1.png')
        self.walk_frame = 0
        self.idle_frame = 0
        self.jump = True
        self.dropSpeed = 0
        self.dir = 0
        self.weith,self.height = 50,50

    def draw_walk(self):
        if self.dir == 0:
            self.img.clip_draw(self.walk_frame * self.weith,0,self.weith,self.height,self.x,self.y)
        if self.dir == 1:
            self.img.clip_draw(self.walk_frame * self.weith,self.height,self.weith,self.height,self.x,self.y)

    def draw_idle(self):
        if self.dir == 0:
            self.img.clip_draw(0,0,self.weith,self.height,self.x,self.y)
        if self.dir == 1:
            self.img.clip_draw(0,self.height,self.weith,self.height,self.x,self.y)

    def draw_jump(self):
        if self.dir == 0:
            self.img.clip_draw(50, 0, 50, 50, self.x, self.y)
        if self.dir == 1:
            self.img.clip_draw(50, 50, 50, 50, self.x, self.y)

    def now_state(self):
        return self.state

    def handle_events(self):
        events = get_events()
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
                        self.dropSpeed = 12
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

    def draw(self):
        if self.state['JUMP']:
            self.draw_jump()
        elif self.state['WALK']:
            self.draw_walk()
        elif self.state['IDLE']:
            self.draw_idle()

    def update(self,frame_time):
        self.total_frames += Mario.FRAMES_PER_ACTION * Mario.ACTION_PER_TIME * frame_time
        self.handle_events()

        for key,value in self.state.items():
            if key == 'WALK' and value == True:
                self.walk_frame = int(self.total_frames) % 4

        if self.presskey['RIGHT']:
            self.x += self.speed
            self.state['WALK'] = True
        elif self.presskey['LEFT']:
            self.x -= self.speed
            self.state['WALK'] = True
        else:
            if not self.state['JUMP']:
                self.set_state(True,False,False)
        #점프
        if self.jump == False:
            self.dropSpeed -= 0.5

        #중력
        if self.dropSpeed < 0:
            if (self.y + self.dropSpeed) < 125:
                self.y = 125
                self.dropSpeed = 0
                self.jump = True
                self.set_state(True,False,False)

        self.y += self.dropSpeed
