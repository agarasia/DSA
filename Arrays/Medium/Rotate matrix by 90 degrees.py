def rotateMatrix(matrix):
    # Approach : Transpose the matrix and reverse the rows

    # Transposing
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(i+1, cols):
            # Swap elements at (i, j) and (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reversing the rows of the matrix
    for i in range(len(matrix)):
        start, end = 0, len(matrix[0]) - 1
        while start < end:
            matrix[i][start], matrix[i][end] = matrix[i][end], matrix[i][start]
            start += 1
            end -= 1
    return matrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)
print(rotateMatrix(matrix))