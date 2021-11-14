from pico2d import *

import GM
import game_framework

PIXEL_PER_METER = (10.0 / 0.5)  # 10 pixel 30 cm
MOVE_SPEED_KMPH = 20.0  # Km / Hour
MOVE_SPEED_MPM = (MOVE_SPEED_KMPH * 1000.0 / 60.0)
MOVE_SPEED_MPS = (MOVE_SPEED_MPM / 60.0)
MOVE_SPEED_PPS = (MOVE_SPEED_MPS * PIXEL_PER_METER)

class Background:
    SKY = None
    CLOUD1 = None
    CLOUD2 = None
    def __init__(self):
        if Background.SKY == None:
            Background.SKY = load_image('sky.png')
        if Background.CLOUD1 == None:
            Background.CLOUD1 = load_image('cloud_1.png') # 60 x 44
        if Background.CLOUD2 == None:
            Background.CLOUD2 = load_image('cloud_2.png') # 150 x 113
        self.speed = 0
        self.cloud1_x,self.cloud2_x = GM.GAME_WIDTH * 0.3,GM.GAME_WIDTH * 0.7
        self.cloud3_x, self.cloud4_x = GM.GAME_WIDTH * 0.6, GM.GAME_WIDTH * 0.8
        self.cloud_x = [self.cloud1_x,self.cloud2_x,self.cloud3_x,self.cloud4_x]

    def enter(self):
        pass

    def exit(self):
        pass

    def update(self):
        self.cloud_x[0] -= MOVE_SPEED_PPS * game_framework.frame_time
        self.cloud_x[1] -= (MOVE_SPEED_PPS * 1.3) * game_framework.frame_time
        self.cloud_x[2] -= (MOVE_SPEED_PPS * 0.6) * game_framework.frame_time
        self.cloud_x[3] -= (MOVE_SPEED_PPS * 1.8) * game_framework.frame_time

        for i in range(len(self.cloud_x)):
            if self.cloud_x[i] <= -50:
                self.cloud_x[i] = 1310

    def draw(self):
        Background.SKY.draw(GM.GAME_WIDTH // 2, GM.GAME_HEIGHT // 2, GM.GAME_WIDTH,GM.GAME_HEIGHT)
        Background.CLOUD1.clip_draw(0,0,60,44,self.cloud_x[0],GM.GAME_HEIGHT * 0.7)
        Background.CLOUD2.clip_draw(0,0,150,113,self.cloud_x[1],GM.GAME_HEIGHT * 0.5)
        Background.CLOUD2.clip_draw(0, 0, 150, 113, self.cloud_x[2], GM.GAME_HEIGHT * 0.65)
        Background.CLOUD1.clip_draw(0, 0, 60, 44, self.cloud_x[3], GM.GAME_HEIGHT * 0.8)
