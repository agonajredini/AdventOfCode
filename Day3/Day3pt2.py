import re
memory = ""
with open("Day3\input.txt") as f:
    memory = f.read()

def toggle(text):
    is_enabled = True
    results = []
    
    pattern = r'(mul\((\d+),(\d+)\)|do\(\)|don\'t\(\))'
    matches = re.findall(pattern, text)
    
    for match in matches:
        if match[0].startswith('mul'):
            if is_enabled:
                results.append(int(match[1])*int(match[2]))
        
        elif match[0] == 'do()':
            is_enabled = True
        elif match[0] == 'don\'t()':
            is_enabled = False
    return sum(results)

results = toggle(memory)
print(results)