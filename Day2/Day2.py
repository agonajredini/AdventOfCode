lists = []
def check_asc_or_desc(lst):
    results = []
    for sublist in lst:
        is_ordered = all(sublist[i] < sublist[i + 1] for i in range(len(sublist) - 1))or \
           all(sublist[i] > sublist[i+1] for i in range(len(sublist) - 1))
           
        check_diff = any(abs(sublist[i] - sublist[i+1]) > 3 for i in range(len(sublist) - 1))
        
        if is_ordered and not check_diff:
            results.append(True)
        else:
            results.append(False)
    return results

with open("C:/Users/Life's Good/Desktop/AdventCode/Day2/input.txt") as f:
    for line in f:
        numbers = list(map(int, line.strip().split()))
        lists.append(numbers)

results = check_asc_or_desc(lists)
print(results.count(True))