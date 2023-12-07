import ctypes
import os
import numpy as np

cwd = os.getcwd()
lib = ctypes.CDLL(cwd + '/day5.so')

with open('input.txt') as f:
    lines = f.readlines()
    
seeds = lines[0].strip().replace('seeds: ', '').split(' ')
seed_ranges = sorted([(int(seeds[i]), int(seeds[i]) + int(seeds[i+1])) for i in range(0, len(seeds), 2)], key=lambda x: x[0])
g_source = []
g_dest = []
g_range_size = []

line_counter = 2
for i in range(7):
    source = []
    dest = []
    range_length = []
    line_counter += 1
    while lines[line_counter] != '\n':
        values = [int(i) for i in lines[line_counter].strip().split(' ')]
        dest.append(values[0])
        source.append(values[1])
        range_length.append(values[2])
        
        line_counter += 1
        if line_counter == len(lines):
            break
        
    line_counter += 1
    g_source.append(source)
    g_dest.append(dest)
    g_range_size.append(range_length)

seed_ranges = np.array(seed_ranges, dtype=np.int_).flatten()
seed_ranges_len = len(seed_ranges)

array_lengths = np.array([len(i) for i in g_source], dtype=np.int32)
g_source = np.array([item for sublist in g_source for item in sublist])
g_dest = np.array([item for sublist in g_dest for item in sublist])
g_range_size = np.array([item for sublist in g_range_size for item in sublist])

print(lib.do_the_hard_part(
    g_source.ctypes.data_as(ctypes.POINTER(ctypes.c_long)), 
    g_dest.ctypes.data_as(ctypes.POINTER(ctypes.c_long)), 
    g_range_size.ctypes.data_as(ctypes.POINTER(ctypes.c_long)), 
    array_lengths.ctypes.data_as(ctypes.POINTER(ctypes.c_int)), 
    seed_ranges.ctypes.data_as(ctypes.POINTER(ctypes.c_long)), 
    ctypes.c_int(seed_ranges_len)
))