import game_framework
import pico2d
import GM
import title

pico2d.open_canvas(GM.GAME_WIDTH,GM.GAME_HEIGHT)
game_framework.run(title)
pico2d.close_canvas()