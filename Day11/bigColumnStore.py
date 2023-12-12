import numpy as np
from itertools import combinations

with open('input.txt') as f:
    lines = f.readlines()


universe = []
galaxy_count = 0
for line in lines:
    row = []
    for c in line.strip():
        if c == '#':
            galaxy_count += 1
            row.append(galaxy_count)
        else:
            row.append(0)
    universe.append(row)

universe = np.array(universe)
universe = np.insert(universe, np.where(np.all(universe == 0, axis=0))[0], 0, axis=1)
universe = np.insert(universe, np.where(np.all(universe == 0, axis=1))[0], 0, axis=0)

distances = []
for (x1, y1), (x2, y2) in combinations(zip(*np.where(universe > 0)), 2):
    distance = np.abs(x1 - x2) + np.abs(y1 - y2)
    distances.append(distance)
    
print(sum(distances))