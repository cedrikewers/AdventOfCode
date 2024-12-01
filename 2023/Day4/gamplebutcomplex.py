with open('input.txt') as f:
    lines = f.readlines()
    
cards = []    
    
for index, line in enumerate(lines):
    line = line.strip()
    line = line.replace(f'Card {index+1}:', '')
    
    temp = line.split('|')
    temp = (temp[0].split( ), temp[1].split( ))
    
    cards.append(temp)

matches_per_card = [] 
card_counts = {i: 1 for i in range(len(cards))}
    
for card in cards:
    matches = 0
    for number_we_have in card[1]:
        if number_we_have in card[0]:
            matches += 1
    
    matches_per_card.append(matches)

for parent_card, matches in enumerate(matches_per_card):
    for card in range(parent_card + 1, parent_card + 1 + matches):
        if card > len(matches_per_card) - 1:
            break
        
        card_counts[card] += card_counts[parent_card]
        
        

print(card_counts)
print(sum(card_counts.values()))