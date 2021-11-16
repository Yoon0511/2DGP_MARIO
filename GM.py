GAME_WIDTH,GAME_HEIGHT = 1280,800
OFFSET_GAP = 0
objects = [[],[]]
COIN = 0
SCORE = 0

my_mario = None
map = None
enemys = None
bg = None
my_ui = None
items = []

def add_object(o, layer):
    objects[layer].append(o)

def add_objects(l, layer):
    objects[layer] += l

def remove_object(o):
    for i in range(len(objects)):
        if o in objects[i]:
            objects[i].remove(o)
            del o
            break

def clear():
    for o in all_objects():
        del o

def all_objects():
    for i in range(len(objects)):
        for o in objects[i]:
            yield o
