import random

from pico2d import *
import GM
import Looding
import game_framework

name = "title"
image = None
loading_time = 0.0
font = None
R,G,B = 255,255,255
time = 0

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()

        if event.type == SDL_KEYDOWN and event.key != SDLK_ESCAPE:
            game_framework.change_state(Looding)

def enter():
    global image,font
    image = load_image("title.png")
    font = load_font('myfont.TTF', 40)

def exit():
    pass

def update():
    global time,R,G,B
    time += game_framework.frame_time
    if time >= 0.2:
        time = 0
        R = random.randint(0,255)
        G = random.randint(0, 255)
        B = random.randint(0, 255)


def draw():
    global image,R,G,B
    clear_canvas()
    image.draw(GM.GAME_WIDTH//2,GM.GAME_HEIGHT//2)
    font.draw(GM.GAME_WIDTH * 0.25, GM.GAME_HEIGHT * 0.3, 'Press Any Key To Start', (R, G, B))
    update_canvas()

def pause():
    pass

def resume():
    pass
