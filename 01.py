from itertools import combinations
from math import prod
from lib import load_txt

def one(inp, num, target):
    for comb in combinations(inp, num):
        if sum(comb) == target:
            return prod(comb)

if __name__ == '__main__':
    inp = load_txt('01inp.txt', t=int, ot=set)
    print(f'2 Values: {one(inp, 2, 2020)}\n3 Values: {one(inp, 3, 2020)}')
