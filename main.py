from pico2d import *
import time
import keyboard

class Mario :
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 0.01 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 13
    total_frames = 0.0

    def __init__(self):
        self.x,self.y = 100,100
        self.state = {'IDLE':True,'WALK':False,'JUMP':False}
        self.presskey = {'LEFT':False,'RIGHT':False}
        self.speed = 3
        self.frame = 0
        self.img = load_image("mario.png")
        self.walk_frame = 0
        self.idle_frame = 0
        self.jump = True
        self.dropSpeed = 0
        self.dir = 0

    def draw_walk(self):
        if self.dir == 0:
            self.img.clip_draw(self.walk_frame * 35 + 35,253,35,50,self.x,self.y)
        if self.dir == 1:
            self.img.clip_draw(self.walk_frame * 35 + 35, 253, 35, 50, self.x, self.y)

    def draw_idle(self):
        self.img.clip_draw(self.idle_frame * 35 + 35,153,35,50,self.x,self.y)

    def now_state(self):
        return self.state

    def handle_events(self):
        global running
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
               running = False
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
               running = False

            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_d:
                    self.dir = 0
                    self.presskey['RIGHT'] = True
                elif event.key == SDLK_a:
                    self.dir = 1
                    self.presskey['LEFT'] = True
                elif event.key == SDLK_w:
                    if self.jump == True:
                        self.state['JUMP'] = True
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
        pass
        if(self.state['JUMP']):
            self.draw_idle()
        elif(self.state['WALK']):
            self.draw_walk()
        elif self.state['IDLE']:
            self.draw_idle()

    def update(self,frame_time):
        self.total_frames += Mario.FRAMES_PER_ACTION * Mario.ACTION_PER_TIME * frame_time
        self.handle_events()
        # if self.state == 'WALK':
        #     self.walk_frame = int(self.total_frames) % 13
        #     self.x += 1
        # if self.state == 'IDLE':
        #     self.idle_frame = int(self.total_frames) % 13
        # if self.state == 'JUMP':
        #     self.idle_frame = int(self.total_frames) % 13
        # 각 상태에 대한 애니메이션
        for key,value in self.state.items():
            if key == 'WALK' and value == True:
                self.walk_frame = int(self.total_frames) % 13
            if key == 'IDLE' and value == True:
                self.idle_frame = int(self.total_frames) % 13
            if key == 'JUMP' and value == True:
                self.idle_frame = int(self.total_frames) % 13

        if self.presskey['RIGHT']:
            self.x += self.speed
        elif self.presskey['LEFT']:
            self.x -= self.speed
        #점프
        if self.jump == False:
            self.dropSpeed -= 0.5

        #중력
        if self.dropSpeed < 0:
            if (self.y + self.dropSpeed) < 100:
                self.y = 100
                self.dropSpeed = 0
                self.jump = True
                #self.set_state(True,False,False)

        self.y += self.dropSpeed
        print(self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()
mario = Mario()
current_time = time.process_time()
running = True

while running:
    frame_time = time.process_time() - current_time
    current_time += frame_time

    clear_canvas()
    #handle_events()

    mario.update(current_time)
    mario.draw()

    update_canvas()
    delay(0.01)


close_canvas()