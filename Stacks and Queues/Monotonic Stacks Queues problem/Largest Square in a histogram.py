# Approach: While traversing the array, find the next
#           smaller element on the left and on the right
#           to formm a rectangle.
def areaOfRectangleBruteForce(heights):
    maxArea = 0

    for i in range(len(heights)):
        minHeight = float('inf')
        for j in range(i, len(heights)):
            minHeight = min(minHeight, heights[j])
            maxArea = max(maxArea, minHeight * (j - i + 1))
    
    return maxArea
# T(n) = O(n**2)
# S(n) = O(1)

# Approach: Optimize the process of getting the next smaller
#           element using monotonic stacks for next smaller element.
def areaOfRectangleOptimal(heights):
    n = len(heights)
    stack = []
    leftSmall, rightSmall = [-1]*n, [-1]*n

    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        if not stack:
            leftSmall[i] = 0
        else:
            leftSmall[i] = stack[-1] + 1
        stack.append(i)

    while stack:
        stack.pop()
    
    for i in range(n-1, -1, -1):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        if not stack:
            rightSmall[i] = n-1
        else:
            rightSmall[i] = stack[-1] - 1
        stack.append(i)

    maxArea = 0
    for i in range(n):
        maxArea = max(maxArea, heights[i] * (rightSmall[i] - leftSmall[i] + 1))
    
    return maxArea
# T(n) = O(n)
# S(n) = O(n)   for storing the stack

heights = [2, 1, 5, 6, 2, 3]

print(areaOfRectangleBruteForce(heights))
print(areaOfRectangleOptimal(heights))