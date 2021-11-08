from block import *
from ENEMY import *
#1280 800
# 맵 (블록,몬스터) 정보 파일

class MAP:
    def __init__(self):
        self.path = 'stage1.txt'
        self.blocks = []
        self.enemys = []
        # self.skyblocks = []
        self.setup()

    def get_blocks(self):
        return self.blocks

    def draw(self):
        for block in self.blocks:
            block.draw()
        # for skyblock in self.skyblocks:
        #     skyblock.draw()

    def get_enemeys(self):
        return self.enemys

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
            if a != '0':
                if a == '6' or a == '7' or a == '8' or a == '4' or a == '5':
                    bl.set_pos(x - 25, y - 50, 'bitem')
                elif a == 'G' or a == 'T':
                    bl.set_pos(x - 25, y - 50,'0')  # 굼바나 거북이인 곳을 하늘블록으로 채움
                    enemy = Enemy()                 #하늘블록으로 채운곳에 enemy생성
                    enemy.set_pos(x - 25,y - 50, a)
                    self.enemys.append(enemy)
                else:
                    # not 아이템박스 not enmey
                    bl.set_pos(x - 25, y - 50, a)
                self.blocks.append(bl)
            x += 50

        mapdata.close()
        # for i in range(25,1280,50):
        #     skyblock = block()
        #     skyblock.set_pos(i,775,'0')
        #     self.skyblocks.append(skyblock)

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
