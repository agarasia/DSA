# Approach: Convert each row to a histogram and then find the 
#           maximum area of a rectangle in that histogram.
def maxArea(mat):
    def findAreaInHistogram(row):
        n = len(row)
        stack = []
        leftSmall, rightSmall = [-1]*n, [-1]*n
        maxArea = 0

        for i in range(n):
            while stack and row[stack[-1]] >= row[i]:
                stack.pop()
            if not stack:
                leftSmall[i] = 0
            else:
                leftSmall[i] = stack[-1] + 1
            stack.append(i)
        
        while stack:    stack.pop()

        for i in range(n-1, -1, -1):
            while stack and row[stack[-1]] >= row[i]:
                stack.pop()
            if not stack:
                rightSmall[i] = n - 1
            else:
                rightSmall[i] = stack[-1] - 1
            stack.append(i)
        
        for i in range(n):
            maxArea = max(maxArea, row[i] * (rightSmall[i] - leftSmall[i] + 1))
        
        return maxArea


    histogram = [[0]*len(mat[0]) for _ in range(len((mat)))]

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == "0":
                histogram[i][j] = 0
            else:
                histogram[i][j] = histogram[i-1][j] + 1
    
    maxArea = 0
    for i in range(len(mat)):
        area = findAreaInHistogram(histogram[i])
        maxArea = max(maxArea, area)

    return maxArea
# T(n) = O(m*n) where m and n represent columns and rows of the matrix respectively.
# S(n) = O(m*n) for storing the histograms.

mat = [["1","0","1","0","0"],
       ["1","0","1","1","1"],
       ["1","1","1","1","1"],
       ["1","0","0","1","0"]]

print(maxArea(mat))