from pico2d import *

class block:
    def __init__(self):
        self.b1 = load_image('b1.png')
        self.b0 = load_image('b0.png')
        self.x,self.y = 0,0
        self.type = '1'

    def set_pos(self,x,y,type):
        self.x,self.y = x,y
        self.type = type

    def draw(self):
        if self.type == '1':
            self.b1.draw(self.x,self.y,50,50)
        elif self.type == '0':
            self.b0.draw(self.x,self.y,50,50)