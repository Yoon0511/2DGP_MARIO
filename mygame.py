import game_framework
import pico2d
import GM
import title

import RESULT

pico2d.open_canvas(GM.GAME_WIDTH,GM.GAME_HEIGHT)
game_framework.run(RESULT)
pico2d.close_canvas()