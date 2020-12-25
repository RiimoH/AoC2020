from collections import Counter, defaultdict
from copy import deepcopy

def neighbors(arr):
    d = defaultdict(list)
    len_y, len_x = len(arr), len(arr[0])

    vectors = (
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
        )

    for y in range(len_y):
        for x in range(len_x):
            for dy, dx in vectors:
                factor = 1

                while len_y > y+dy*factor >= 0 and len_x > x+dx*factor >= 0:
                    if arr[y+dy*factor][x+dx*factor] == FREE:
                        d[(y, x)].append((y+dy*factor, x+dx*factor))
                        break
                    else:
                        factor += 1
    
    return d


def part_one(arr):

    new = deepcopy(arr)
    for y in range(len(arr)):
        for x in range(len(arr[0])):
            if arr[y][x] == FLOOR:
                continue

            taken = 0

            for dy, dx in neigh[(y, x)]:
                if arr[dy][dx] == TAKEN:
                    taken += 1

            if taken >= 5 and arr[y][x] == TAKEN:
                new[y][x] = FREE
            elif taken == 0 and arr[y][x] == FREE:
                new[y][x] = TAKEN

    return new

def printr(arr):
    print('\n'.join([''.join(x) for x in arr]))
    print('---------------*--------------')

def visualize_neigbors(y,x, arr):
    new = deepcopy(arr)
    for dy, dx in neigh[y, x]:
        new[dy][dx] = 'O'
    printr(new)

if __name__=="__main__":

    FREE, FLOOR, TAKEN = 'L', '.', '#'

    with open('11.txt', 'r') as fp:
        arr = [[char for char in s.strip()] for s in fp]

    neigh = neighbors(arr)

    while True:
        new = part_one(arr)
        printr(new)
        if new == arr:
            break
        else:
            arr = deepcopy(new)
    print('finished')
    c = Counter('\n'.join([''.join(x) for x in arr]))
    print(c['#'])
