import random
from pico2d import *
import GM
import title
import Looding
import game_framework
from SOUND import Sound

name = "result"
image = None
loading_time = 0.0
font = None
title_font = None
time,coin,score = 0,0,0

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()

def enter():
    global image,font,title_font
    image = load_image("black.png")
    font = load_font('myfont.TTF', 30)
    title_font = load_font('myfont.TTF', 80)
    GM.sound = Sound()
    GM.sound.play_clear_bgm(10)

def exit():
    GM.COIN,GM.SCORE,GM.PLAY_TIME = 0,0,0.0

def update():
    global time,coin,score,loading_time
    if time < GM.PLAY_TIME:
        time += 0.1
    if coin < GM.COIN and time >= GM.PLAY_TIME:
        coin += 1
    if score < GM.SCORE and time >= GM.PLAY_TIME and coin >= GM.COIN:
        score += 10

    if score >= GM.SCORE and time >= GM.PLAY_TIME and coin >= GM.COIN:
        loading_time += game_framework.frame_time
        if loading_time >= 3:
            game_framework.change_state(title)

def draw():
    global image
    clear_canvas()
    image.draw(GM.GAME_WIDTH//2,GM.GAME_HEIGHT//2)
    title_font.draw(GM.GAME_WIDTH * 0.35, GM.GAME_HEIGHT * 0.8, 'CLEAR!', (255, 255, 255))

    font.draw(GM.GAME_WIDTH * 0.35, GM.GAME_HEIGHT * 0.6, 'Time %3.1f' % time, (255, 255, 255))
    font.draw(GM.GAME_WIDTH * 0.35, GM.GAME_HEIGHT * 0.4, 'COIN %d' % coin, (255, 255, 255))
    font.draw(GM.GAME_WIDTH * 0.35, GM.GAME_HEIGHT * 0.2, 'SCORE %d' % score, (255, 255, 255))
    update_canvas()

def pause():
    pass

def resume():
    pass
