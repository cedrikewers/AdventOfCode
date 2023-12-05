def neighbor_is_symbol(matrix: list[list], lindex: int, cindex: int, ndigits: int) -> bool:
    def is_symbol(char: str) -> bool:
        return char != '.'

    ltuple = (lindex -1, lindex + 1)

    carray = [cindex - 1 - ndigits, cindex] # edgecases
    if carray[0] < 0:
        carray[0] = 0
    elif carray[1] >= len(matrix[0]):
        carray[1] = len(matrix[0]) - 1

    if (cindex - 1 - ndigits) >= 0 and is_symbol(matrix[lindex][carray[0]]) or cindex < len(matrix[0]) and is_symbol(matrix[lindex][carray[1]]):
        return True

    for new_lindex in ltuple:
        if new_lindex < 0 or new_lindex >= len(matrix):
            continue

        for new_cindex in range(carray[0], carray[1] + 1):
            if is_symbol(matrix[new_lindex][new_cindex]):
                return True

    return False
    

with open('input.txt') as f:
    lines = f.readlines()

inputmatrix = [[c for c in line.strip()] for line in lines]

gsum = 0
nums = [] 

for lindex, line in enumerate(inputmatrix):
    num_detected = False
    num = ''
    for cindex, char in enumerate(line):
        if ord(char) >= ord('0') and ord(char) <= ord('9'): # adding up the digits of current number
            num_detected = True
            num += char

        elif num_detected:
            num_detected = False
            ndigits = len(num)
            
            if neighbor_is_symbol(inputmatrix, lindex, cindex, ndigits):
                nums.append(int(num))
            num = ''

    if num and neighbor_is_symbol(inputmatrix, lindex, cindex + 1, len(num)):
        nums.append(int(num))
 
print(sum(nums))
