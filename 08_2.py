def load_txt(inp):
    with open(inp, 'r') as fp:
        lines = fp.readlines()
        lines = [line.split(' ') for line in lines]
        out = [(instr, int(value)) for instr, value in lines]
    return out

def accumolator(code):
    visited = set()
    a = i = 0
    while i not in visited:
        if i == len(code):
            return True, a
        visited.add(i)
        instr, value = code[i]
        if instr == 'acc':
            a += value
            i += 1
        elif instr == 'jmp':
            i += value
        elif instr == 'nop':
            i += 1

    return False, a

code = load_txt('08.txt')
for i, v in enumerate(code):
    instr, value = v
    if instr == 'jmp':
        new = 'nop'
    elif instr == 'nop':
        new = 'jmp'
    else:
        continue
    b, a = accumolator([*code[:i], (new, value), *code[i+1:]])
    if b:
        print(f'Terminated! {a=}, {i=}, {new=}')
        break
    else:
        continue
    
