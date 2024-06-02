# Approach: Traverse the matrix and check
#           for the existence.
def searchBruteForce(matrix, target):
    row, col = len(matrix), len(matrix[0])

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == target:  return True
    
    return False
# T(n) = O(row * col)

# Approach: For each row, check using BS
#           if the key exists.
def searchBetter(matrix, target):

    def found(row):
        low, high = 0, len(row)-1

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
        if found(matrix[i]):
            return True
    return False
# T(n) = O(row * log(col))

# Approach: Since each subsequent row is sorted and
#           next row has elements larger than earlier,
#           we can apply BS to the entire matrix using maths.
def searchOptimal(matrix, key):
    row, col = len(matrix), len(matrix[0])
    low, high = 0, (row * col) - 1

    while low <= high:
        mid = low + (high - low)//2
        Row = mid // col
        Col = mid % col
        if matrix[Row][Col] == key:
            return True
        elif matrix[Row][Col] > key:
            high = mid - 1
        else:
            low = mid + 1

    return False

matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]
key = 8

print(searchBruteForce(matrix, key))
print(searchBetter(matrix, key))
print(searchOptimal(matrix, key))