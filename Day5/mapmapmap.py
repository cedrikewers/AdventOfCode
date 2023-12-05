with open('input.txt') as f:
    lines = f.readlines()
    
seeds = lines[0].strip().replace('seeds: ', '').split(' ')
conversion_ranges = {}

def convert(conversions, seed):
    for conv in conversions:
        dest = conv[0]
        source = conv[1]
        len = conv[2]
        if seed < source or seed >= source + len:
            #print(f'{seed} is not in range {source} to {source + len -1}')
            continue
        #print(f'{seed} is in range {source} to {source + len-1}, returning {seed + dest - source}')
        return seed + dest - source
    #print(f'{seed} is not in any range, returning {seed}')
    return seed

line_counter = 2
key = 'seed'
for i in range(7):
    conversions = []
    key = lines[line_counter].strip().replace(f'{key}-to-', '').replace(' map:', '')
    line_counter += 1
    while lines[line_counter] != '\n':
        values = [int(i) for i in lines[line_counter].strip().split(' ')]
        conversions.append(values)
        line_counter += 1
        
        if line_counter == len(lines):
            break
        
    conversion_ranges[i] = conversions
    line_counter += 1

#print(conversion_ranges)
res = []
for seed in seeds:
    seed = int(seed)
    loc = seed
    for i in range(7):
        loc = convert(conversion_ranges[i], loc)
    res.append(loc)
print(res)
