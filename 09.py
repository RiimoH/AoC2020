from lib import load_txt, manipulate_self
from collections import deque
from itertools import combinations, accumulate
import timeit

def valid(running, check):
    for counter in running:
        if (check-counter) in running:
            return True
        else:
            continue
    return False

def part_one_1(arr):
    PREAMBLE = idx = 25
    running = deque(arr[:PREAMBLE])
    while valid(running, arr[idx]):
        running.popleft()
        running.append(arr[idx])
        idx += 1
    return idx

def part_one_2(arr):
    PREAMBLE = idx = 25
    while valid(arr[idx-PREAMBLE:idx], arr[idx]):
        idx += 1
    return idx

def part_one_3(arr):
    PREAMBLE = idx = 25
    while arr[idx] not in set(map(sum, combinations(arr[idx-PREAMBLE:idx], 2))):
        idx += 1
    return idx

## Part 2
def part_two_1(arr, idx):
    target = arr[idx]

    for i, v2 in enumerate(arr[1:], start=1):
        v1 = arr[i-1]
        lsum = v1 + v2
        li = i + 1
        while lsum < target:
            lsum += arr[li]
            li += 1
        if lsum == target:
            sub = arr[i-1:li]
            tsum = min(sub) + max(sub)
            return tsum
        else:
            continue
    return 0

def part_two_2(arr, target):
    i1, i2 = 0, 1
    while (s := sum(arr[i1:i2])) != target:
        if s < target:
            i2 += 1
        elif s > target:
            i1 += 1
    return min(arr[i1:i2]) + max(arr[i1:i2])

if __name__=="__main__":
    arr = load_txt('09.txt', t=int, ot=list)
    num = 1
    rep = 100
    t11 = min(timeit.repeat("part_one_1(arr)", globals=globals(), number=num, repeat=rep))/num #&11 0.0009933000000000303 s
    t12 = min(timeit.repeat("part_one_2(arr)", globals=globals(), number=num, repeat=rep))/num #&12 0.001060000000000061 s
    t13 = min(timeit.repeat("part_one_3(arr)", globals=globals(), number=num, repeat=rep))/num #&13 2.920000000006251e-05 s
    idx = part_one_3(arr)
    num = 1
    rep = 100
    t21 = min(timeit.repeat("part_two_1(arr, idx)", globals=globals(), number=num, repeat=rep))/num #&21 8.499999999966867e-06 s
    t22 = min(timeit.repeat("part_two_2(arr, arr[idx])", globals=globals(), number=num, repeat=rep))/num #&22 5.200000000038507e-06 s

    manipulate_self(__file__, '11', str(t11) + ' s')
    manipulate_self(__file__, '12', str(t12) + ' s')
    manipulate_self(__file__, '13', str(t13) + ' s')
    manipulate_self(__file__, '21', str(t21) + ' s')
    manipulate_self(__file__, '22', str(t22) + ' s')

    
