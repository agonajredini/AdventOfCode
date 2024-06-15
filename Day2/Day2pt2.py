lists = []
def check_asc_or_desc(lst):
    results = []
    for sublist in lst:
        valid = False
        for i in range (len(sublist)):
            mod_sublist = sublist[:i] + sublist[i+1:]
            is_ordered = all(mod_sublist[j] < mod_sublist[j + 1] for j in range(len(mod_sublist) - 1))or \
            all(mod_sublist[j] > mod_sublist[j+1] for j in range(len(mod_sublist) - 1))
            
            check_diff = any(abs(mod_sublist[j] - mod_sublist[j+1]) > 3 for j in range(len(mod_sublist) - 1))
            
            if is_ordered and not check_diff:
                valid = True
                break
                
        results.append(valid)
    return results

with open("Day2\input.txt") as f:
    for line in f:
        numbers = list(map(int, line.strip().split()))
        lists.append(numbers)

results = check_asc_or_desc(lists)
print(results.count(True))