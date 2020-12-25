from data23 import test, puzzle
from tqdm import tqdm
import time

startTime = time.time()

inp = list(map(int, list(puzzle)))

MAX = 1_000_000

cups = {inp[i]: inp[i+1] for i in range(len(inp) - 1)}
cups[inp[-1]] = max(inp)+1
for k in range(max(inp)+1, MAX):
    cups[k] = k+1
cups[MAX] = inp[0]

current = inp[0]

setupTime = time.time()

for _ in range(10_000_000):
    destination = current - 1
    pickup = []

    n = current
    for _ in range(3):
        pickup.append(cups.get(n))
        n = pickup[-1]
    
    cups[current] = cups.get(n)

    while destination in pickup or destination <= 0:
        destination -= 1
        if destination <= 0:
            destination = MAX
    
    # print(f'D:{destination}, P:{pickup}, N:{current}, Cups:{cups}')
    current = cups[current]
    cups[pickup[2]] = cups.get(destination)
    cups[destination] = pickup[0]

# sol = ''
# n = 1
# while True:
#     n = cups[n]
#     if n == 1:
#         break
#     sol += str(n)

# print(f'Part 1: {sol}')

endTime = time.time()

n = 1
x1 = cups[n]
x2 = cups[x1]
sol = x1 * x2

print(f'Part 2: {x1} * {x2} = {sol}')
print(f'Setup: {setupTime - startTime}, Loop: {endTime - setupTime}, Total: {endTime - startTime}')

# class Cup():
#     def __init__(self, id, next):
#         self.id = id
#         self.next = next


# def round(inp):
#     pickup = [inp.pop(1) for x in range(3)]

#     destination = inp[0] -1
#     while destination not in inp:
#         destination -= 1
#         if destination <= 0:
#             destination = 9

#     i_destination = inp.index(destination)
#     for i, p in enumerate(pickup, start=1):
#         inp.insert(i_destination + i, p)

#     # move current
#     inp.append(inp.pop(0))
#     return inp

# for run in tqdm(range(1, 1_000_001)):
#     test = round(test)

# print(f"{''.join(map(str, test))}")

# # x = ''.join(map(str, test)).split('1')
# # print(x)
# # x = x[1] + x[0]
# # print(x)

# i = test.index(1)
# print(test[i+1]*test[i+2])