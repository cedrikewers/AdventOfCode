import re
import math

with open('input.txt') as f:
    lines = f.readlines()
    
instructions = [1 if c == 'R' else 0 for c in lines[0].strip()]

nodes = {}

for line in lines[2:]:
    result = re.match(r'([A-Z0-9]{3}) = \(([A-Z0-9]{3}), ([A-Z0-9]{3})\)', line)
    key = result.group(1)
    left = result.group(2)
    right = result.group(3)
        
    nodes[key] = (left, right)

start_nodes =  list(filter(lambda x: x[2] == 'A', nodes.keys()))
end_nodes = list(filter(lambda x: x[2] == 'Z', nodes.keys()))

node_occurences = []

for start_node in start_nodes:
    print(f"Checking {start_node}")
    current_node = start_node
    for i in range(100000):
        next_node = nodes[current_node][instructions[i % len(instructions)]]
        if next_node[2] == 'Z':
            print(f"\tFound exit node {next_node} after {i + 1} steps")
            node_occurences.append(i + 1)
            break   
        current_node = next_node

print(math.lcm(*node_occurences))