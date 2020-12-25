import re

def evaluate(term):
    term = term.group() if type(term) != str else term
    add = r"(\d+ \+ \d+)+"
    while re.search(add, term):
        term = re.sub(add, eval_add, term)
    num = 0
    op = '+'
    term = term.lstrip('(').rstrip(')').split(' ')
    for x in term:
        if x not in ['+', '/', '*', '-']:
            num = eval(f'{num}{op}{x}')
        else:
            op = x
    return str(num)

def eval_add(term):
    term = term.group() if type(term) != str else term
    term = term.lstrip('(').rstrip(')').split(' ')
    return str(int(term[0])+int(term[2]))

def scan(term):
    braces = r"\([\d\+\*\-\\\s]+\)+?"
    
    while '(' in term:
        term = re.sub(braces, evaluate, term)
    
    term = evaluate(term)
    return term

if __name__ == '__main__':
    t = ["1 + 2 * 3 + 4 * 5 + 6",
    "1 + (2 * 3) + (4 * (5 + 6))",
    "2 * 3 + (4 * 5)",
    "5 + (8 * 3 + 9 + 3 * 4 * 3)",
    "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))",
    "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"]

    with open('18.txt') as fp:
        t = fp.read().split('\n')

    results = [int(scan(term)) for term in t]
    print(results)
    print(sum(results))
