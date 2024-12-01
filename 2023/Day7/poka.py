import numpy as np
from functools import cmp_to_key

card_value = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2
}

def get_hand_type(hand: list) -> int:
    hand = np.array(hand)
    unique, counts = np.unique(hand, return_counts=True)
    
    if counts.max() == 5:
        return 7
    elif counts.max() == 4:
        return 6
    
    sorted_counts = sorted(counts, reverse=True)
    if sorted_counts[0:2] == [3, 2]:
        return 5
    elif counts.max() == 3:
        return 4
    elif sorted_counts[0:3] == [2, 2, 1]:
        return 3
    elif counts.max() == 2:
        return 2
    else:
        return 1  
    

def compare_hands(hand1: tuple[list, int], hand2: tuple[list, int]) -> int:
    hand_type_1 = get_hand_type(hand1[0])
    hand_type_2 = get_hand_type(hand2[0])    
    
    if hand_type_1 < hand_type_2:
        return -1
    elif hand_type_1 > hand_type_2:
        return 1
    
    for card1, card2 in zip(hand1[0], hand2[0]):
        if card1 < card2:
            return -1
        elif card1 > card2:
            return 1
    return 0

with open('input.txt') as f:
    lines = f.readlines()
    
hand_biddings = []

for line in lines:
    values = line.strip().split(' ')
    hand = [card_value[card] for card in values[0]]
    value = int(values[1])
    hand_biddings.append((hand, value))

sorted_hands = sorted(hand_biddings, key=cmp_to_key(compare_hands), reverse=False)

out_val = 0

for i, hand in enumerate(sorted_hands):
    #print(f"{hand} has rank {i + 1}. Out val = {out_val} + {hand[1]} * {i+1}")
    out_val += (i + 1) * hand[1]
    
print(out_val)
