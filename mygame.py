import game_framework
import pico2d
import GM
import start_state

pico2d.open_canvas(GM.GAME_WIDTH,GM.GAME_HEIGHT)
game_framework.run(start_state)
pico2d.close_canvas()