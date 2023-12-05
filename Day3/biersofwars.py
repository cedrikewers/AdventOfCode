def has_two_nums_adjescent(matrix: list[list], lindex, cindex):
    def is_int(s):
        return type(s) == tuple

    gear_numbers = []

    ltuple = (lindex -1, lindex + 1)
    carray = [cindex - 1, cindex + 1]

    if carray[0] < 0:
        carray[0] = 0
    elif is_int(matrix[lindex][carray[0]]):
            gear_numbers.append(matrix[lindex][carray[0]])

    if carray[1] >= len(matrix[0]):
        carray[1] = len(matrix[0]) - 1
    elif is_int(matrix[lindex][carray[1]]):
            gear_numbers.append(matrix[lindex][carray[1]])
        
    for new_lindex in ltuple:
        if new_lindex < 0 or new_lindex >= len(matrix):
            continue

        for new_cindex in range(carray[0], carray[1] + 1):
            if is_int(matrix[new_lindex][new_cindex]):
                gear_numbers.append(matrix[new_lindex][new_cindex])
    
    if len(set(gear_numbers)) == 2:
        return list(set(gear_numbers))
    return []


with open('input.txt') as f:
    lines = f.readlines()

numbercouts = {}

inputmatrix = [[c for c in line.strip()] for line in lines]
digits = [str(i) for i in range(10)]
for line in inputmatrix:
    num = ''
    for index, char in enumerate(line):
        if char in digits:
            num += char
        elif len(num):
            numbercouts[num] = numbercouts.get(num, 0) + 1
            for i in range(index - len(num), index):
                line[i] = (int(num), numbercouts[num])
            num = ''
    if len(num):
        for i in range(len(line) - len(num), len(line)):
            numbercouts[num] = numbercouts.get(num, 0) + 1
            line[i] = (int(num), numbercouts[num])

results = []
gsum = 0
for line in inputmatrix:
    print(line)

for lindex, line in enumerate(inputmatrix):
    for cindex, char in enumerate(line):
        if char == '*':
            res = has_two_nums_adjescent(inputmatrix, lindex, cindex)
            if len(res):
                 results.append(res)
                 gsum += res[0][0] * res[1][0]

print(results)
print(gsum)

