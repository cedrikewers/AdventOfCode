import re
from functools import reduce

with open("input.txt") as f:
    lines = f.readlines()
    
empty_index = lines.index("\n")
workflows = {}
for line in lines[:empty_index]:
    m = re.match(r"^([a-z]+)\{(.+)\}$", line)
    identifier = m.group(1)
    workflows[identifier] = []
    rules = m.group(2).split(",")
    for rule in rules:
        m = re.match(r"(a|s|m|x)(<|>)(\d+):([a-z]+|A|R)", rule)
        if not m:
            workflows[identifier].append(rule)
        else:
            workflows[identifier].append([
                m.group(1),
                m.group(2),
                int(m.group(3)),
                m.group(4)
            ])

parts = []
for line in lines[empty_index+1:]:
    m = re.match(r"{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}", line)
    parts.append({
        'x': int(m.group(1)),
        'm': int(m.group(2)),
        'a': int(m.group(3)),
        's': int(m.group(4))
    })

def check_part(part: dict, workflow: tuple[str, str, int, str] | str):
    for [attr, comp, val, next] in workflow[:-1]:
        if (comp == '<' and part[attr] < val) or (comp == '>' and part[attr] > val):
            match next:
                case 'A':
                    return part
                case 'R':
                    return -1
                case _:
                    return next
    match workflow[-1]:
        case 'A':
            return part
        case 'R':
            return -1
        case _:
            return workflow[-1]
                    
accepted_parts = []

for part in parts:
    result = 'in'
    while type(result) not in (dict, int):
        result = check_part(part, workflows[result])
    if type(result) == dict:
        accepted_parts.append(result)
        
    
print(reduce(lambda a, b: a + sum(b.values()), accepted_parts, 0))