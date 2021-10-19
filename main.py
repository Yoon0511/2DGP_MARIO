from pico2d import *
import time
from Mario import *
import GM
from Map import *
from ENEMY import *

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
    #마리오가 앞으로 가는것이 아닌 배경이 앞으로 와서 마리오가 앞으로 가는것처럼 보임
def collision():
    for block in map.blocks:
        mario.Collision_block(block)


open_canvas(GAME_WIDTH,GAME_HEIGHT)
mario = Mario()
current_time = time.time()
map = MAP()
map.setup()
ene = map.get_enemeys()

while GM.running:
    frame_time = time.time() - current_time
    current_time += frame_time
    #handle_events()

    for ENEMY in ene:
        ENEMY.update(frame_time)
    mario.update(frame_time)
    map_offset()

    clear_canvas()

    collision()
    map.draw()
    mario.draw()
    for ENEMY in ene:
        ENEMY.draw()

    update_canvas()
    #delay(0.01)

close_canvas()