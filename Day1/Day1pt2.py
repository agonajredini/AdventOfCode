left_numbers = []
right_numbers = []
similarity = []

with open("Day1\input.txt") as f:
    for line in f:
        parts = line.split()
        
        left_numbers.append(int(parts[0]))
        right_numbers.append(int(parts[1]))

for i in left_numbers:
    # add = 0
    # for j in right_numbers:
    #     if i == j:
    #         add+=1
    similarity.append(i*right_numbers.count(i))

print(sum(similarity))