from pico2d import *
import game_framework
import GM
from Mario import mario
from Map import MAP
from background import Background
from ui import Ui
import Map

my_mario = None
map = None
enemys = None
bg = None
my_ui = None

def collide(a, b):
    left_a, top_a, right_a, bottom_a = a.get_foot_bb()
    left_b, top_b, right_b, bottom_b = b.get_bb()

    # if left_a - 25 > left_b: return False
    # if right_a + 25 < right_b: return False
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def enter():
    global my_mario
    my_mario = mario()
    GM.add_object(my_mario,1)

    global map
    my_map = MAP()
    map = my_map.blocks
    GM.add_objects(map,1)

    global bg
    bg = Background()
    GM.add_object(bg,0)

    global enemys
    enemys = my_map.enemys
    GM.add_objects(enemys,1)

    global my_ui
    my_ui = Ui()
    GM.add_object(my_ui,1)

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

    foot_collision = 0
    for block in map:
        my_mario.Collision_block(block)
        if not (collide(my_mario,block)):
            foot_collision+=1
    if (foot_collision == len(map)):
        my_mario.down_mario()

    for block in map:
        for enemy in enemys:
            enemy.Collsion_block(block)

    for enemy in enemys:
        if (collide(my_mario,enemy)):
            my_mario.kill_enemy()
            enemy.set_state('DIE')
            enemys.remove(enemy)
            GM.remove_object(enemy)


def draw():
    clear_canvas()
    for game_object in GM.all_objects():
        game_object.draw()
    update_canvas()

def pause():
    pass

def resume():
    pass
