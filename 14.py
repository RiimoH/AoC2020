from collections import defaultdict

if __name__ == '__main__':
    with open('14.txt', 'r') as fp:
        instr = fp.read().split('\n')
    mem = defaultdict(lambda: ['0']*36)

    for i in instr:
        if 'mask' in i:
            mask = {'1': [], '0': []}
            for idx, char in enumerate(i.lstrip('mask = ')):
                if char != 'X':
                    mask[char].append(idx)
        else:
            idx, val = i.lstrip('mem[').split('] = ')
            idx, val = int(idx), list(bin(int(val)).lstrip('0b').zfill(36))
            for k, v in mask.items():
                for change in v:
                    val[change] = k

            mem[idx] = int(''.join(val), 2)

    print(mem)
    print(sum(mem.values()))
                
            
                
