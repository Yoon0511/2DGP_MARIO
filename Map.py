from block import *

#1280 800

class MAP:
    def __init__(self):
        self.path = 'stage1.txt'
        self.blocks = []

    def draw(self):
        for block in self.blocks:
            block.draw()


    def setup(self):
        x,y = 0,775
        mapdata = open(self.path, 'r')
        n = mapdata.read()
        for a in n:
            if a == '\n':
                x = 0
                y -= 50
                continue

            bl = block()
            if a == '6' or a == '7':
                bl.set_pos(x - 25, y - 50, 'bitem')
            else:
                bl.set_pos(x - 25, y - 50,a)
            self.blocks.append(bl)
            x += 50

        mapdata.close()

def main():
    r = True
    open_canvas(1280,800)
    map = MAP()
    map.setup()
    while r:
        clear_canvas()
        map.draw()
        update_canvas()

    #close_canvas()

if __name__ == '__main__':
    main()
