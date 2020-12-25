from collections import defaultdict, Counter
from itertools import product

def set_value(mem, addr, val):
    if addr.count('X') == 0:
        mem[addr] = val
        return

    set_value(mem, addr.replace('X','0',1), val)
    set_value(mem, addr.replace('X','1',1), val)

if __name__ == '__main__':
    with open('14.txt', 'r') as fp:
        instr = fp.read().split('\n')
    mem = defaultdict(lambda: ['0']*36)

    for i in instr:
        if 'mask' in i:
            mask = {'1': [], 'X': []}
            for addr, char in enumerate(i.lstrip('mask = ')):
                if char != '0':
                    mask[char].append(addr)
        else:
            addr, val = i.lstrip('mem[').split('] = ')
            addr, val = list(bin(int(addr)).lstrip('0b').zfill(36)), int(val)

            for k, v in mask.items():
                for change in v:
                    addr[change] = k

            addr = ''.join(addr)

            set_value(mem, addr, val)


                
            
                
