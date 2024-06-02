# Approach: Search the entire matrix for the
#           target.
def searchBruteForce(matrix, target):
    row, col = len(matrix), len(matrix[0])

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == target:  return True
    
    return False
# T(n) = O(n * m)

# Approach: For each row, apply BS to check if
#           target key exists.
def searchBetter(matrix, target):
    def found(row):
        low, high = 0, len(row) - 1

        while low <= high:
            mid = low + (high - low)//2
            if row[mid] == target:
                return True
            elif row[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        return False

    row = len(matrix)
    
    for i in range(row):
        if found(matrix[i]):    return True
    
    return False
# T(n) = O(n * log m)

# Approach: Since each row and each column is sorted,
#           apply BS from top-right corner and pivot 
#           from there by changing row or column.
def searchOptimal(matrix, target):
    n1, n2 = len(matrix), len(matrix[0])
    row, col = 0, n2 - 1
    
    while row < n1 and col >= 0:
        if matrix[row][col] == target: 
            return True
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1
    
    return False
# T(n) = O(n + m)

matrix = [[1,4,7,11,15],
          [2,5,8,12,19],
          [3,6,9,16,22],
          [10,13,14,17,24],
          [18,21,23,26,30]]
target = 30

print(searchBruteForce(matrix, target))
print(searchBetter(matrix, target))
print(searchOptimal(matrix, target))