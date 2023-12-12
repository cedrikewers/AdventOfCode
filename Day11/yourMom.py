import numpy as np
from itertools import combinations

with open('input.txt') as f:
    lines = f.readlines()
    
universe = np.array([[c == '#' for c in line.strip()] for line in lines])

galaxies = list(zip(*np.where(universe)))
empty_cols = np.where(np.all(universe == False, axis=0))[0]
empty_rows = np.where(np.all(universe == False, axis=1))[0]

for index, (y, x) in enumerate(galaxies):
    empty_columns_smaller = np.count_nonzero(empty_cols < x)
    empty_rows_smaller = np.count_nonzero(empty_rows < y)
    
    new_pos = (x + empty_columns_smaller*999999, y + empty_rows_smaller*999999)
    
    galaxies[index] = new_pos
    
distances = []
for (y1, x1), (y2, x2) in combinations(galaxies, 2):
    distance = np.abs(x1 - x2) + np.abs(y1 - y2)
    distances.append(distance)

print(sum(distances))