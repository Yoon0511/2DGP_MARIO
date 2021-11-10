from pico2d import *
import game_framework
import GM
from Mario import mario
from Map import MAP
import Map

my_mario = None
map = None
enemys = None

def enter():
    global my_mario
    my_mario = mario()
    GM.add_object(my_mario,1)

    global map
    my_map = MAP()
    map = my_map.blocks
    GM.add_objects(map,1)

    # global enemys
    # enemys = my_map.enemys
    # GM.add_object(enemys,1)

def exit():
    GM.clear()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        my_mario.handle_events(events)

def update():
    for game_object in GM.all_objects():
        game_object.update()

    for block in map:
        my_mario.Collision_block(block)

def draw():
    clear_canvas()
    for game_object in GM.all_objects():
        game_object.draw()
    update_canvas()

def pause():
    pass

def resume():
    pass
