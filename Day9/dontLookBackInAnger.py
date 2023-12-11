def simplify(nums: list[int]) -> list[list[int]]:
    result = [nums]
    
    while not all(x == 0 for x in result[-1]):
        last = result[-1]
        result.append([r - l for l, r in zip(last, last[1:])])
    
    return result

def extrapolate_backwards(nums: list[list[int]]) -> int:
    for l, r in zip(nums[::-1], nums[::-1][1:]):
        r.insert(0, r[0] - l[0])
        
    
    return nums[0][0]

with open('input.txt') as f:
    lines = f.readlines()

input = [[int(x) for x in line.strip().split(' ')] for line in lines]

extrapolated_values = [extrapolate_backwards(simplify(nums)) for nums in input]
print(sum(extrapolated_values))