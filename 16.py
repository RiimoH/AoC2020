import re
from collections import defaultdict
from itertools import chain
from math import prod
from copy import deepcopy


def parse_limits(limits):
    d = defaultdict(list)
    for limit in limits:
        regex = r'(.+): (\d+)-(\d+) or (\d+)-(\d+)'

        grps = re.findall(regex, limit)
        if grps:
            grps = grps[0]
            d[grps[0]] = [*[x for x in range(int(grps[1]), int(grps[2])+1)],
                          *[x for x in range(int(grps[3]), int(grps[4])+1)]]
    return d


def parse_ticket(ticket):
    return list(map(int, ticket[0].split(',')))


def parse_other_tickets(other_tickets):
    tmps = [t.split(',') for t in other_tickets]
    return list(list(map(int, tmp)) for tmp in tmps)


def check_for_invalids(limits, other_tickets):
    valid_numbers = set(chain.from_iterable(limits.values())) # all valid values ever
    other_tickets_numbers = list(chain.from_iterable(other_tickets)) # all available values ever
    invalid = list(filter(lambda x: x not in valid_numbers, other_tickets_numbers)) # filter out all values that are available but not valid
    return sum(invalid), valid_numbers


def conclude_classes(classes, valid_tickets, limits):
    for valid_ticket in valid_tickets:
        for i, v in enumerate(valid_ticket):
            for k, l in limits.items():
                if v not in l:
                    classes[i].remove(k)


if __name__ == '__main__':
    with open('16.txt', 'r') as fp:
        txt = fp.read().split('\n')

    target = limits = []
    ticket = []
    other_tickets = []
    for line in txt:
        if line == 'your ticket:':
            target = ticket
            continue
        elif line == 'nearby tickets:':
            target = other_tickets
            continue
        elif line == '':
            continue

        target.append(line)

    limits = parse_limits(limits) # dict: key=name, value=list of int
    ticket = parse_ticket(ticket) # list of int
    other_tickets = parse_other_tickets(other_tickets) # list of lists of int

    sum_invalids, valid_numbers = check_for_invalids(limits, other_tickets)
    print(sum_invalids) # Part 01

    
    valid_tickets = []
    for other_ticket in other_tickets:
        if all(map(lambda num: num in valid_numbers, other_ticket)):
            valid_tickets.append(other_ticket)
        else:
            pass
    classes = [{*limits.keys()} for x in range(len(valid_tickets[0]))]
    conclude_classes(classes, valid_tickets, limits)

        
    taken = set()
    new_taken = set()
    changed = True
    defined = {}

    while changed:
        classes = [x - taken if type(x) == set else x for x in classes]
        classes = [next(iter(x)) if len(x) == 1 and type(x) == set else x for x in classes]
        for i, c in enumerate(classes):
            if type(c) == str:
                defined[c] = i
                new_taken.add(c)
        
        if new_taken == taken:
            changed = False
        else:
            taken = new_taken
            new_taken = set()


    target_values = [ticket[classes.index(x)] for x in classes if x.startswith('departure')]
    print(prod(target_values))
