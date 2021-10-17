from pico2d import *
import time
from Mario import *
from GM import *
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



open_canvas(GAME_WIDTH,GAME_HEIGHT)
mario = Mario()
current_time = time.process_time()
map = MAP()
map.setup()

def map_offset():
    mx,my = mario.get_pos()
    offsetx = GAME_WIDTH/2
    gap = 0
    if mx >= offsetx:
        gap = mx - offsetx
        mario.set_addpos(-gap,0)
    for block in map.blocks:
        block.offet_pos(-gap,0)

while GM.running:
    frame_time = time.process_time() - current_time
    current_time += frame_time
    #handle_events()
    clear_canvas()

    mario.update(current_time)
    map_offset()

    map.draw()
    mario.draw()

    update_canvas()
    delay(0.01)

close_canvas()