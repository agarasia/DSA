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
def lowerBound(arr, n, x):
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] >= x:
            ans = mid
            # look for smaller index on the left
            high = mid - 1
        else:
            low = mid + 1  # look on the right
    return ans

def max1sOptimal(matrix):
    cnt_max = 0
    index = -1

    # traverse the rows:
    for i in range(len(matrix)):
        # get the number of 1's:
        cnt_ones = len(matrix[i]) - lowerBound(matrix[i], len(matrix[i]), 1)
        if cnt_ones > cnt_max:
            cnt_max = cnt_ones
            index = i
    return index
    
    return ans
# T(n) = O(m * log n) where
# m = number of rows
# n = number of columns

mat = [[0, 0, 1],
       [1, 1, 1],
       [0, 0, 0]]

print(max1sBruteForce(mat))
print(max1sOptimal(mat))