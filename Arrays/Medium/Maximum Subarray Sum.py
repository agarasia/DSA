import sys

# Naive Approach
def maxSubarraySumNaive(arr):
    maxSum = -sys.maxsize - 1
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            if sum > maxSum:
                maxSum = sum
    
    return maxSum

# Optimal : Kadane's Algorithm
def maxSubarraySumOptimal(nums):
    ans = nums[0]
    curr=nums[0]
    for i in (nums[1:]):
        curr = max(i,curr+i)
        ans = max(ans,curr)
    return ans

a = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubarraySumNaive(a) == maxSubarraySumOptimal(a))