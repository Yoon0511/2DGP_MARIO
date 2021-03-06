from pico2d import *
import game_framework
import GM
from Mario import mario
from Map import MAP
from background import Background
from ui import Ui
import Map
from SOUND import Sound

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

def collide_enmey(a, b):
    left_a, top_a, right_a, bottom_a = a.get_bb()
    left_b, top_b, right_b, bottom_b = b.get_bb()

    # if left_a - 25 > left_b: return False
    # if right_a + 25 < right_b: return False
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def enter():
    GM.COIN, GM.SCORE, GM.PLAY_TIME,GM.ITEM_COUNT = 0, 0, 0.0,0
    GM.sound.stop_main_bgm()

    GM.map = MAP()
    GM.add_objects(GM.map.blocks,1)

    GM.my_mario = mario()
    GM.add_object(GM.my_mario, 1)

    GM.bg = Background()
    GM.add_object(GM.bg,0)

    GM.enemys = GM.map.enemys
    GM.add_objects(GM.enemys,1)

    GM.my_ui = Ui()
    GM.add_object(GM.my_ui,1)

def exit():
    GM.clear()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        GM.my_mario.handle_events(events)

def update():
    for game_object in GM.all_objects():
        game_object.update()

    foot_collision = 0
    for block in GM.map.blocks:
        GM.my_mario.Collision_block(block)

        for fireball in GM.my_mario.fireballlist:
            fireball.collision_block(block)

        if not (collide(GM.my_mario,block)):
            foot_collision+=1

    if (foot_collision == len(GM.map.blocks)):
        GM.my_mario.down_mario()

    for block in GM.map.blocks:
        for enemy in GM.enemys:
            enemy.Collsion_block(block)

    for enemy in GM.enemys:
        if (collide(GM.my_mario,enemy)):
            if GM.my_mario.jump == False and GM.my_mario.iscollsion == False:
                GM.my_mario.kill_enemy()
                enemy.set_state('DIE')
                GM.enemys.remove(enemy)
                #GM.remove_object(enemy)
        if(collide_enmey(GM.my_mario,enemy)):
            GM.my_mario.collisiontoEenemy()

        for fireball in GM.my_mario.fireballlist:
            fireball.collision_enemy(enemy)

    for mush in GM.items:
        for block in GM.map.blocks:
            mush.Collsion_block(block)


def draw():
    clear_canvas()
    for game_object in GM.all_objects():
        game_object.draw()
    update_canvas()

def pause():
    pass

def resume():
    pass
