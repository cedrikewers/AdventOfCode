import numpy as np
from functools import reduce

with open('input.txt') as f:
    lines = f.readlines()
    
input = np.array([list(line.strip()) for line in lines])
memory = {hash(input.data.tobytes()): 0}

def rotation():
    # shift north
    for row_idx, column_idx in zip(*np.where(input == 'O')):
        for i in range(row_idx, 0, -1):
            if input[i-1, column_idx] == '.':
                input[i-1, column_idx] = 'O'
                input[i, column_idx] = '.'
            else:
                break    
    #shift west
    for row_idx, column_idx in zip(*np.where(input == 'O')):
        for i in range(column_idx, 0, -1):
            if input[row_idx, i-1] == '.':
                input[row_idx, i-1] = 'O'
                input[row_idx, i] = '.'
            else:
                break
    #shift south
    idxs = np.where(input == 'O')
    for row_idx, column_idx in zip(idxs[0][::-1], idxs[1][::-1]):
        for i in range(row_idx, input.shape[0] - 1):
            if input[i+1, column_idx] == '.':
                input[i+1, column_idx] = 'O'
                input[i, column_idx] = '.'
            else:
                break
    #shift east
    idxs = np.where(input == 'O')
    for row_idx, column_idx in zip(idxs[0][::-1], idxs[1][::-1]):        
        for i in range(column_idx, input.shape[1] - 1):
            if input[row_idx, i+1] == '.':
                input[row_idx, i+1] = 'O'
                input[row_idx, i] = '.'
            else:
                break

second_loop_cnt = 0
for _ in range(10000):
    
    rotation()

    h = hash(input.data.tobytes())
    if h in memory:
        print(f"State {_} is the same as state {memory[h]}. There is a loop every {_ - memory[h]} steps starting at {memory[h]}.\nWe only need to do {(int(1e9) - _ -  1) % (_ - memory[h])} more steps.")
        second_loop_cnt = (int(1e9) - _ -  1) % (_ - memory[h])
        break

    memory[h] = _

for _ in range(second_loop_cnt):
    rotation()
    
gload = reduce(lambda x, y: x + input.shape[0] - y, np.where(input == 'O')[0], 0)

print(gload)             