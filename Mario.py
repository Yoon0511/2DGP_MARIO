from pico2d import *
import GM
import game_framework
import Looding
import title
from EFFECT import Effect

invincibility_time = 0.5

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
        self.img = load_image('m1.png')
        self.img_man = load_image('mario_man.png')
        self.img_fireman = load_image('mario_fire.png')
        self.img_dead = load_image('mario_dead.png')
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
        self.fireballlist = []
        self.die = False
        self.collision_timer = 0
        self.iscollsion = False
        self.fireball_cooltime = 0.5
        self.die_time = 0

    def get_pos(self):
        return self.x,self.y

    def get_bb(self):
        if self.level == 0:
            return self.x - 22,self.y + 25,self.x + 22,self.y - 20
        elif self.level == 1 or self.level == 2:
            return self.x - 22, self.y + 35, self.x + 22, self.y - 30

    def get_foot_bb(self):
        if self.level == 0:
            return self.x - 17,self.y-24,self.x + 17,self.y-25
        elif self.level == 1 or self.level == 2:
            return self.x - 17, self.y - 34, self.x + 17, self.y - 34

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
                self.img_man.clip_draw(self.walk_frame * self.weith,0,self.weith,self.height,self.x,self.y)
            elif self.dir == 1:
                self.img_man.clip_draw(self.walk_frame * self.weith,self.height,self.weith,self.height,self.x,self.y)
        if self.level == 2:
            if self.dir == 0:
                self.img_fireman.clip_draw(self.walk_frame * self.weith, 0, self.weith, self.height, self.x, self.y)
            elif self.dir == 1:
                self.img_fireman.clip_draw(self.walk_frame * self.weith, self.height, self.weith, self.height, self.x,
                                       self.y)

    def draw_idle(self):
        if self.level == 0:
            if self.dir == 0:
                self.img.clip_draw(0,0,self.weith,self.height,self.x,self.y)
            elif self.dir == 1:
                self.img.clip_draw(0,self.height,self.weith,self.height,self.x,self.y)
        if self.level == 1:
            if self.dir == 0:
                self.img_man.clip_draw(0,0,self.weith,self.height,self.x,self.y)
            elif self.dir == 1:
                self.img_man.clip_draw(0,self.height,self.weith,self.height,self.x,self.y)
        if self.level == 2:
            if self.dir == 0:
                self.img_fireman.clip_draw(0,0,self.weith,self.height,self.x,self.y)
            elif self.dir == 1:
                self.img_fireman.clip_draw(0,self.height,self.weith,self.height,self.x,self.y)

    def draw_jump(self):
        if self.level == 0:
            if self.dir == 0:
                self.img.clip_draw(50, 0, 50, 50, self.x, self.y)
            elif self.dir == 1:
                self.img.clip_draw(50, 50, 50, 50, self.x, self.y)
        if self.level == 1:
            if self.dir == 0:
                self.img_man.clip_draw(50,0,self.weith,self.height,self.x,self.y)
            elif self.dir == 1:
                self.img_man.clip_draw(50,self.height,self.weith,self.height,self.x,self.y)
        if self.level == 2:
            if self.dir == 0:
                self.img_fireman.clip_draw(50,0,self.weith,self.height,self.x,self.y)
            elif self.dir == 1:
                self.img_fireman.clip_draw(50,self.height,self.weith,self.height,self.x,self.y)

    def draw_die(self):
        self.img_dead.clip_draw(0,0,self.weith,self.height,self.x,self.y)

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
                        GM.sound.play_jump_bgm(10)
                        self.set_state(False,False,True)
                        self.dropSpeed = self.jump_power
                        #self.accel = 5
                        self.jump = False
                elif event.key == SDLK_SPACE:
                    self.fire_ball()

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

        #충돌시 invincibility_time동안 무적
        if self.iscollsion == True:
            self.collision_timer += game_framework.frame_time
            if self.collision_timer >= invincibility_time:
                self.collision_timer = 0
                self.iscollsion = False

        #불덩이 쿨타임
        if self.fireball_cooltime <= 0.5:
            self.fireball_cooltime += game_framework.frame_time

        #사망시 1초뒤 재시작
        if self.die == True:
            self.die_time += game_framework.frame_time
            if self.die_time >= 2.5:
                self.die = False
                self.die_time = 0
                game_framework.change_state(title)

    def draw(self):
        if self.die == True:
            self.draw_die()
            return

        if self.state['JUMP']:
            self.draw_jump()
        elif self.state['WALK']:
            self.draw_walk()
        elif self.state['IDLE']:
            self.draw_idle()


        draw_rectangle(*self.get_bb())
        draw_rectangle(*self.get_foot_bb())

    def Collision_block(self,block):
        if self.die == True : return

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
                    #self.jump_time = 1.5
                    if self.state['IDLE'] == False:
                        self.set_state(True, False, False)
            if t == True:
                block.collision_event()
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
        GM.sound.play_enemy_die_bgm(10)
        self.set_addpos(0,5)
        self.dropSpeed = 0
        self.accel = -5
        self.dropSpeed = 200
        GM.SCORE += 300

    def fire_ball(self):
        if self.level != 2: return
        if self.fireball_cooltime < 0.5 : return
        self.fireball_cooltime = 0

        GM.sound.play_fire_ball_bgm(10)
        fireball = FireBall()
        if self.dir == 0:
            fireball.setting(self.x + 20,self.y + (self.height//2)*0.7,self.dir)
        elif self.dir == 1:
            fireball.setting(self.x + 20,self.y + (self.height//2)*0.7,self.dir)

        self.fireballlist.append(fireball)
        GM.add_object(fireball,1)

    def collisiontoEenemy(self):
        if self.iscollsion == True : return

        self.iscollsion = True
        level = self.level
        level -= 1
        if level <= -1:
            GM.sound.play_mario_die_bgm(10)
            self.die = True
            self.set_addpos(0, 2)
            self.dropSpeed = 0
            self.accel = -5
            self.dropSpeed = 300
        else:
            self.level = level
            if self.level == 0:
                self.height = 50


PIXEL_PER_METER = (10.0 / 0.5)  # 10 pixel 50 cm
FIRE_BALL_MOVE_SPEED_KMPH = 70.0  # Km / Hour
FIRE_BALL_SPEED_MPM = (FIRE_BALL_MOVE_SPEED_KMPH * 1000.0 / 60.0)
FIRE_BALL_SPEED_MPS = (FIRE_BALL_SPEED_MPM / 60.0)
FIRE_BALL_SPEED_PPS = (FIRE_BALL_SPEED_MPS * PIXEL_PER_METER)

class FireBall: # 20 x 20
    fireball = None
    def __init__(self):
        if FireBall.fireball == None:
            FireBall.fireball = load_image('fire.png')
        self.x,self.y = 0,0
        self.dir = 0
        self.angle = 0
        self.drop = True
        self.dropSpeed = 0
        self.gravity = -20.5
        self.accel = 0

    def get_bb(self):
        return self.x - 10,self.y + 10,self.x + 10, self.y -10

    def setting(self,x,y,dir):
        self.x,self.y,self.dir = x,y,dir

    def get_pos(self):
        return self.x,self.y

    def add_pos(self,x,y):
        self.x += x
        self.y += y

    def enter(self):
        pass

    def exit(self):
        pass

    def update(self):
        self.add_pos(-GM.OFFSET_GAP, 0)

        if self.dir == 0: #왼쪽
            self.x += FIRE_BALL_SPEED_PPS * game_framework.frame_time
        elif self.dir == 1: #오른쪽
            self.x += FIRE_BALL_SPEED_PPS * game_framework.frame_time * -1

        self.angle += 1000 * game_framework.frame_time


        if self.drop == True:
            self.dropSpeed += self.accel
            self.accel += self.gravity * game_framework.frame_time
            if self.accel <= -300:
                self.accel = -300

        self.y += self.dropSpeed * game_framework.frame_time

    def draw(self):
        FireBall.fireball.clip_composite_draw(0, 0, 20, 20, self.angle * (3.14 / 180), '', self.x,self.y,20, 20)

    def make_effect(self,x,y):
        effect = Effect()
        effect.set_pos(x,y)
        GM.add_object(effect,1)

    def collision_enemy(self,enemy):
        eleft, etop, eright, ebottom = self.get_bb()
        bleft, btop, bright, bbottom = enemy.get_bb()

        if ebottom > btop: return
        if eleft > bright: return
        if eright < bleft: return
        if etop < bbottom: return

        GM.sound.play_enemy_die_bgm(10)
        self.make_effect(self.x,self.y)
        GM.SCORE += 300
        enemy.set_state('DIE')
        GM.enemys.remove(enemy)

        GM.remove_object(self)
        GM.my_mario.fireballlist.remove(self)


    def collision_block(self,block):
        eleft, etop, eright, ebottom = self.get_bb()
        bleft, btop, bright, bbottom = block.get_bb()

        if ebottom - 40 > btop:
            self.drop = True
            return
        if eleft - 40 > bright: return
        if eright + 40 < bleft: return
        if etop + 40 < bbottom: return

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
                    self.dropSpeed = 150
                    self.accel = 0
        else:
            if not block.get_type() == '1':
                if l == True:
                    self.make_effect(self.x, self.y)
                    GM.my_mario.fireballlist.remove(self)
                    GM.remove_object(self)
                if r == True:
                    self.make_effect(self.x, self.y)
                    GM.my_mario.fireballlist.remove(self)
                    GM.remove_object(self)