import numpy as np

with open('input.txt') as f:
    lines = f.readlines()
    
input = np.array([list(line.strip()) for line in lines])
for column_idx in range(input.shape[1]):    
    for row_idx in range(1, input.shape[0]):
        if input[row_idx, column_idx] == 'O':
            for i in range(row_idx, 0, -1):
                if input[i-1, column_idx] == '.':
                    input[i-1, column_idx] = 'O'
                    input[i, column_idx] = '.'
                else:
                    break

gload = 0
for row_idx, column_idx in zip(*np.where(input == 'O')):
    gload += input.shape[0] - row_idx

print(gload)