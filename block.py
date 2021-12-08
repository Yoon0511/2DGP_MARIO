from pico2d import *
import GM
from item import Coin
from item import Mush
from item import Flower
import random

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

        if self.x <= -30:
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

    def make_coin(self):
        GM.sound.play_coin_bgm(10)
        GM.COIN += 1
        GM.SCORE += 100
        coins = Coin()
        coins.set_pos(self.x,self.y+60)
        GM.add_object(coins,1)

    def make_mush(self):
        mush = Mush()
        mush.set_pos(self.x,self.y+50)
        GM.add_object(mush, 1)
        GM.items.append(mush)

    def make_flower(self):
        flower = Flower()
        flower.set_pos(self.x,self.y+50)
        GM.add_object(flower,1)

    def collision_event(self):
        if self.get_type() == 'bitem':
            if GM.my_mario.level == 2:
                self.make_coin()
            else:
                randomitem = random.randint(0,3)
                if randomitem <= 3:
                    if randomitem == 0:
                        self.make_coin()
                    elif randomitem == 1:
                        self.make_mush()
                    elif randomitem == 2:
                        self.make_flower()
            self.type = '6'

