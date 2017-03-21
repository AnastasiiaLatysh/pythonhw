def diagonal_reverse(matrix) :
    if not matrix: return []
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

def print_matrix(matrix) :
    for i in range(len(matrix)):
        print(matrix[i])

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print_matrix(matrix)
print()

matrix = diaginal_reverse(matrix)
print_matrix(matrix)