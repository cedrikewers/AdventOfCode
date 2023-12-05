digits = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

with open('input.txt') as f:
    lines = f.readlines()

gval = 0
for line in lines:
    lfinds = {}
    rfinds = {}
    for word in digits.keys():
        if word in line:
            lfinds[word] = line.find(word)
            rfinds[word] = line.rfind(word)
    
    val = digits[min(lfinds, key=lfinds.get)] * 10
    val += digits[max(rfinds, key=rfinds.get)]

    print(val)
    gval += val

print(gval)

    
