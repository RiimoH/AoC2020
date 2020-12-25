import re


def compute_rule(rule):
    regex = r"(^|\d)(.+?)bag"

    matches = re.findall(regex, rule)
    bag = matches[0][1].strip()
    contains = dict([
        (s.strip(), int(v)) for v, s in matches[1:]
        ])

    return bag, contains
    
def search(bags, bag, target, visited):
    visited.append(bag)

    if bag == target:
        print(' > '.join(visited))
        return visited
    elif bag in success:
        print(' > '.join(visited), 'success')
        return visited
    
    for new_bag in bags[bag]:
        if (depth := search(bags, new_bag, target, visited[:])):
            return depth
        else:
            continue

    return False

with open('07.txt', 'r') as fp:
    rules = fp.read().split('\n')

bags = {}
for rule in rules:
    bag, contains = compute_rule(rule)
    bags[bag] = contains

target = 'shiny gold'
success = []

for bag in bags:
    if bag not in success:
        if (visited := search(bags, bag, target, [])):
            success += visited

success = set(success)
success.remove(target)
print(len(success))
print(success)
