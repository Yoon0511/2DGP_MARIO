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

while GM.running:
    frame_time = time.process_time() - current_time
    current_time += frame_time
    #handle_events()
    clear_canvas()

    mario.update(current_time)

    map.draw()
    mario.draw()

    update_canvas()
    delay(0.01)

close_canvas()