from functools import reduce

with open('input.txt') as f:
    lines = f.readlines()
    
def get_no_of_options(time, record):
    no = 0
    for i in range(time):
        if (time - i) * i > record:
            no += 1        
    return no
    
time = list(filter(lambda x: x!= '', lines[0].strip().split(' ')[1:]))
record = list(filter(lambda x: x!= '', lines[1].strip().split(' ')[1:]))

options = []

for time, record in zip(time, record):
    options.append(get_no_of_options(int(time), int(record)))
    
print(reduce(lambda x, y: x*y, options))