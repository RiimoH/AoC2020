import re


def compute_rule(rule):
    regex = r"(^|\d)(.+?)bag"

    matches = re.findall(regex, rule)
    bag = matches[0][1].strip()
    contains = dict([
        (s.strip(), int(v)) for v, s in matches[1:]
        ])

    return bag, contains
    
def search(bags, check, target):
    if bags[target] == {}:
        return 0
    
    if target in check:
        return check[target]

    total = 0
    for bag, amount in bags[target].items():
        count = search(bags, check, bag)
        total += amount + amount * count
        print(target, amount, count)

    check[target] = total
    return total

with open('07.txt', 'r') as fp:
##with open('test.txt', 'r') as fp:
    rules = fp.read().split('\n')

bags = {}
for rule in rules:
    bag, contains = compute_rule(rule)
    bags[bag] = contains

target = 'shiny gold'
success = []
count = 0
check = {}

print(search(bags, check, target))
print(check[target])
