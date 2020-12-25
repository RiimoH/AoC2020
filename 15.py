from collections import defaultdict


def part_one(arr):
    d = defaultdict(list)
    for i, num in enumerate(arr, start=1):
        d[num].append(i)
        last = num

    for i in range(len(arr)+1, 30000001):
        if len(d[last]) < 2:
            last = 0
        else:
            last = d[last][-1] - d[last][-2]
        d[last].append(i)
    return last
    

if __name__ == '__main__':
    with open('15.txt', 'r') as fp:
        arr = list(map(int, fp.read().split(',')))

    print(part_one([0,3,6]) == 175594)
    print(part_one(arr))
