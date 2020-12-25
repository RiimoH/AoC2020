from timeit import timeit

def bus(bus):
    return (target // bus + 1) * bus - target


def solve2(busses):
    print(busses)
    busses = [(start, int(bus)) for start, bus in enumerate(busses) if bus != 'x']
    timestep = 0
    lcm = 1
    for start, step in busses:
        while (timestep + start) % step != 0:
            timestep += lcm
        lcm *= step
    return timestep
    
if __name__ == '__main__':
    with open('13.txt', 'r') as fp:
        t = fp.read()

    target, busses = t.split('\n')
    target = int(target)
    busses = busses.split(',')


    # --- Part 2 ---
    x = solve2(busses)
    print(solve2([17,'x',13,19]) == 3417)
    print(solve2([67,7,'x',59,61]) == 1261476)
    print(solve2([1789,37,47,1889]) == 1202161486)
    print(x)
