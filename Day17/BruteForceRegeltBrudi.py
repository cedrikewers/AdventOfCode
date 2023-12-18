import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from itertools import product
from functools import reduce

ORIENTARIONS = ['n', 'e', 's', 'w']
def next_nodes(row, column, same_direction_count, orientation):
    if same_direction_count < 3:
        match orientation:
            case 'n':
                return [(row - 1, column, same_direction_count + 1, 'n')]
            case 'e':
                return [(row, column + 1, same_direction_count + 1, 'e')]
            case 's':
                return [(row + 1, column, same_direction_count + 1, 's')]
            case 'w':
                return [(row, column - 1, same_direction_count + 1, 'w')]    
    
                
    match orientation:
        case 'n':
            return (
                (row - 1, column, same_direction_count + 1, 'n'),
                (row, column + 1, 0, 'e'),
                (row, column - 1, 0, 'w'),
            )
        case 'e':
            return (
                (row, column + 1, same_direction_count + 1, 'e'),
                (row - 1, column, 0, 'n'),
                (row + 1, column, 0, 's'),
            )
        case 's':
            return (
                (row + 1, column, same_direction_count + 1, 's'),
                (row, column + 1, 0, 'e'),
                (row, column - 1, 0, 'w'),
            )
        case 'w':
            return (
                (row, column - 1, same_direction_count + 1, 'w'),
                (row - 1, column, 0, 'n'),
                (row + 1, column, 0, 's'),
            )

with open("input.txt") as f:
    lines = f.readlines()

input = np.array([[int(c) for c in line.strip()] for line in lines])

G = nx.DiGraph()

nodes = list((
    (row, column, same_direction_count, orientation) for 
    (row, column), same_direction_count, orientation in 
    product(np.ndindex(input.shape), range(11), ('n', 'e', 's', 'w'))
))

G.add_nodes_from(nodes)
for row, column, same_direction_count, orientation in nodes:
    if same_direction_count == 10 or row < 0 or column < 0:
        continue
    
    try:
        weight = input[row, column]
    except IndexError:
        continue
    
    for next_row, next_column, next_same_direction_count, next_orientation in next_nodes(row, column, same_direction_count, orientation):
        if next_row < 0 or next_column < 0 or next_row > input.shape[0] - 1 or next_column > input.shape[1] - 1:
            continue
        G.add_weighted_edges_from([
            (
                (row, column, same_direction_count, orientation),
                (next_row, next_column, next_same_direction_count, next_orientation),
                weight
            )
        ])

path_lens = []
paths = []    
for start, end_dir, same_direction_count in product(((0, 1, 1, 'e'), (1, 0, 1, 'n')), ('s', 'e'), range(4, 10)):
    try:
        sp = nx.shortest_path(G, start, (input.shape[0] - 1, input.shape[1] - 1, same_direction_count, end_dir), weight='weight')
    except nx.NetworkXNoPath:
        continue
    path_lens.append(reduce(lambda a, b: a + input[b[0], b[1]], sp, 0))
    paths.append(sp)
    
print(min(path_lens))

min_path = paths[np.argmin(path_lens)]

plt.arrow(0, 0, min_path[0][1], min_path[0][0], head_width=0.3, head_length=0.3, length_includes_head=True)
for a, b in zip(min_path, min_path[1:]):
    plt.arrow(a[1], a[0], b[1] - a[1], b[0] - a[0], head_width=0.3, head_length=0.3, length_includes_head=True)
    
    
plt.gca().set_xticks([i + 0.5 for i in range(0, input.shape[1] + 1)], minor=True)
plt.gca().set_yticks([i + 0.5 for i in range(0, input.shape[0] + 1)], minor=True)
plt.grid(True, which='minor', linestyle='-', linewidth=0.5)
plt.xlim(-0.5, input.shape[1] - 0.5)
plt.ylim(input.shape[0] - 0.5, -0.5)
plt.show()