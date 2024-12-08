matrix = []
with open("Day4\input.txt") as f:
    for line in f:
        matrix.append(list(line.strip()))

def count_word_in_matrix(matrix, word):
    word_length = len(word)
    count = 0
   
    for row in matrix:
        row_string = ''.join(row) 
        count += row_string.count(word)
    
    for col_idx in range(len(matrix[0])):  
        col_string = ''.join([matrix[row_idx][col_idx] for row_idx in range(len(matrix))]) 
        count += col_string.count(word)
    
    for start_row in range(len(matrix)):
        diag_string = ''
        row, col = start_row, 0
        while row < len(matrix) and col < len(matrix[0]):
            diag_string += matrix[row][col]
            row += 1
            col += 1
        count += diag_string.count(word)
    
    for start_col in range(1, len(matrix[0])):
        diag_string = ''
        row, col = 0, start_col
        while row < len(matrix) and col < len(matrix[0]):
            diag_string += matrix[row][col]
            row += 1
            col += 1
        count += diag_string.count(word)
    
    
    for start_row in range(len(matrix)):
        diag_string = ''
        row, col = start_row, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            diag_string += matrix[row][col]
            row += 1
            col -= 1
        count += diag_string.count(word)
    
    for start_col in range(len(matrix[0]) - 2, -1, -1):
        diag_string = ''
        row, col = 0, start_col
        while row < len(matrix) and col >= 0:
            diag_string += matrix[row][col]
            row += 1
            col -= 1
        count += diag_string.count(word)
    
    return count

word1 = "XMAS"
count1 = count_word_in_matrix(matrix, word1)
word2 = "SAMX"
count2 = count_word_in_matrix(matrix, word2)
print(sum([count1, count2]))