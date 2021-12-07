from pico2d import *

class Sound:
    def __init__(self):
        self.main_bgm           = load_music('sound\main_bgm.mp3')
        self.coin_bgm           = load_music('sound\Coin.wav')
        self.enemy_die_bgm      = load_music('sound\enemy_die.mp3')
        self.clear_bgm          = load_music('sound\clear.mp3')
        self.fire_ball_bgm      = load_music("sound\_fire_ball.mp3")
        self.jump_bgm           = load_music('sound\jump.wav')
        self.level_up_bgm       = load_music('sound\level_up.mp3')
        self.mario_die_bgm      = load_music('sound\mario_die.mp3')

    def play_main_bgm(self,volum):
        self.main_bgm.repeat_play()
        self.main_bgm.set_volume(volum)

    def play_coin_bgm(self,volum):
        self.coin_bgm.play(1)
        self.coin_bgm.set_volume(volum)

    def play_enemy_die_bgm(self, volum):
        self.enemy_die_bgm.play(1)
        self.enemy_die_bgm.set_volume(volum)

    def play_clear_bgm(self, volum):
        self.clear_bgm.play(1)
        self.clear_bgm.set_volume(volum)

    def play_fire_ball_bgm(self, volum):
        self.fire_ball_bgm.play(1)
        self.fire_ball_bgm.set_volume(volum)

    def play_jump_bgm(self, volum):
        self.jump_bgm.play(1)
        self.jump_bgm.set_volume(volum)

    def play_level_up_bgm(self, volum):
        self.level_up_bgm.play(1)
        self.level_up_bgm.set_volume(volum)

    def play_mario_die_bgm(self, volum):
        self.mario_die_bgm.play(1)
        self.mario_die_bgm.set_volume(volum)
