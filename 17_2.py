from itertools import product

DIF = {*product([1,0,-1], repeat=4)} - {(0,0,0,0)}

def parse_input(txt):
    lines = txt.strip('\n').split('\n')
    space = {}
    for y, line in enumerate(lines):
        for x, cell in enumerate(line):
            space[(x, y, 0, 0)] = 1 if cell == '#' else 0
    return space


def increase_size(space):
    W, X, Y, Z = zip(*space.keys())
    w1, w2 = min(W), max(W)
    x1, x2 = min(X), max(X)
    y1, y2 = min(Y), max(Y)
    z1, z2 = min(Z), max(Z)
    for m in range(x1-1, x2+2):
        for n in range(y1-1, y2+2):
            for o in range(z1-1, z2+2):
                for p in range(w1-1, w2+2):
                    if (p,m,n,o) not in space.keys():
                        space[(p,m,n,o)] = 0
    

def check_cubes(starting_space, c):
    if c == 0:
        return starting_space

    increase_size(starting_space)
    new_space = {}
    for k, v in starting_space.items():
        neighbors = [(k[0]+dw,
            k[1]+dx,
            k[2]+dy,
            k[3]+dz) for dw, dx, dy, dz in DIF] # liste aller nachbarn
        
        new = [starting_space.get(n, 0) for n in neighbors] # resultat der nachbarn

        if (v == 1 and sum(new) in [2,3]) or (v == 0 and sum(new) == 3):
            new_space[k] = 1
        else:
            new_space[k] = 0

    return check_cubes(new_space, c-1)


if __name__ == '__main__':
    with open('17.txt') as fp:
        txt = fp.read()
    starting_space = parse_input(txt)
    print(starting_space)
    space = check_cubes(starting_space, 6)

    print(sum(space.values()))