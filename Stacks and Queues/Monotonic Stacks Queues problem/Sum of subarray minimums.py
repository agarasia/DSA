# Approach: As we only need the minimum element,
#           we only record the minimum element as
#           we traverse the array. Then we add that
#           element to the result.
def sumOfMinimumsBruteForce(nums):
    sum = 0
    MOD = 10**9 + 7

    for i in range(len(nums)):
        Min = nums[i]
        for j in range(i, len(nums)):
            Min = min(Min, nums[j])
            sum = (sum + Min) % MOD
    
    return sum
# T(n) = O(n**2), S(n) = O(1)

def sumOfMinimumOptimal(nums):
    sum = 0
    MOD = 10**9 + 7
    n = len(nums)
    stack = []

    for i, val in enumerate(nums):
        while stack and val < stack[-1][1]:
            j, val2 = stack.pop()
            left = j - stack[-1][0] if stack else j + 1
            right = i - j
            sum = (sum + val2*left*right) % MOD
        stack.append((i, val))
    
    for i in range(len(stack)):
        j, val = stack[i]
        left = j - stack[i-1][0] if i > 0 else j+1
        right = n - j
        sum = (sum + val*left*right) % MOD
    
    return sum

nums = [3, 1, 2, 4]
print(sumOfMinimumsBruteForce(nums))
print(sumOfMinimumOptimal(nums))