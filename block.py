from pico2d import *

class block:
    def __init__(self):
        self.b0 = load_image('b0.png')
        self.b1 = load_image('b1.png')
        self.b2 = load_image('b2.png')
        self.b3 = load_image('b3.png')
        self.b6 = load_image('b6.png')
        self.bA = load_image('bA.png')
        self.bB = load_image('bB.png')
        self.bC = load_image('bC.png')
        self.bD = load_image('bD.png')
        self.bE = load_image('bE.png')
        self.bF = load_image('bF.png')
        self.bitem = load_image('bitem.png')
        self.Gumba = load_image('Gumba.png')
        self.x,self.y = 0,0
        self.type = '1'

    def set_pos(self,x,y,type):
        self.x,self.y = x,y
        self.type = type

    def offet_pos(self,x,y):
        self.x += x
        self.y += y

    def draw(self):
        if self.type == '0':
            self.b0.draw(self.x,self.y,50,50)
        elif self.type == '1':
            self.b1.draw(self.x,self.y,50,50)
        elif self.type == '2':
            self.b2.draw(self.x, self.y, 50, 50)
        elif self.type == '3':
            self.b3.draw(self.x, self.y, 50, 50)
        elif self.type == '6':
            self.b6.draw(self.x, self.y, 50, 50)
        elif self.type == 'A':
            self.bA.draw(self.x, self.y, 50, 50)
        elif self.type == 'B':
            self.bB.draw(self.x, self.y, 50, 50)
        elif self.type == 'C':
            self.bC.draw(self.x, self.y, 50, 50)
        elif self.type == 'D':
            self.bD.draw(self.x, self.y, 50, 50)
        elif self.type == 'E':
            self.bE.draw(self.x, self.y, 50, 50)
        elif self.type == 'F':
            self.bF.draw(self.x, self.y, 50, 50)
        elif self.type == 'bitem':
            self.bitem.draw(self.x, self.y, 50, 50)
        elif self.type == 'G':
            self.Gumba.draw(self.x, self.y, 50, 50)