from pico2d import *

class Enemy:
    def __init__(self):
        self.x,self.y = 0,0
        self.type = 'Gumba'
        self.Gumbaimg = load_image('Gumba.png')
        self.Turtleimg = load_image('turtle.png')
        self.dir = True
        self.movespeed = 250
        self.weith,self.height = 50,50
        self.drop = False
        self.dropSpeed = 0
        self.gravity = -8.8
        self.frametime = 0

    def move(self):
        if dir == 0: # 왼쪽
            self.x -= self.movespeed * self.frametime
        elif dir == 1: #오른쪽
            self.x += self.movespeed * self.frametime

    def get_pos(self):
        return self.x,self.y

    def set_addpos(self,x,y):
        self.x += x
        self.y += y

    def set_pos(self,x,y,type):
        self.x = x
        self.y = y
        self.type = type

    def get_bb(self):
        return self.x - 25, self.y + 25, self.x + 25, self.y - 25

    def update(self,frame_time):
        self.frametime = frame_time
        self.move()

        if self.drop == True:
            self.dropSpeed += self.gravity

        self.y += self.dropSpeed * frame_time

    def draw(self):
        if self.type == 'Gumba':
            self.Gumbaimg.draw(self.x,self.y)
        if self.type == 'Turtle':
            if self.dir == 0: # 왼쪽
                self.Turtleimg.clip_draw(0,0,self.weith,self.height,self.x,self.y)
            elif self.dir == 1: # 오른쪽
                self.Turtleimg.clip_draw(self.weith,0,self.weith,self.height,self.x,self.y)