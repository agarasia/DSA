def nextGreaterElementBruteForce(nums):
    res = [-1]*len(nums)
    
    for i in range(2*len(nums)):
        for j in range((i+1)%len(nums), len(nums)):
            if nums[j] > nums[i%len(nums)]:
                res[i%len(nums)] = nums[j]
                break
    
    return res

def nextGreaterElementOptimal(nums):
    n = len(nums)
    stack = []
    res = []

    for i in range(2*n-1, -1, -1):
        if not stack:
            res.append(-1)
        elif stack and stack[-1] > nums[i%n]:
            res.append(stack[-1])
        elif stack and stack[-1] < nums[i%n]:
            while stack and stack[-1] <= nums[i%n]:
                stack.pop()
            if not stack:
                res.append(-1)
            else:
                res.append(stack[-1])
        stack.append(nums[i%n])

    res = res[::-1]

    return res[:n]

nums = [5, 7, 2, 1, 6, 0]

print(nextGreaterElementBruteForce(nums))
print(nextGreaterElementOptimal(nums))