import numpy as np
from functools import cmp_to_key

card_value = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 1,
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

jvals = np.array([[14], [13], [12], [10], [9], [8], [7], [6], [5], [4], [3], [2]])
x2, y2 = np.meshgrid(jvals, jvals)
x3, y3, z3 = np.meshgrid(jvals, jvals, jvals)
x4, y4, z4, w4 = np.meshgrid(jvals, jvals, jvals, jvals)
x5, y5, z5, w5, v5 = np.meshgrid(jvals, jvals, jvals, jvals, jvals)

combinations = {
    1: jvals,
    2: np.column_stack((x2.ravel(), y2.ravel())),
    3: np.column_stack((x3.ravel(), y3.ravel(), z3.ravel())),
    4: np.column_stack((x4.ravel(), y4.ravel(), z4.ravel(), w4.ravel())),
    5: np.column_stack((x5.ravel(), y5.ravel(), z5.ravel(), w5.ravel(), v5.ravel()))
}

def get_hand_type(hand: list | np.ndarray) -> int:
    hand = np.array(hand)
    _, counts = np.unique(hand, return_counts=True)
    
    if counts.max() == 5:
        return 7
    elif counts.max() == 4:
        return 6
    
    sorted_counts = sorted(counts, reverse=True)
    if sorted_counts[0:2] == [3, 2]:
        return 5
    elif counts.max() == 3:
        return 4
    elif sorted_counts[0:2] == [2, 2]:
        return 3
    elif counts.max() == 2:
        return 2
    else:
        return 1 

def compare_hands(hand1: tuple[list, int], hand2: tuple[list, int]) -> int:
    best_hand1_type = get_hand_type(hand1[0])
    if 1 in hand1[0]:
        hand = np.array(hand1[0])    
        j_pos= np.where(hand == 1)[0]
        no_of_js = j_pos.shape[0]
        
        for combination in combinations[no_of_js]:
            new_hand = hand.copy()
            for i, rep_val in zip(j_pos, combination):
                new_hand[i] = rep_val
            
            new_hand_type = get_hand_type(new_hand)
            if new_hand_type > best_hand1_type:
                best_hand1_type = new_hand_type
    
    best_hand2_type = get_hand_type(hand2[0])
    if 1 in hand2[0]:
        hand = np.array(hand2[0])    
        j_pos = np.where(hand == 1)[0]
        no_of_js = j_pos.shape[0]
        
        for combination in combinations[no_of_js]:
            new_hand = hand.copy()
            for i, rep_val in zip(j_pos, combination):
                new_hand[i] = rep_val
            
            new_hand_type = get_hand_type(new_hand)
            if new_hand_type > best_hand2_type:
                best_hand2_type = new_hand_type
    
    if best_hand1_type < best_hand2_type:
        return -1
    elif best_hand1_type > best_hand2_type:
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

sorted_hands = sorted(hand_biddings, key=cmp_to_key(compare_hands))

out_val = 0

for i, hand in enumerate(sorted_hands):
    out_val += (i + 1) * hand[1]
    
print(out_val)