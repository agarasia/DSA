# Approach: Keep track of opening and closing
#           of the brackets and then find the max. depth.
def maxDepth(expr):
    opened = 0
    ans = float('-inf')

    for char in expr:
        if char == '(':
            opened += 1
            ans = max(ans, opened)
        if char == ')':
            opened -= 1
    
    return ans
# T(n) = O(n)   where n = length of string

expr = "()(())"

print(maxDepth(expr))