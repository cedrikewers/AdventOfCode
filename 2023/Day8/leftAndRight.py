from __future__ import annotations
import re    

with open('input.txt') as f:
    lines = f.readlines()
    
instructions = [1 if c == 'R' else 0 for c in lines[0].strip()]

nodes = {}
for line in lines[2:]:
    result = re.match(r'([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)', line)
    nodes[result.group(1)] = (result.group(2), result.group(3))

current = 'AAA'
instruction_counter = 0
while current != 'ZZZ':
    current = nodes[current][instructions[instruction_counter % len(instructions)]]
    instruction_counter += 1
    
print(instruction_counter)