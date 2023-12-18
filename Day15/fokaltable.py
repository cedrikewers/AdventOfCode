with open('input.txt') as f:
    lines = f.readlines()

def holiday_ascii_string_helper(input: str) -> int:
    out = 0
    for c in input:
        out += ord(c)
        out *= 17
        out %= 256
    
    return out

def get_parts(input: str) -> tuple[int, str, int]:
    if '-' in input:
        return (holiday_ascii_string_helper(input[:-1]), input[:-1], -1)

    parts = input.split('=')
    return (holiday_ascii_string_helper(parts[0]), parts[0], int(parts[1]))
    
input = lines[0].strip().split(',')
input = list(map(get_parts, input))

hashmap = {_ : {} for _ in range(256)}
for box, label, value in input:
    if value < 0:
        try:
            del hashmap[box][label]
        except KeyError:
            pass
    else:
        hashmap[box][label] = value

gsum = 0
for index, box in enumerate(hashmap, 1):
    for box_index, focal_length in enumerate(hashmap[box].values(), 1):
        gsum += index * box_index * focal_length

print(gsum)
