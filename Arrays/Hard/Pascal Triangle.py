
# Variation 1: just finding the ith element of the Pascal Triangle
def pascalTriangleV1Naive(row, col):
    # Approach : Find factorial everytime for n!/(r! * (n-r)!)
    def factorial(num):
        if num == 0: return 1
        return num * factorial(num-1)
    
    row -= 1
    col -= 1

    return factorial(row)//(factorial(col)*factorial(row-col))

def pascalTriangleV1Optimal(row, col):
    # Approach : Optimize the calculation part.
    ans = 1
    row -= 1
    col -= 1

    for i in range(col):
        ans = ans * (row - i)
        ans = ans // (i+1)
    
    return ans

# Variation 2: Return the ith row of the Pascal Triangle
def pascalTriangleV2Naive(row):
    # Approach : Initialize an array to return the ith row and find the elements
    def findElement(row, col):
        ans = 1
        row -= 1
        col -= 1

        for i in range(col):
            ans = ans * (row - i)
            ans = ans // (i+1)
        
        return ans

    ans = [1] * row

    for i in range(row//2 + 2):
        ans[i], ans[row-i-1] = findElement(row, i), findElement(row, i)
    
    return ans

def pascalTriangleV2Optimal(row):
    # Approach : Observe how each element in the row is calculated
    ans = [1]
    for i in range(row-1):
        numerator = ans[-1]*(row-i-1)
        ans.append(numerator//(i+1))
    
    return ans

# Variation 3: Print the entire triangle
def pascalTriangleV3(numRows):
    # Find each row using the algorithm stated above and append it
    ans = []
    for i in range(1, numRows + 1):
        row = [1]
        for j in range(i-1):
            numerator = row[-1]*(i-j-1)
            row.append(numerator//(j+1))
        
        ans.append(row)
    return ans

row, col = 5, 3
print(pascalTriangleV1Naive(row, col), pascalTriangleV1Optimal(row, col))
print(pascalTriangleV2Naive(row), pascalTriangleV2Optimal(row))
print(pascalTriangleV3(3))