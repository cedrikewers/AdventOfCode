from functools import reduce
import ctypes
import os

os.system('gcc -shared -fopenmp -o day6.so -fPIC day6.c')

cwd = os.getcwd()
lib = ctypes.CDLL(cwd + '/day6.so')

with open('input.txt') as f:
    lines = f.readlines()
    
def get_no_of_options(time, record):
    no = 0
    for i in range(time):
        if (time - i) * i > record:
            no += 1        
    return no
    
time = reduce(lambda a, b: a + b, filter(lambda x: x!= '', lines[0].strip().split(' ')[1:]))
record = reduce(lambda a, b: a + b, filter(lambda x: x!= '', lines[1].strip().split(' ')[1:]))

print(lib.do_the_hard_part(ctypes.c_long(int(time)), ctypes.c_long(int(record))))