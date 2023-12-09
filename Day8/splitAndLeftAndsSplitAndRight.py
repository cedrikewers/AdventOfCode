import re
import ctypes
import os
import numpy as np

# Die Lösung ist > 20_000_000_000

os.system('gcc -shared -fopenmp -o day8.so -fPIC day8.c')

cwd = os.getcwd()
lib = ctypes.CDLL(cwd + '/day8.so')

with open('input.txt') as f:
    lines = f.readlines()
    
instructions = np.array([1 if c == 'R' else 0 for c in lines[0].strip()], dtype=np.int8)

lut =  {}
nodes = []
end_nodes = []
start_nodes = []

for index, line in enumerate(lines[2:]):
    lut[line[:3]] = index
    if line[2:3] == 'Z':
        end_nodes.append(index)
    if line[2:3] == 'A':
        start_nodes.append(index)

for line in lines[2:]:
    result = re.match(r'([A-Z0-9]{3}) = \(([A-Z0-9]{3}), ([A-Z0-9]{3})\)', line)
    key = result.group(1)
    left = result.group(2)
    right = result.group(3)
        
    nodes.append((lut[left], lut[right]))

nodes = np.array(nodes, dtype=np.int16)

print(start_nodes)
print(nodes)

# nodes = np.array(nodes, dtype=ctypes.c_short).ravel()
# directions = np.array(instructions, dtype=ctypes.c_short)
# zs = np.array(end_nodes, dtype=ctypes.c_short)
# start_nodes = np.array(start_nodes, dtype=ctypes.c_short)

# res = lib.do_the_hard_part(
#     directions.ctypes.data_as(ctypes.POINTER(ctypes.c_short)),
#     ctypes.c_int(directions.shape[0]),
#     nodes.ctypes.data_as(ctypes.POINTER(ctypes.c_short)),
#     ctypes.c_int(nodes.shape[0]),
#     start_nodes.ctypes.data_as(ctypes.POINTER(ctypes.c_short)),
#     ctypes.c_int(start_nodes.shape[0]),
#     zs.ctypes.data_as(ctypes.POINTER(ctypes.c_short)),
#     ctypes.c_int(zs.shape[0])
# )

# print(res)

# def all_zs(nodes: list) -> bool:
#     for node in nodes:
#         if node not in zs:
#             return False
#     return True

# instruction_counter = 0
# while not all_zs(current_nodes):
#     new_current_nodes = []
#     for current_node in current_nodes:
#         new_current_nodes.append(nodes[current_node][instructions[instruction_counter % len(instructions)]])
#     instruction_counter += 1
#     current_nodes = new_current_nodes
    
# print(instruction_counter)