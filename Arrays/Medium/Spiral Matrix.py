def spiralMatrix(matrix):
    row = len(matrix)
    col = len(matrix[0])
    top, left = 0, 0
    bottom, right = col-1, row-1
    ans = []

    while top <= bottom and left <= right:
        for i in range(left, right+1):
            ans.append(matrix[top][i])
        top += 1

        for i in range(top, bottom+1):
            ans.append(matrix[i][right])
        right -= 1

        for i in range(right, left-1, -1):
            ans.append(matrix[bottom][i])
        bottom -= 1

        for i in range(bottom, top-1, -1):
            ans.append(matrix[i][left])
        left += 1

    return ans

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralMatrix(matrix))