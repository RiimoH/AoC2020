from collections import Counter, defaultdict
from copy import deepcopy

def neighbors(len_y, len_x):
    d = defaultdict(list)

    dif = (
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
            for dy, dx in dif:
                if len_y > y+dy >= 0 and len_x > x+dx >= 0:
                    d[(y, x)].append((y+dy, x+dx))
    
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

            if taken >= 4 and arr[y][x] == TAKEN:
                new[y][x] = FREE
            elif taken == 0 and arr[y][x] == FREE:
                new[y][x] = TAKEN

    return new

def printr(arr):
    print('\n'.join([''.join(x) for x in arr]))
    print('---------------*--------------')

if __name__=="__main__":

    FREE, FLOOR, TAKEN = 'L', '.', '#'

    with open('11.txt', 'r') as fp:
        arr = [[char for char in s.strip()] for s in fp]

    neigh = neighbors(len(arr), len(arr[0]))

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
