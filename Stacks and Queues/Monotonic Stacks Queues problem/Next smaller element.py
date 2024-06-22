def nextSmallerElementBruteForce(nums):
    res = [-1]*len(nums)

    for i in range(len(nums)):
        for j in range(i, -1, -1):
            if nums[i] > nums[j]:
                res[i] = nums[j]
                break
    
    return res

def nextSmallerElementOptimal(A):
    stack = []
    res = []

    for i in range(len(A)):
        # Remove elements from stack that are not smaller than A[i]
        while stack and stack[-1] >= A[i]:
            stack.pop()
        # If stack is empty, no smaller previous element exists
        if not stack:
            res.append(-1)
        else:
            res.append(stack[-1])
        # Push the current element onto the stack
        stack.append(A[i])

    return res

nums = [4, 5, 2, 10, 8]

print(nextSmallerElementBruteForce(nums))
print(nextSmallerElementOptimal(nums))