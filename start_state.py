from pico2d import *
import GM
import state_1
import game_framework

name = "StartState"
image = None
loading_time = 0.0
def handle_events():
    pass

def enter():
    global image
    image = load_image("Looding.png")

def exit():
    pass

def update():
    global loading_time

    if (loading_time > 1.0):
        loading_time = 0
        game_framework.change_state(state_1)
    loading_time += 0.01

def draw():
    global image
    clear_canvas()
    image.draw(GM.GAME_WIDTH//2,GM.GAME_HEIGHT//2)
    update_canvas()

def pause():
    pass

def resume():
    pass
