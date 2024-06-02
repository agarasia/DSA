# Approach: Use BS to eliminate halves
#           among rows by selecting the highest
#           element in each column and check 
#           for the top and bottom elements.
def peakElement(mat):
    def findColIndex(row):
        n = len(row)
        element = max(row)

        for i in range(n):
            if row[i] == element:
                return i

    n = len(mat)
    low, high = 0, n - 1
    while low <= high:
        mid = low + (high - low)//2
        maxCol = findColIndex(mat[mid])

        top = mat[mid-1][maxCol] if mid - 1 >= 0 else -1
        bottom = mat[mid+1][maxCol] if mid + 1 < n else -1

        if mat[mid][maxCol] > top and mat[mid][maxCol] > bottom:
            return [mid, maxCol]
        elif mat[mid][maxCol] > top and mat[mid][maxCol] < bottom:
            low = mid + 1
        else:
            high = mid - 1
# T(n) = O(m * log n)

mat = [[47, 30, 35, 8, 25],
       [6, 36, 19, 41, 40],
       [24, 37, 13, 46, 5],
       [3, 43, 15, 50, 19],
       [6, 15, 7, 25, 10]]

print(peakElement(mat))