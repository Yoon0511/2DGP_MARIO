from pico2d import *
import GM
from item import Item

class block:
    image = False
    b0,b1,b2,b3,b6,bA,bB,bC,bD,bE,bF,bitem = None,None,None,None,None,None,None,None,None,None,None,None
    def __init__(self):
        #self.Gumba = load_image('Gumba.png')
        if block.image == False:
            block.b0 = load_image('b0.png')
            block.b1 = load_image('b1.png')
            block.b2 = load_image('b2.png')
            block.b3 = load_image('b3.png')
            block.b6 = load_image('b6.png')
            block.bA = load_image('bA.png')
            block.bB = load_image('bB.png')
            block.bC = load_image('bC.png')
            block.bD = load_image('bD.png')
            block.bE = load_image('bE.png')
            block.bF = load_image('bF.png')
            block.bitem = load_image('bitem.png')
            block.image = True
        self.x,self.y = 0,0
        self.type = '1'

    def set_pos(self,x,y,type):
        self.x,self.y = x,y
        if type == 'G' or type == 'T':
            self.type = '0'
        else:
            self.type = type

    def get_pos(self):
        return self.x,self.y

    def add_pos(self,x,y):
        self.x += x
        self.y += y

    def get_bb(self):
        return self.x - 25,self.y + 25,self.x + 25,self.y - 25

    def get_type(self):
        return self.type

    def update(self):
        self.add_pos(-GM.OFFSET_GAP,0)

        if self.x <= -100:
            GM.remove_object(self)

    def draw(self):
        if self.type == '0':
            block.b0.draw(self.x,self.y,50,50)
        elif self.type == '1':
            block.b1.draw(self.x,self.y,50,50)
        elif self.type == '2':
            block.b2.draw(self.x, self.y, 50, 50)
        elif self.type == '3':
            block.b3.draw(self.x, self.y, 50, 50)
        elif self.type == '6':
            block.b6.draw(self.x, self.y, 50, 50)
        elif self.type == 'A':
            block.bA.draw(self.x, self.y, 50, 50)
        elif self.type == 'B':
            block.bB.draw(self.x, self.y, 50, 50)
        elif self.type == 'C':
            block.bC.draw(self.x, self.y, 50, 50)
        elif self.type == 'D':
            block.bD.draw(self.x, self.y, 50, 50)
        elif self.type == 'E':
            block.bE.draw(self.x, self.y, 50, 50)
        elif self.type == 'F':
            block.bF.draw(self.x, self.y, 50, 50)
        elif self.type == 'bitem':
            block.bitem.draw(self.x, self.y, 50, 50)

        #draw_rectangle(*self.get_bb())

    def collision_event(self):
        if self.get_type() == 'bitem':
            coins = Item()
            coins.set_pos(self.x,self.y)
            GM.add_object(coins,1)
            self.type = '6'
            GM.COIN += 1
            GM.SCORE += 100
