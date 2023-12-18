import numpy as np
from typing import Literal
import matplotlib.pyplot as plt

class day16:
    
    # (row_idx, col_idx)
    offsets: dict[str, tuple[int, int, str]] = {
        'n' : (-1, 0, 'n'),
        'e' : (0, 1, 'e'),
        's' : (1, 0, 's'),
        'w' : (0, -1, 'w')
    }
    
    next_tiles_offsets: dict[str, dict[str, tuple[tuple[int, int, str]]]] = {
        'n': {
            '.' : [offsets['n']],
            '|' : [offsets['n']],
            '-' : [offsets['w'], offsets['e']],
            '/' : [offsets['e']],
            '\\': [offsets['w']]
        },
        'e': {
            '.' : [offsets['e']],
            '|' : [offsets['n'], offsets['s']],
            '-' : [offsets['e']],
            '/' : [offsets['n']],
            '\\': [offsets['s']]
        },
        's': {
            '.' : [offsets['s']],
            '|' : [offsets['s']],
            '-' : [offsets['w'], offsets['e']],
            '/' : [offsets['w']],
            '\\': [offsets['e']]
        },
        'w': {
            '.' : [offsets['w']],
            '|' : [offsets['n'], offsets['s']],
            '-' : [offsets['w']],
            '/' : [offsets['s']],
            '\\': [offsets['n']]
        }
    }
    
    from_to = []
    
    def __init__(self):
        with open('input.txt') as f:
            lines = f.readlines()
        
        self.input = np.array([list(line.strip()) for line in lines])
        self.energized = [[[] for _ in range(self.input.shape[0])] for _ in range(self.input.shape[1])]
        
        self.beam(0, 0, 'e')
        
    def beam(self, row: int, column: int, dir: Literal['n', 'e', 'w', 's']) -> None:
        current_indeces = [(row, column, dir)]
        while len(current_indeces) > 0:
            next_indeces = []
            for row, column, dir in current_indeces:
                
                try:
                    if row < 0 or column < 0 or dir in self.energized[row][column]:
                        continue
                    self.energized[row][column].append(dir)
                except IndexError:
                    continue
                
                for row_offset, column_offet, next_dir in self.next_tiles_offsets[dir][self.input[row, column]]:
                    self.from_to.append(((row, column), (row_offset, column_offet)))
                    next_indeces.append((row + row_offset, column + column_offet, next_dir))
            
            current_indeces = next_indeces
            
    def visualize(self):
        for (y, x), (dy, dx) in self.from_to:
            plt.arrow(x, y, dx, dy, head_width=0.3, head_length=0.3, length_includes_head=True)
        
        
        plt.gca().set_xticks([i + 0.5 for i in range(0, self.input.shape[1] + 1)], minor=True)
        plt.gca().set_yticks([i + 0.5 for i in range(0, self.input.shape[0] + 1)], minor=True)
        plt.grid(True, which='minor', linestyle='-', linewidth=0.5)
        plt.xlim(-0.5, self.input.shape[1] - 0.5)
        plt.ylim(self.input.shape[0] - 0.5, -0.5)
        plt.show()
           
    
a = day16()
# a.visualize()

gsum = 0
for row in a.energized:
    for field in row:
        if len(field) > 0:
            gsum += 1

print(gsum)