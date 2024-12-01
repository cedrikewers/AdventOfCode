import re

max = {
    'red': 12,
    'green': 13,
    'blue': 14
}

with open('input.txt') as f:
    lines = f.readlines()

sum = (len(lines) * (len(lines) + 1)) // 2

for index, line in enumerate(lines):
    line = line.strip()
    line = line.replace(f'Game {index+1}: ', '')
    draws = line.split(';')
    for draw in draws:
        isvalid = True
        cdraws = draw.split(',')
        for cdraw in cdraws:
            res = re.search(r' ?([0-9]+) (red|green|blue)', cdraw)
            num = int(res.group(1))
            color = res.group(2)

            if num > max[color]:
                print(f'Game {index+1}: is not possible because there are {num} {color} cubes in the draw, but only {max[color]} are allowed.')
                sum -= index + 1
                isvalid = False
                break
        if not isvalid:
            break
    
print(f'Sum: {sum}')