# Approach: Prune the search space,
#           which is min(mat) - max(mat) by BS via
#           counting the number of elements smaller than
#           the required elements and then do as necessary.
def median(mat):
    def upperBound(row, key):
        low, high = 0, len(row) - 1

        while low <= high:
            mid = low + (high - low)//2
            if row[mid] >= key:
                high = mid - 1
            else:
                low = mid + 1
        
        return low

    def count(mat, key):
        m = len(mat)
        count = 0

        for i in range(m):
            count += upperBound(mat[i], key)
        return count    

    m, n = len(mat), len(mat[0])
    low, high = float('inf'), float('-inf')

    for i in range(m):
        low = min(low, mat[i][0])
        high = max(high, mat[i][n-1])
    
    required = (m*n)//2

    while low <= high:
        mid = low + (high - low)//2
        smallerElements = count(mat, mid)
        if smallerElements <= required:
            low = mid + 1
        else:
            high = mid - 1
    
    return low
# T(n) = O(m logn)

mat = [[1, 2, 3, 4, 5],
       [8, 9, 10, 11, 13],
       [21, 23, 25, 27, 29]]

print(median(mat))