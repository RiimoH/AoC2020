from math import sin, cos
from math import radians as rad

class Boat():
    def __init__(self):
        self.cx = self.cy = 0
        self.wpx = 10
        self.wpy = -1
        self.VEC = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}
        self.DIR = ['N', 'E', 'S', 'W']

    def move(self, instr):
        md, mv = instr

        if md == 'F':
            #moves ship forward
            self.cx += self.wpx * mv
            self.cy += self.wpy * mv
        elif md in self.DIR:
            #moves waypoint
            self.wpx += self.VEC[md][0] * mv
            self.wpy += self.VEC[md][1] * mv
        else:
            #rotate waypoint
            if md == 'L':
                mv = -mv
            beta = rad(mv)
            self.wpx, self.wpy = cos(beta)*self.wpx - sin(beta)*self.wpy, sin(beta)*self.wpx + cos(beta)*self.wpy
    
    def repr(self):
        print(f'Current Position: {self.cx} | {self.cy}')
        print(f'Current Waypoint: {self.wpx} | {self.wpy}')
        print(f'Current Manhattan-Distance: {abs(self.cx) + abs(self.cy)}')


if __name__=="__main__":

    with open('12.txt', 'r') as fp:
        instr = [(line[0], int(line[1:].strip())) for line in fp]

    ferry = Boat()
    for i in instr:
        print(i)
        ferry.move(i)
        ferry.repr()