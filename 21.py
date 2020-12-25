import array
from collections import Counter


test = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
"""

test = """dxfdxt vgufpnya kec avjmt (contains fish)
toumfvc avjmt (contains fish, soy)
qkecxpe dxfdxt xsqfsxl toumfvc (contains soy)"""

def part_one(txt):
    lines = txt.rstrip().split('\n')

    a = {}
    f = set()
    for line in lines:
        foods, allergens = line.split(' (contains ')
        foods = set(foods.split(' '))
        f.update(foods)
        allergens = allergens.rstrip(')').split(', ')
        for allergen in allergens:
            if allergen not in a.keys():
                a[allergen] = foods.copy()
            else:
                a[allergen].intersection_update(foods)
    
    while True:
        if not any({x for x in a if len(a[x]) > 1}):
            break
        for b in {y for y in a if len(a[y]) > 1}:
            for c in {x for x in a if len(a[x]) == 1}:
                a[b] -= a[c]

    return a, f, f.difference({list(x)[0] for x in a.values()})

def part_two(inhalt):
    x = []
    for k, v in inhalt.items():
        x.append((k,v))
    x.sort()
    sol = ','.join([list(y[1])[0] for y in x])
    print(sol)

if __name__ == '__main__':

    # txt = test
    with open('21.txt') as fp:
        txt = fp.read()

    inhalt, foods, dif = part_one(txt)
    s = 0
    for f in dif:
        c = txt.count(f + ' ')
        print(f'{f=}: {c}')
        s += c
    print(s)

    part_two(inhalt)
