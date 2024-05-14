def spiralMatrix(A):
    row, col = len(A), len(A[0])
    top, left = 0, 0 
    bottom, right = row - 1, col - 1
    ans = []
    
    while top<=bottom and left<=right:
        for i in range(left, right+1):
            ans.append(A[top][i])
        top += 1
        
        for i in range(top, bottom+1):
            ans.append(A[i][right])
        right -= 1
        
        if top <= bottom:
            for i in range(right, left-1, -1):
                ans.append(A[bottom][i])
            bottom -= 1
        
        if left <= right:
            for i in range(bottom, top-1, -1):
                ans.append(A[i][left])
            left += 1
            
    return ans

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralMatrix(matrix))