from data24 import test, puzzle

from collections import Counter, defaultdict

def parse_inp(txt):
    txt = list(txt)
    x = 0
    y = 0
    z = 0
    while txt:
        char = txt.pop(0)
        if char == 's':
            z -= 1
            n_char = txt.pop(0)
            if n_char == 'e':
                x += 1
            else:
                y -= 1
        elif char == 'n':
            z += 1
            n_char = txt.pop(0)
            if n_char == 'e':
                y += 1
            else:
                x -= 1
        elif char == 'w':
            x -= 1
            y -= 1
        else:
            x += 1
            y += 1
    
    return (x, y, z)

def count(tiles):
    whites = 0
    blacks = 0

    for k, v in tiles.items():
        if v:
            blacks += 1
        else:
            whites += 1

    return blacks, whites

def increase_range(tiles):
    new = tiles.copy()
    DIF = [
        (-1,0,1),
        (-1,-1,0),
        (0,-1,-1),
        (0,1,1),
        (1,0,-1),
        (1,1,0),
    ]

    for k, v in new.items():
        for dx, dy, dz in DIF:
            tiles[k[0]+dx, k[1]+dy, k[2]+dz]


def flippedyfloppedy(tiles):
    new = tiles.copy()

    DIF = [
        (-1,0,1),
        (-1,-1,0),
        (0,-1,-1),
        (0,1,1),
        (1,0,-1),
        (1,1,0),
    ]

    for k, v in new.items():
        black_neighbors = [tiles[(k[0]+dx,
        k[1]+dy,
        k[2]+dz)] for dx, dy, dz in DIF]
        num = sum(black_neighbors)
        if v and (num == 0 or num > 2): # if black and blackneighbors are exactly 0 or more than 2 flip to white
            new[k] = False
        elif not v and num == 2: # if white and blackneighbors are exactly 2 flip to black
            new[k] = True
    
    tiles.update(new)

tiles = defaultdict(bool)

for instr in puzzle: # swap test with puzzle for input
    x, y, z = parse_inp(instr)
    tiles[(x, y, z)] = not tiles[(x, y, z)]

print(f'Part One: {count(tiles)[0]} blacks')

increase_range(tiles)
for i in range(1, 101):
    flippedyfloppedy(tiles)
    print(f'Day {str(i).rjust(3)}: {str(count(tiles)[0]).rjust(6)} blacks')
