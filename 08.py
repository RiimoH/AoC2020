

class BootCode():
    def __init__(self, inp, acc = 0, curr = 0, visited = []):
        self.code = self.load_txt(inp)
        self.acc = acc
        self.curr = curr
        self.visited = visited


    def load_txt(self, txt):
        with open(txt, 'r') as fp:
            lines = fp.readlines()
            lines = [line.split(' ') for line in lines]
            out = [(instr, int(value)) for instr, value in lines]
            out.append(('trm', 0))
        return out

    def run(self):
        instr, value = self.code[self.curr]
        print(f'{instr=}, {value=}')
        if instr == 'acc':
            self.acc += value
            self.curr += 1
        elif instr == 'jmp':
            self.curr += value
        elif instr == 'nop':
            self.curr += 1
        elif instr == 'trm':
            print('Terminated! {acc=}')
            return False
        else:
            print(f'Not implemented: {instr}')
            return False
        print(f'{self.acc=}, {self.curr=}')
        return True
        
    def check(self):
        if self.curr not in self.visited:
            self.visited.append(self.curr)
            return True
        else:
            print(f'Infinite Loop! {self.acc=}')
            return False

    def main(self):
        while self.check():
            if not self.run():
                break

bc = BootCode('08.txt')
bc.main()
