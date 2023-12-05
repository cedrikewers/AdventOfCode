import re
import functools

with open('input.txt') as f:
    lines = f.readlines()

gprod = 0

for index, line in enumerate(lines):
    line = line.strip()
    line = line.replace(f'Game {index+1}: ', '')
    draws = line.split(';')
    maxs = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
    for draw in draws:
        cdraws = draw.split(',')
        for cdraw in cdraws:
            res = re.search(r' ?([0-9]+) (red|green|blue)', cdraw)
            num = int(res.group(1))
            color = res.group(2)

            if num > maxs[color]:
                maxs[color] = num
            
    
            #print(f'Game {index+1}: is not possible because there are {num} {color} cubes in the draw, but only {max[color]} are allowed.')

    prod = functools.reduce(lambda a, b: a * b, maxs.values())
    gprod += prod
    
print(f'pgrod: {gprod}')