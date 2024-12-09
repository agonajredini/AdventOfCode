rules = []
updates = []
valid_updates = []
invalid_updates = []
middle = []
with open("Day5/input.txt") as file:
    for line in file:
        line = line.strip()
        if '|' in line:
            pair = tuple(map(int, line.split('|')))
            rules.append(pair)
        elif ',' in line:
            numbers= list(map(int, line.split(',')))
            updates.append(numbers)

for update in updates:
    flag = False
    for i in range(len(update)-1):
        if (update[i+1], update[i]) in rules:
            flag = True
            break
    if not flag: valid_updates.append(update)
    else: invalid_updates.append(update)

for update in invalid_updates:
    flag = True
    while flag:
        for i in range(len(update)-1):
            if (update[i+1], update[i]) in rules:
                flag = True
                update[i], update[i+1] = update[i+1], update[i]
                break
            else:
                flag = False
                
for update in invalid_updates:
     middle.append(update[len(update)//2])
    
print(sum(middle))