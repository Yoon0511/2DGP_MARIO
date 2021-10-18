from pico2d import *
import time
from Mario import *
import GM
from Map import *

GAME_WIDTH,GAME_HEIGHT = 1280,800

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def map_offset():
    mx,my = mario.get_pos()
    offsetx = GAME_WIDTH/2
    gap = 0
    if mx >= offsetx:
        gap = mx - offsetx
        mario.set_addpos(-gap,0)
    for block in map.blocks:
        block.offet_pos(-gap,0)

def collision():
    mleft,mtop,mright,mbottom = mario.get_bb()

    for block in map.blocks:
        bleft,btop,bright,bbottom = block.get_bb()
        if mleft <= bright and mtop >= bbottom and mright >= bleft and mbottom <= btop:
            mx,my = mario.get_pos()
            bx,by = block.get_pos()
            l,r,b,t = False,False,False,False
            gapx,gapy = 0,0
                # 마리오 기준충돌위치
            if mx > bx : #왼쪽충돌 +
                gapx = bright - mleft
                l = True
            elif mx < bx: #오른쪽충돌 -
                gapx = mright - bleft
                r = True
            if my > by : #아래 충돌 +
                gapy = btop - mbottom
                b = True
            elif my < by: #위 충돌 -
                gapy = mtop - bbottom
                t = True

            if gapx > gapy:
                if not block.get_type() == '0':  # 하늘이 아닌 모든 블록
                    if b == True:
                        mario.set_addpos(0,gapy + 0.1)
                        mario.dropSpeed = 0
                        mario.jump = True
                        mario.set_state(True,False,False)
                    if t == True:
                        mario.dropSpeed = 0
                        mario.jump = False
                        mario.set_addpos(0, -gapy)
            else:
                if not block.get_type() == '0':
                    if l == True:
                        #print('l')
                        mario.set_addpos(gapx + 1,0)
                    if r == True:
                        #print('r')
                        mario.set_addpos(-gapx, 0)


open_canvas(GAME_WIDTH,GAME_HEIGHT)
mario = Mario()
current_time = time.time()
map = MAP()
map.setup()

while GM.running:
    frame_time = time.time() - current_time
    current_time += frame_time
    #handle_events()
    clear_canvas()
    mario.update(frame_time)
    map_offset()

    collision()
    map.draw()
    mario.draw()

    update_canvas()
    delay(0.01)

close_canvas()