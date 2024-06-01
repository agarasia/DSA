# Approach: Traverse each row and find the number
#           of ones. Return the index of the required row.
def max1sBruteForce(mat):
    ans, col = -1, 0

    for i in range(len(mat)):
        row = sum(mat[i])
        if row > col:
            col = row
            ans = i
    
    return ans
# T(n) = O(m * n) where
# m = number of rows
# n = number of columns

# Approach: For each row, find the first and last occurence
#           of 1s, the one with the most difference is our answer.
def lastOccurence(row):
    low, high = 0, len(row)-1
    ans = -1

    while low <= high:
        mid = low + (high - low)//2
        if row[mid] > 0:
            low = mid + 1
        else:
            high = mid - 1
    
    return high
        

def firstOccurence(row):
    low, high = 0, len(row)-1
    ans = -1

    while low <= high:
        mid = low + (high - low)//2
        if row[mid] > 0:
            high = mid - 1
        else:
            low = mid + 1
    
    return low

def max1sOptimal(mat):
    row = len(mat)
    ans = -1
    sumRow = -1
    for i in range(row):
        first, last = firstOccurence(mat[i]), lastOccurence(mat[i])
        sum = last - first
        if sum > sumRow:
            sumRow = sum
            ans = i
    
    return ans
# T(n) = O(m * log n) where
# m = number of rows
# n = number of columns

mat = [[0, 0, 1],
       [1, 1, 1],
       [0, 0, 0]]

print(max1sBruteForce(mat))
print(max1sOptimal(mat))