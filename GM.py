GAME_WIDTH,GAME_HEIGHT = 1280,800
OFFSET_GAP = 0
objects = [[],[]]
COIN = 0
SCORE = 0
STAGE_CLEAR = False

my_mario = None
map = None
enemys = None
bg = None
my_ui = None
items = []
sound = None

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
    for _ in all_objects():
        del _

    for l in objects:
        l.clear()

def destroy():
    clear()
    objects.clear()

def all_objects():
    for i in range(len(objects)):
        for o in objects[i]:
            yield o