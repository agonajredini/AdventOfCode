matrix = []
with open("Day4\input.txt") as f:
    for line in f:
        matrix.append(list(line.strip()))

def count_diagonals(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            if matrix[i][j] == 'A':
                
                top_left = matrix[i-1][j-1]
                top_right = matrix[i-1][j+1]
                bottom_left = matrix[i+1][j-1]
                bottom_right = matrix[i+1][j+1]
                
                if top_left in ['M', 'S'] and bottom_right in ['M', 'S'] and top_right in ['M', 'S'] and bottom_left in ['M', 'S']:
                    if top_left != bottom_right and top_right != bottom_left:
                        count += 1

    return count

print(count_diagonals(matrix))
