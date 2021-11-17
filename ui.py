from pico2d import *
import GM
import game_framework

class Ui:
    def __init__(self):
        self.font = load_font('myfont.TTF',30)
        self.time = 0

    def enter(self):
        pass

    def exit(self):
        pass

    def update(self):
        self.time += game_framework.frame_time

    def draw(self):
        self.font.draw(GM.GAME_WIDTH * 0.8,GM.GAME_HEIGHT*0.9,'TIME: %3.2f' % self.time,(255,255,255))
        self.font.draw(GM.GAME_WIDTH * 0.15, GM.GAME_HEIGHT * 0.9, 'COIN: %d' % GM.COIN, (255, 255, 255))
        self.font.draw(GM.GAME_WIDTH * 0.4, GM.GAME_HEIGHT * 0.9, 'SCORE: %d' % GM.SCORE, (255, 255, 255))