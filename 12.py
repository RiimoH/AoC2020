

class Boat():
    def __init__(self):
        self.cx = self.cy = 0
        self.VEC = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}
        self.DIR = ['N', 'E', 'S', 'W']
        self.cd = 1

    def move(self, instr):
        md, mv = instr

        if md == 'F':
            md = self.DIR[self.cd]

        if md in self.DIR:
            self.cx += self.VEC[md][0] * mv
            self.cy += self.VEC[md][1] * mv
        else:
            VECf = 1 if md == 'R' else -1
            turn = int(mv/90)
            self.cd += VECf * turn 
            if 3 < self.cd or self.cd < 0: 
                self.cd = int(self.cd % 4)
    
    def repr(self):
        print(f'Current Position: {self.cx} | {self.cy}')
        print(f'Current Manhattan-Distance: {abs(self.cx) + abs(self.cy)}')


if __name__=="__main__":

    with open('12.txt', 'r') as fp:
        instr = [(line[0], int(line[1:].strip())) for line in fp]

    ferry = Boat()
    for i in instr:
        ferry.move(i)
        ferry.repr()