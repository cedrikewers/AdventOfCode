import sys

process_nbr = int(sys.argv[1])

with open('input.txt') as f:
    lines = f.readlines()
    
seeds = lines[0].strip().replace('seeds: ', '').split(' ')
seed_ranges = sorted([(int(seeds[i]), int(seeds[i]) + int(seeds[i+1])) for i in range(0, len(seeds), 2)], key=lambda x: x[0])
conversion_ranges = {}

def convert_backwards(conversions, seed):
    for conv in conversions:
        dest = conv[1]
        source = conv[0]
        len = conv[2]
        if seed < source or seed >= source + len:
            #print(f'{seed} is not in range {source} to {source + len -1}')
            continue
        #print(f'{seed} is in range {source} to {source + len-1}, returning {seed + dest - source}')
        return seed + dest - source
    #print(f'{seed} is not in any range, returning {seed}')
    return seed



line_counter = 2
for i in range(7):
    conversions = []
    line_counter += 1
    while lines[line_counter] != '\n':
        values = [int(i) for i in lines[line_counter].strip().split(' ')]
        conversions.append(values)
        line_counter += 1
        
        if line_counter == len(lines):
            break
        
    conversion_ranges[i] = conversions
    line_counter += 1

def thread_func(l, r):
    print(f'Running from {l} to {r}')
    for i in range(l, r):
        seed = i
        for j in range(6, -1, -1):
            seed = convert_backwards(conversion_ranges[j], seed)
        
        for r in seed_ranges:
            if seed >= r[0] and seed < r[1]:
                print(f'Process {process_nbr} Found seed {seed} in range {r}, smallest location number is {i}')
                exit()

#print(conversion_ranges)
max = 100_000_000
thread_func((max // 16) * process_nbr, (max // 16) * (process_nbr + 1))
print(f'Process {process_nbr} found nothing')


