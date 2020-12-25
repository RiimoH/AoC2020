from inp20 import data
# from test20 import data
from collections import defaultdict
import regex as re


tiles = data.split('\n\n')

class Tiles():
    def __init__(self, txt):
        num, lines = txt.lstrip('Tile ').split(':\n')
        self.num = int(num)
        self.lines = lines.split('\n')
        self.rotated = 0
        self.generate_edges()
        self.is_corner = False
        self.is_edge = False
        self.is_placed = False
        self.lone_edges = []

    def generate_edges(self):
        self.edges = [self.lines[0], self.lines[-1]]
        self.rotate()
        self.edges.extend([self.lines[0], self.lines[-1]])
        
    def rotate(self):
        self.lines = [''.join(x) for x in zip(*self.lines[::-1])]
        self.rotated += 1

        if self.rotated == 4:
            self.lines = [''.join(reversed(x)) for x in self.lines]
            self.rotated = 0
    
    def vertical_edges(self):
        l = [''.join(x) for x in zip(*self.lines[::-1])]
        return [l[0], l[-1]]
    
    def img(self):
        img = [line[1:-1] for line in self.lines[1:-1]]
        return img


# Part One
tiles = [Tiles(t) for t in tiles]
all_edges = []
for t in tiles:
    all_edges.extend(t.edges)

# find corner tiles:
for t in tiles:
    t_sum = 0
    for e in t.edges:
        if (all_edges.count(e) + all_edges.count("".join(reversed(e)))) == 1:
            t_sum += 1
            t.lone_edges.append(e)
        else:
            t_sum += 2
    if t_sum == 6:
        t.is_corner = True
    elif t_sum == 7:
        t.is_edge = True

p = 1
for t in tiles:
    if t.is_corner:
        p *= t.num

print(p)
print(p == 17250897231301)

# Part Two
tile_map = {}

def recurse(tile_map, tiles, last_tile, max_x, x, y):

    if x != 0:
        last_edge = last_tile.vertical_edges()[1]
        new_edge = lambda x: x.vertical_edges()[0]
    else:
        last_tile = tile_map[(x, y-1)]
        last_edge = last_tile.lines[-1]
        new_edge = lambda x: x.lines[0]

    for t in tiles:
        if not t.is_placed:
            for _ in range(8):
                if new_edge(t) == last_edge:
                    tile_map[(x, y)] = t
                    t.is_placed = True
                    if (t.is_corner and x > 0) or x == max_x:
                        max_x = x
                        nx = 0
                        ny = y + 1
                    else:
                        nx = x + 1
                        ny = y

                    return recurse(tile_map, tiles, t, max_x, nx, ny)
                else:
                    t.rotate()

for t in tiles:
    if t.is_corner: # find first corner and rotate it in place
        for i in range(8):
            if not (t.lines[0] in t.lone_edges and t.vertical_edges()[0] in t.lone_edges):
                t.rotate()
            else:
                break
        tile_map[(0,0)] = t
        t.is_placed = True
        last_tile = t
        break

recurse(tile_map, tiles, last_tile, -1, 1, 0)

def transform(img):
    lines = img.rstrip('\n').split('\n')
    yield lines
    for i in range(7):

        lines = [''.join(x) for x in zip(*lines[::-1])]

        if i == 4:
            lines = [''.join(reversed(x)) for x in lines]

        yield lines
    


l = list(zip(*[*tile_map.keys()]))
xl = max(l[0]) + 1
yl = max(l[1]) + 1
arr = [['' for x in range(xl)] for y in range(yl)]

for k, v in tile_map.items():
    x, y = k
    arr[y][x] = v.img()

img = ''
for y in range(yl):
    for x in zip(*arr[y]):
        img += ''.join(x) + '\n'


def findmonsters(im):
    monster = 0
    nessi = r"..................#."
    m2 = r"(?=#....##....##....###)"
    m3 = r"(?=.#..#..#..#..#..#)"
    for i, r in enumerate(im):
        ns1 = [m.start(0) for m in re.finditer(m2, r)]
        for n1 in ns1:
            if n1 and i > 0:
                ns2 = [m.start(0) for m in re.finditer(m3, im[i+1])]
                if n1 in ns2:
                    if im[i-1][n1+18] == '#':
                        monster += 1
    return monster

mon = 0
trans = transform(img)
for im in trans:
    print(im)
    mon += findmonsters(im)

print(f"{mon} sea monsters")
print(f"Roughness: {img.count('#')-mon*15}")
