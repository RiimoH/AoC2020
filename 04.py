import re

def read_txt(file, ft, at):
    with open(file, 'r') as fp:
        txt = at(map(ft, fp.read().split('\n')))
        return txt

def validate_passport(d):
    #verify if all keys are there
    if not (set(new_dict.keys()) == {'byr','iyr','eyr','hgt','hcl','ecl','pid'} or set(new_dict.keys()) == {'byr','iyr','eyr','hgt','hcl','ecl','pid','cid'}):
        print('failed keys')
        return False

    # validate byr
    if not 1920 <= int(d['byr']) <= 2002:
        print(f"failed {d['byr']=}")
        return False

    # validate iyr
    if not 2002 <= int(d['iyr']) <= 2020:
        print(f"failed {d['iyr']=}")
        return False
        
    # validate eyr
    if not 2020 <= int(d['eyr']) <= 2030:
        print(f"failed {d['eyr']=}")
        return False  

    # validate hgt
    reg = r"(\d+)(in|cm)"
    if not (match := re.search(reg, d['hgt'])):
        print(f"failed {d['hgt']=}")
        return False
    else:
        if match.groups()[1] == 'cm' and not 150 <= int(match.groups()[0]) <= 193:
            print(f"failed {d['hgt']=}")
            return False
        elif match.groups()[1] == 'in' and not 59 <= int(match.groups()[0]) <= 76:
            print(f"failed {d['hgt']=}")
            return False

    # validate hcl
    reg = r"#[0-9a-f]{6}"
    if not re.search(reg, d['hcl']):
        print(f"failed {d['hcl']=}")
        return False

    # validate ecl
    if d['ecl'] not in 'amb blu brn gry grn hzl oth'.split(' '):
        print(f"failed {d['ecl']=}")
        return False

    # validate pid
    reg = r"^[0-9]{9}$"
    if not re.search(reg, d['pid']):
        print(f"failed {d['pid']=}")
        return False

    return True

arr = read_txt('04.txt', str, list)
new_arr = []
new_dict = {}
failed = 0
success = 0
for i, entry in enumerate(arr):
    if entry == '':
        new_arr.append(new_dict)
        if validate_passport(new_dict):
            success += 1
        else:
            failed += 1
            
        new_dict = {}
    else:
        new_dict.update(dict(map(lambda x: x.split(':'), entry.split(' '))))
new_arr.append(new_dict)
if validate_passport(new_dict):
    success += 1
else:
    failed += 1


print(failed, success)
