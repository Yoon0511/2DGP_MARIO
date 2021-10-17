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
            if block.get_type() == 'bitem' or block.get_type() == '3':
                mx,my = mario.get_pos()
                bx,by = block.get_pos()
                gapx,gapy = 0,0
                # 마리오 기준충돌위치
                if mx > bx : #왼쪽충돌
                    #print('left')
                    gapx = bright - mleft
                elif mx < bx: #오른쪽충돌
                    #print('right')
                    gapx = mright - bleft
                if my > by : #아래 충돌
                    #print('down')
                    gapy = btop - mbottom
                elif my < by: #위 충돌
                    #print('up')
                    gapy = mtop - bbottom

                if gapx < gapy:
                    mario.set_addpos(0,-gapy)
                else:
                    mario.set_addpos(-gapx,0)


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