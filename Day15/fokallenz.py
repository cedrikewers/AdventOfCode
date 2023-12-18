from functools import reduce

with open('input.txt') as f:
    lines = f.readlines()

def holiday_ascii_string_helper(input: str) -> int:
    out = 0
    for c in input:
        out += ord(c)
        out *= 17
        out %= 256
    
    return out

input = lines[0].strip().split(',')
print(sum(map(holiday_ascii_string_helper, input)))