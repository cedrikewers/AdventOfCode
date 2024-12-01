import re
import numpy as np
from functools import reduce
from itertools import product

with open('input.txt') as f:
    lines = f.readlines()

input = [(
    np.array([c for c in line.strip().split()[0]]), 
    line.strip().split()[1].split(',')
    ) for line in lines]

valid_permutaions_count = 0

for linenbr, (springs, counts) in enumerate(input):
    spring_indices = np.where(springs == '?')[0]
    
    regex: str = '^\\.*' + reduce(lambda a, b: a + b, [f"#{{{count}}}" + '\\.+' for count in counts])
    regex = regex[0:-1] + '*$'
    
    for arrangement in product('#.', repeat=spring_indices.shape[0]):
        for index, replacement_charachter in zip(spring_indices, arrangement):
            springs[index] = replacement_charachter
            
        if re.match(regex, ''.join(springs)):
            valid_permutaions_count += 1

print(valid_permutaions_count)
    