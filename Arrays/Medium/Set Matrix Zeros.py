def setMatrixZerosBruteForce(nums):
    # Approach: Travserse the matrix, find the zero elements,
    #           set the respective row and column as zero.
    def setRow(nums, cols, row):
        for i in range(cols):
            if nums[row][i] != 0: nums[row][i] = -float('inf')

    def setCol(nums, rows, col):
        for i in range(rows):
            if nums[i][col] != 0: nums[i][col] = -float('inf')

    m = len(nums)
    if m == 1:  n = 0
    else:       n = len(nums[0])

    # Traversing the matrix
    for i in range(m):
        for j in range(n):
            if nums[i][j] == 0:
                # If zero is found, we set the row and col to -inf
                setRow(nums, n, i)
                setCol(nums, m, j)

    # For all elements marked with -inf, we change them to 0
    for i in range(m):
        for j in range(n):
            if nums[i][j] == -float('inf'):
                nums[i][j] = 0
    
    return nums
# ___________________________________________________________________


def setMatrixZerosBetter(matrix):
    # Approach: Use auxiliary arrays to keep track of
    #           zeros and set the rows and columns while
    #           traversing the matrix.
    m = len(matrix)
    n = len(matrix[0])
    
    # Initialize the auxiliary arrays
    rows = [0]*m
    cols = [0]*n

    # Traverse and keep track of zero elements
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows[i] = 1
                cols[j] = 1
    
    # Use the arrays to traverse the matrix and set zeros
    for i in range(m):
        for j in range(n):
            if rows[i] == 1 or cols[j] == 1:
                matrix[i][j] = 0
    
    return matrix


matrix = [[1,1,1], [1,0,1], [1,1,1]]
print(matrix, [[0,1,2,0],[3,4,5,2],[1,3,1,5]], [[-1,2,3]])
print(setMatrixZerosBruteForce(matrix), setMatrixZerosBruteForce([[0,1,2,0],[3,4,5,2],[1,3,1,5]]), setMatrixZerosBruteForce([[-1,2,3]]))
print(setMatrixZerosBetter(matrix), setMatrixZerosBetter([[0,1,2,0],[3,4,5,2],[1,3,1,5]]), setMatrixZerosBetter([[-1,2,3]]))