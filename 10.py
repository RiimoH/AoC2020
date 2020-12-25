from lib import load_txt, manipulate_self
from functools import lru_cache
import timeit

def part_one(adapters, idx, last):
    if idx == len(adapters):
        return {3: 1, 2: 0, 1: 0}

    lower = part_one(adapters, idx+1, adapters[idx])
    dif = adapters[idx] - last
    lower[dif] += 1
    return lower

@lru_cache(maxsize=None)
def idxs(adapters, idx):
    vals = [adapters[idx] + i for i in range(1, 4)]
    idxs = set([adapters.index(val) for val in vals if val in adapters])
    return idxs

@lru_cache(maxsize=None)
def part_two(adapters, idx):
    if adapters[idx] == max(adapters):
        return 1
    ways = 0
    for idx in idxs(adapters, idx):
        ways += part_two(adapters, idx)
    return ways
        
if __name__=="__main__":
    adapters = tuple([0, *sorted(load_txt('10.txt', t=int, ot=list))])

    num = 1
    rep = 100
    t11 = min(timeit.repeat("part_one(adapters, 1, 0)", globals=globals(), number=num, repeat=rep))/num #&11 3.8599999999999746e-05 s
    d = part_one(adapters, 1, 0)
    print(t11)
    print(d[3] * d[1])
    t21 = min(timeit.repeat("part_two(adapters, 0)", globals=globals(), number=num, repeat=rep))/num #&21 3.999999999559911e-07 s
    w = part_two(adapters, 0)
    print(t21)
    print(w)
    manipulate_self(__file__, '11', str(t11) + ' s')
    manipulate_self(__file__, '21', str(t21) + ' s')
