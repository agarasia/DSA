# Approach: Create a non-decreasing monotonic stack
#           while removing the k digits.
def removeKDigits(num, k):
    if len(num) == k:
        return "0"
    
    stack = []

    for i in num:
        while stack and k > 0 and stack[-1] > i:
            stack.pop()
            k -= 1
        stack.append(i)
    
    # Remove the remaining digits from the end if k is still greater than 0
    while k > 0:
        stack.pop()
        k -= 1
    
    # Remove leading zeros
    result = ''.join(stack).lstrip('0')
    
    return result if result else "0"
# T(n) = O(n), S(n) = O(n)

num = "1432219"
k = 3

print(removeKDigits(num, k))