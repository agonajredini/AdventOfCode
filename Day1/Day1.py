left_numbers = []
right_numbers = []
difference = []

with open("Day1\input.txt") as f:
    for line in f:
        parts = line.split()
        
        left_numbers.append(int(parts[0]))
        right_numbers.append(int(parts[1]))
        
left_numbers.sort()
right_numbers.sort()

for i in range(len(left_numbers)):
    difference.append(abs(right_numbers[i] - left_numbers[i]))

print(sum(difference))