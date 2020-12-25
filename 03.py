from lib import read_txt
from math import prod

lines = read_txt('03.txt', item_type=str, array_type=list)
size = len(lines[0])
height = len(lines)

def move_by_slope(pos, slope):
    pos[0] += slope[0]
    pos[1] += slope[1]

    if pos[0] >= size:
        pos[0] -= size
    
    if pos[1] >= height:
        pos[1] = height

    return pos

def check_tree(lines, pos):
    tmp = list(lines[pos[1]])
    if tmp[pos[0]] == '#': # that's a tree
        tmp[pos[0]] = 'X'
        tree = True
    else:
        tmp[pos[0]] = 'O'
        tree = False
    lines[pos[1]] = ''.join(tmp)
    return tree, lines

def run(slope, lines, size, height):
    pos = [0-slope[0], 0-slope[1]] # position x, Y
    tree_counter = 0

    for run in range(height):
# start with -slope run=0
# add slope -> slope == run -> check_trees
# pos still 0 but run == 1 -> just print
# pos still 0 but run == 2 -> move and check_trees
        if run - pos[1] == slope[1]:
            pos = move_by_slope(pos, slope)
            tree, lines = check_tree(lines, pos)
            if tree:
                tree_counter += 1

        print(run, lines[run])
   
    return tree_counter

slopes = [
    (1,1),
    (3,1),
    (5,1),
    (7,1),
    (1,2),
]

trees_per_slope = [run(slope, lines[:], size, height) for slope in slopes]
print(trees_per_slope)
print(prod(trees_per_slope))