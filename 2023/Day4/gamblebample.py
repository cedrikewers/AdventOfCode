with open('input.txt') as f:
    lines = f.readlines()
    
cards = []    
    
for index, line in enumerate(lines):
    line = line.strip()
    line = line.replace(f'Card {index+1}:', '')
    
    temp = line.split('|')
    temp = (temp[0].split( ), temp[1].split( ))
    
    cards.append(temp)
    
results = []    
    
for card in cards:
    matches = -1
    for number_we_have in card[1]:
        if number_we_have in card[0]:
            matches += 1
    
    if matches > -1:
        results.append(2**matches)

print(sum(results))
    
    
    