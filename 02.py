import re
from lib import read_txt

lines = read_txt('02.txt', item_type=str, array_type=list)

def check_valid(match):
    # lower_bounds, higher_bounds, target, string = match.groups()
    # return int(lower_bounds) <= string.count(target) <= int(higher_bounds)

    first, second, target, string = match.groups()

    b = [string[int(first)-1] == target, string[int(second)-1] == target]
    return b.count(True) == 1

regex = r"(\d+)-(\d+)\s([a-z]):\s(.+)"
matches = [re.search(regex, x) for x in lines]

filtered = list(filter(check_valid, matches))
print(len(filtered))