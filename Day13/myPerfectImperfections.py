import numpy as np

with open('input.txt') as f:
    lines = f.readlines()
    
parts = []
part = []
for line in lines:
    if line == '\n':
        parts.append(np.array(part))
        part = []
        continue
    part.append(list(line.strip()))
parts.append(np.array(part))    

def test_horizontal(matrix: np.ndarray) -> int:
    max_index = len(matrix) 
    for index in range(1, max_index):
        num_rows = min(index, max_index - index)
        diff_index = np.where(~np.equal(matrix[index-num_rows:index], matrix[index:index+num_rows][::-1]))
        if len(diff_index[0]) == 1:
            return index
    return 0

def test_vertical(matrix: np.ndarray) -> int:
    max_index = matrix.shape[1]
    for index in range(1, max_index):
        num_cols = min(index, max_index - index)
        diff_index = np.where(~np.equal(
                matrix[:, index-num_cols:index], 
                np.flip(matrix[:, index:index+num_cols], axis=1)
                ))
        
        if len(diff_index[0]) == 1:
            return index        
    
    return 0
        
grows = 0
gcols = 0
for part in parts:
    grows += test_horizontal(part)
    gcols += test_vertical(part)
    
print(grows * 100 + gcols)
    