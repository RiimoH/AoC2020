from d22 import player
from collections import deque
from timeit import timeit

for k, v in player.items():
    player[k] = deque(iterable=v)


def combat(one, two):
    archive = set()

    while (tuple(one), tuple(two)) not in archive:
        archive.add((tuple(one), tuple(two)))

        o = one.popleft()
        t = two.popleft()

        if o <= len(one) and t <= len(two):
            win =  combat(deque(list(one)[:o]), deque(list(two)[:t]))
        else:
            win = o > t
        
        if win:
            one.append(o)
            one.append(t)
        else:
            two.append(t)
            two.append(o)

        if len(one) == 0 or len(two) == 0:
            return len(one) > len(two)

    return True


# while len(player['one']) > 0 and len(player['two']) > 0:
#     o = player['one'].popleft()
#     t = player['two'].popleft()

#     if o > t:
#         player['one'].append(o)
#         player['one'].append(t)
#     else:
#         player['two'].append(t)
#         player['two'].append(o)


t = timeit(stmt="combat(player['one'], player['two'])", number=1, globals=globals())
print(t)
win = combat(player['one'], player['two'])

winning_deck = player['one'] if win else player['two']
winning_deck = reversed(list(winning_deck))
score = 0
for i, v in enumerate(winning_deck, start=1):
    score += i*v
print(score)