import re
memory = ""
with open("C:/Users/Life's Good/Desktop/AdventCode/Day3/input.txt") as f:
    memory = f.read()
pattern = r'mul\((\d+),(\d+)\)'
matches = re.findall(pattern, memory)
results = [int(x)*int(y) for x, y in matches]
print(sum(results))