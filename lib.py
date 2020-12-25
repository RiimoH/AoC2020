import re

def load_txt(txt, t=int, ot=list):
    with open(txt, 'r') as fp:
        inp = ot(map(t, fp.readlines()))
    return inp

def manipulate_self(path, mid, content, separator='#&'):
    path = str(path)
    mid = str(mid)
    content = str(content)
    with open(path, 'r') as fp:
        txt = fp.readlines()
    regex = fr"{separator}{mid}.*$"
    subst = f"{separator}{mid} {content}"

    new = []
    for line in txt:
        new.append(re.sub(regex, subst, line))
    with open(path, 'w') as fp:
        fp.writelines(new)
